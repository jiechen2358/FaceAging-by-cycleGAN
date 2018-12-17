# Background

This directory contains files that can be used to quantitatively estimate the performance of a AgingGAN model. In order to use any of the files in here, please first set up this repository [**Keras implementation of a CNN network for age and gender estimation**](https://github.com/yu4u/age-gender-estimation). Containing in this repository is a keras CNN network that can give estimation of the age of someone in the input image. We will use this network to do quantitative analysis for our model.

There are two estimation methods:

* age_diff_relative.py: Calculate the relative age difference of before and after AgingGAN. We first run the original image through the age estimation model and get age_before, then we run the age progressed image through the age estimation model and get age_after. The difference of these two values is how much "older" the AgingGAN made people look.

* age_diff_absolute.py: Calculate the age difference between generated image and ground truth. We only run the generated image through the age estimation model, then we subtract the ground truth age of the person in the photo (IMDB-WIKI dataset has metadata for this) from it, so we can get how much "older" the AgingGAN made people look.

In reality the first method performs better as it eradicated the bias of the Keras CNN model itself.

# To Use

1. Clone and setup this repo

       git clone https://github.com/yu4u/age-gender-estimation

2. Copy the estimator to the project root directory

3. Run following command

       python3 age_diff_relative.py --image_dir ../FaceAging-by-cycleGAN/results/9_wiki_fine_tune_male/test_latest/images/
       python3 age_diff_absolute.py --image_dir ../FaceAging-by-cycleGAN/results/9_wiki_fine_tune_male/test_latest/images/