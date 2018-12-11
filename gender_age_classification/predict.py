import argparse

import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import os

from gender_age_classifier import Net

parser = argparse.ArgumentParser(description='option for gender age classifier')
parser.add_argument('-a', '--age', action='store_true', help='switch classifier to age')
parser.add_argument('--sgd', action='store_true', help='use SGD optimizer')
# parser.add_argument('--test_folder', type=str, required=True, help='test images folder')
args = parser.parse_args()


def main():
    checkpoint_path = os.path.join('checkpoints', 'gender')
    classes = ('female', 'male')
    root = 'gender-data'
    if args.age:
        print('Use Age Classifier ...')
        classes = ('old', 'young')
        root = 'age-data'
        checkpoint_path = os.path.join('checkpoints', 'age')
    else:
        print('Use Gender Classifier ...')

    model = Net()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    if args.sgd:
        optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
        print('use SGD optimizer')
    else:
        print('use Adam optimizer')

    checkpoint = torch.load(os.path.join(checkpoint_path, 'model_best.tar'))
    model.load_state_dict(checkpoint['model_state_dict'])
    epoch = checkpoint['epoch']
    optimizer.load_state_dict(checkpoint['optimizer'])

    model.eval()

    test_transform = transforms.Compose(
        [transforms.Resize(256),
         transforms.CenterCrop(227),
         transforms.ToTensor()])

    # test_data = datasets.ImageFolder(root=args.test_folder, transform=test_transform)
    test_data = datasets.ImageFolder(root=os.path.join(root, 'predict'), transform=test_transform)
    batch_size = len(test_data)
    print('Test data length:', len(test_data))
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=False, num_workers=4)

    dataiter = iter(test_loader)
    images, _ = dataiter.next()

    outputs = model(images)
    _, predicted = torch.max(outputs, 1)
    print('##Predicted: ', ' '.join('%5s' % classes[predicted[j]] for j in range(batch_size)))


if __name__ == '__main__':
    main()
