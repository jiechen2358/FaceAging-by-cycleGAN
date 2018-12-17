## FaceAging-by-cycleGAN
<span style="color:orange">This porject is still under construction... we will add more details in the progress.</span>
## Introduction
In this project, we proposed a simple, yet intuitive deep learning model based on CycleGAN [11] that can generate predictive images of faces after 30 years from the time it was taken, using a dataset with little requirements attached.

## Dataset
1. [**IMDB-WIKI-500k+ face images with age and gender labels**](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/) - contains 500k+ images of celebrities from IMDb and Wikipedia. The metadata of this dataset contains the date of birth of the person portrayed in the image and the date of which the image was taken.
2. [**Cross-Age Celebrity Dataset (CACD)**](http://bcsiriuschen.github.io/CARC/) - contains 163k+ images of 2,000 celebrities. "The images are collected from search engines using celebrity name and year (2004-2013) as keywords. We can therefore estimate the ages of the celebrities on the images by simply subtract the birth year from the year of which the photo was taken."

## Modeling and Implementation
We picked the [**CycleGAN**](https://junyanz.github.io/CycleGAN/) model because we think it can solve two major problems we face:  

1. Making sure the original image and the translated image represent the same person. Adversarial losses alone cannot guarantee that the learned function can map an individual input to a desired output. CycleGan regularizes the space of possible mapping by adding the cycle-consistency losses. Combining this loss with the adversarial losses on the domains “young” and “old”, it made sure that the transformed images still represent the same person in the original images. 


2. Obtain photos of one person that were taken at different ages is challenging and expensive. Therefore, we need an algorithm that can pass around domain knowledges between groups without paired input-output examples. CycleGAN can capture characteristics of faces of young people portraited in one image collection and figure out how these characteristics can be applied to those facial images in a collection of old people.

![Model Architecture](https://raw.githubusercontent.com/jiechen2358/FaceAging-by-cycleGAN/master/imgs/CycelGANAgingModelArchitecture.png)

# Getting Started

## Installation
1. Clone this repo

       git clone https://github.com/jiechen2358/FaceAging-by-cycleGAN.git
       cd FaceAging-by-cycleGAN
   
2. Install PyTorch 0.4+ and torchvision from http://pytorch.org and other dependencies (e.g., visdom and dominate). You can install all the dependencies by
   
       pip install -r requirements.txt
   
3. For Conda users, we include a script ./scripts/conda_deps.sh to install PyTorch and other libraries.

## Train/Test
1. Unpack datasets:

       ./scripts/unzip_datasets.sh
   
2. Train a model: 

       python train.py --dataroot ./datasets/young2old --name aging_cyclegan --model cycle_gan
   
   To view training results and loss plots, run python -m visdom.server and click the URL http://localhost:8097. To see more intermediate results, check out ./checkpoints/aging_cyclegan/web/index.html.

3. Test the model:

       python test.py --dataroot ./datasets/young2old --name aging_cyclegan --model cycle_gan

   The test results will be saved to a html file here: ./results/aging_cyclegan/latest_test/index.html.

## Contribution
The code related to data processing is located in folder [**data_processing**](https://github.com/jiechen2358/FaceAging-by-cycleGAN/tree/master/data_processing), the folder contains utilities perform following  tasks
* image format validation
* remove grayscale images
* remove small size images
* process metadata of raw IMDB and CACD datasets.
* Logging

Added a script print_structure.py to print the network architecture based on the user selections.

The trained models are located in folder [**trained_model**](https://github.com/jiechen2358/FaceAging-by-cycleGAN/tree/master/models), including:
* wiki_all_female - checkpoints trained on female only datasets
* wiki_all_male - checkpoints trained on male only datasets
* wiki_mix_male_female - checkpoints trained on whole dataset with images of male and female combined.

Added options to perform transfer learning and fine-tuning. Those files are located in folder: [**options**](https://github.com/jiechen2358/FaceAging-by-cycleGAN/tree/master/options).

Implemented a [**Gender & Age Classifier**](https://github.com/jiechen2358/FaceAging-by-cycleGAN/tree/master/gender_age_classification) intent to perform multiple tasks.
* From application perspective, we plan to develope a model selection in the future since our experiments show that the results of our model are influenced by the gender of the input images. For example, model trained on female has better performance on female image inputs.

## Results
The following table lists all models we have explored in our study and their quantitative result. The columns are (from left to right): model number, data source, data composition, number of epochs trained, pre-trained network to initialize with, freeze until what layer of generator net, the size of the generator net, maximum age progression (years), average age progression, last 3 columns are the % of test cases where age progression is over 10 years, 15 years and 20 years. Results in model #4 is N/A due to model collapsing.

![Model Comparison: Transfer Learning, Fine Tuning](https://raw.githubusercontent.com/jiechen2358/FaceAging-by-cycleGAN/master/imgs/table-of-experiment-results.PNG)

              Young to Old                      Old to Young
![male young to old 1](https://raw.githubusercontent.com/jiechen2358/FaceAging-by-cycleGAN/master/imgs/m-result1.gif)
![male old to young 1](https://raw.githubusercontent.com/jiechen2358/FaceAging-by-cycleGAN/master/imgs/m-result2.gif)

                 Input                             Output                         reconstruction 
![Input output reconstruction](https://github.com/jiechen2358/FaceAging-by-cycleGAN/blob/master/imgs/Picture1.png)

## Report
[**AgingGAN: Age Progression with CycleGAN**](https://github.com/jiechen2358/FaceAging-by-cycleGAN)

## References
* CycleGAN paper [link](https://arxiv.org/abs/1703.10593)
* Official source code pyTorch implementation [link](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) 
