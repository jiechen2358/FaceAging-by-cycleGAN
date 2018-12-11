import argparse

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.autograd import Variable

import matplotlib.pyplot as plt
import shutil
import numpy as np
import math
import os

parser = argparse.ArgumentParser(description='option for gender age classifier')
parser.add_argument('-a', '--age', action='store_true', help='switch classifier to age')
parser.add_argument('-b', '--batch_size', type=int, metavar='', default=64, help='batch size')
parser.add_argument('-ep', '--epoch', type=int, metavar='', default=100, help='number of epoch')
parser.add_argument('--sgd', action='store_true', help='use SGD optimizer')
args = parser.parse_args()


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 96, kernel_size=7, stride=4),
            nn.BatchNorm2d(96),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2))
        self.conv2 = nn.Sequential(
            nn.Conv2d(96, 256, kernel_size=5, padding=2),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2))
        self.conv3 = nn.Sequential(
            nn.Conv2d(256, 384, kernel_size=3, padding=1),
            nn.BatchNorm2d(384),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2))
        self.fc1 = nn.Linear(384 * 6 * 6, 512)
        self.fc2 = nn.Linear(512, 512)
        self.fc3 = nn.Linear(512, 2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = x.view(x.size(0), -1)
        x = F.dropout(F.relu(self.fc1(x)))
        x = F.dropout(F.relu(self.fc2(x)))
        x = self.fc3(x)
        return x


def check_acc(model, data_loader):
    num_correct, num_sample = 0, 0
    for images, labels in data_loader:
        images = Variable(images)
        outputs = model(images)
        _, pred = torch.max(outputs.data, 1)
        num_sample += labels.size(0)
        num_correct += (pred == labels).sum()
    return float(num_correct) / num_sample


def plot_performance(epoches, train_accs, val_accs, path='performance.png'):
    plt.figure()
    plt.plot(np.array(epoches), np.array(train_accs), label='training accuracy')
    plt.plot(np.array(epoches), np.array(val_accs), label='validation accuracy')
    plt.title('Accuracy on training & validation')
    plt.ylabel('Accuracy')
    plt.xlabel('Number of epoch')
    plt.legend()
    plt.savefig(path)


def plot_loss_vs_iterations(losses, path='loss.png'):
    plt.figure()
    plt.plot(np.array(losses))
    plt.title('Loss vs. iterations')
    plt.ylabel('Loss')
    plt.xlabel('Number of iterations')
    plt.savefig(path)


def save_checkpoint(state, is_best, file_dir='checkpoints', file_name='checkpoint.tar'):
    torch.save(state, os.path.join(file_dir, file_name))
    if is_best:
        shutil.copyfile(os.path.join(file_dir, file_name), os.path.join(file_dir, 'model_best.tar'))


def load_images(train_root, test_root, train_transform, test_transform):
    '''train_root and test_root are strs'''
    print('Loading images...')
    train_data = datasets.ImageFolder(root=train_root, transform=train_transform)
    test_data = datasets.ImageFolder(root=test_root, transform=test_transform)
    print('Train data length:', len(train_data))
    print('Validate data length:', len(test_data))
    return train_data, test_data


def main():
    root = 'gender-data'
    checkpoint_path = os.path.join('checkpoints', 'gender')
    if args.age:
        print('Run Age Classifier ...')
        root = 'age-data'
        checkpoint_path = os.path.join('checkpoints', 'age')
    else:
        print('Run Gender Classifier ...')

    print('checkpoints will be stored in', checkpoint_path)
    if not os.path.exists(checkpoint_path):
        os.mkdir(checkpoint_path)

    train_accs = []
    val_accs = []
    epoches = []
    losses = []
    learning_rate = 0.001
    best_val_acc = 0.0
    batch_size = args.batch_size
    num_epochs = args.epoch

    train_transform = transforms.Compose(
        [transforms.Resize(256),
         transforms.RandomCrop(227),
         transforms.RandomHorizontalFlip(),
         transforms.ToTensor()])

    test_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(227),
        transforms.ToTensor()])

    train_data_path = os.path.join(root, 'train')
    test_data_path = os.path.join(root, 'test')
    train_data, test_data = load_images(train_data_path, test_data_path, train_transform, test_transform)

    train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True, num_workers=4)
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=False, num_workers=4)

    model = Net()
    criterion = nn.CrossEntropyLoss()

    for epoch in range(num_epochs):
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
        if args.sgd:
            optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)
            print('use SGD optimizer')
        else:
            print('use Adam optimizer')
        print('Starting epoch %d / %d' % (epoch + 1, num_epochs))
        print('Learning Rate: {}'.format(learning_rate))

        for i, (images, labels) in enumerate(train_loader):
            images = Variable(images)
            labels = Variable(labels)
            pred_labels = model(images)
            loss = criterion(pred_labels, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            losses.append(loss.data.item())
            print('Epoch [%d/%d], Iter [%d/%d] Loss: %.4f'
                  % (epoch + 1, num_epochs, i + 1, math.ceil(len(train_data) / batch_size), loss.data.item()))

        if (epoch + 1) % 5 == 0:
            learning_rate = learning_rate * 0.9
            print('update learning rate:', learning_rate)

        if (epoch + 1) % 5 == 0 or epoch + 1 == num_epochs:
            train_acc = check_acc(model, train_loader)
            train_accs.append(train_acc)
            print('Train accuracy for epoch {}: {} '.format(epoch + 1, train_acc))

            val_acc = check_acc(model, test_loader)
            val_accs.append(val_acc)
            print('Validation accuracy for epoch {} : {} '.format(epoch + 1, val_acc))

            epoches.append(epoch + 1)

            is_best = (val_acc > best_val_acc)
            best_val_acc = max(val_acc, best_val_acc)
            save_checkpoint(
                {'epoch': epoch + 1,
                 'model_state_dict': model.state_dict(),
                 'best_val_acc': best_val_acc,
                 'optimizer': optimizer.state_dict()}, is_best, file_dir=checkpoint_path,
                file_name='checkpoint' + str(epoch + 1) + '.tar')

    plot_performance(epoches, train_accs, val_accs, path=os.path.join(checkpoint_path, 'performance.png'))
    plot_loss_vs_iterations(losses, path=os.path.join(checkpoint_path, 'loss.png'))


if __name__ == '__main__':
    main()
