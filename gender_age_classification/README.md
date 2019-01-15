# Gender and Age Classification using CNN

Version: 0.9

## Introduction
Implement a simple "Gender and Age Classifier" in Pytorch. For the moment the Age Classifier only classify young and old. If you have prepared datasets of age group and put it correctly in the data folder, it should also work.

## Dataset
The dataset for training this model is pretty small, feel free to add more data if you plan to have a try.

* For Gender, 500 female images, 500 male images for train
* For Age, 543 young images, 515 old images for train
* Arround 100 images for test

For age classification, data locates in folder: age-data

For gender classification, data locates in folder: gender-data
* train folder includes data for training
* test folder includes data for testing
* predict folder is the data used by script "predict.py"

All the raw images are downloaded from [**IMDB-WIKI-500k+ face images with age and gender labels**](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/)

## Modeling and Implementation
The network model is similar with the description in this [paper](https://talhassner.github.io/home/projects/cnn_agegender/CVPR2015_CNN_AgeGenderEstimation.pdf).
Also see references.

## Installation
1. Clone this repo

       git clone https://github.com/jiechen2358/FaceAging-by-cycleGAN.git
       cd FaceAging-by-cycleGAN/gender_age_classification
   
2. Installation requirments should be the same as the mother project - "FaceAging-by-cycleGAN"

## Train
1. Train a model for gender classification:

       python gender_age_classifier.py 
   
2. Train a model for age classification:

       python gender_age_classifier.py -a
   
By default, the batch_size is 64, number of epoch is 100, can modify those values by using '-b' and '-ep'.

By defalut, it use Adam optimizer, can switch to SGD by using '-sgd'.

## Checkpoints and figures

   During training:
   
   Checkpoints and loss, performance figures for gender classifier will be generated and saved in folder: checkpoints/gender
   
   Checkpoints and loss, performance figures for age classifer will be generated and saved in folder: checkpoints/age

   The checkpoint with best validation accuracy will be copied as model_best.tar.

## Predict
   Please note: this is NOT a folder to test model performance, the purpose is to run it from application perspective (input an image and the model can predict).
   
   * There is no shuffle. A better approach will be implemented. Actually in Pytorch, it will label all the files in the first folder as the first label (in our case, female or old).
   * If you'd like to test the performance of the model. Images different from train/test folder should be used. The uploaded images are only some samples to test the predict script.
   
   It picks model_best.tar and load the model.

   For Gender, put images of male and female in folder gender-data/predict/someFolderName, run:
   
       python predict.py
   
   For Age, put images of old and young in folder age-data/predict/someFolderName, run:
   
       python predict.py -a
   

## Results

   Depends on your datasets.
   
   For attached dataset:
   * gender classifier accuracy > 95%
   * age classifier accuracy > 90%
   
## Notes
   * For Age classification, actually, there is some overfitting. For this very first version, it is fine. We will keep working on the project and keep improving the model and tune the hyper-parameters.
   * For Gender classifier, only trained on young male and female.
   * This classifier is in its "early verion" state. The code structure will be improved. More functions, options and comments will be added.

## References

Paper [CVPR2015_CNN_AgeGenderEstimation](https://talhassner.github.io/home/projects/cnn_agegender/CVPR2015_CNN_AgeGenderEstimation.pdf).

Pytorch tutorials [Classifier](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#sphx-glr-beginner-blitz-cifar10-tutorial-py)
