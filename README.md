# FaceAging-by-cycleGAN
<span style="color:orange">This porject is still under construction... we will add more details in the progress.</span>
## Introduction
In this project, we proposed a simple, yet intuitive deep learning model based on CycleGAN [11] that can generate predictive images of faces after 30 years from the time it was taken, using a dataset with little requirements attached.

## Dataset
1. [**IMDB-WIKI-500k+ face images with age and gender labels**](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/) - contains 500k+ images of celebrities from IMDb and Wikipedia. The metadata of this dataset contains the date of birth of the person portrayed in the image and the date of which the image was taken.
2. [**CelebFaces Atributes (CeleA)**](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/) - contains 200k+ images of celebrities from IMDb. The metadata of it contains an attribute called “young”, and there are 46k+ images has the value “-1” for this attribute.

## Modeling and Implementation
We picked the [**CycleGAN**](https://junyanz.github.io/CycleGAN/) model because we think it can solve two major problems we face:  

1. Making sure the original image and the translated image represent the same person. Adversarial losses alone cannot guarantee that the learned function can map an individual input to a desired output. CycleGan regularizes the space of possible mapping by adding the cycle-consistency losses. Combining this loss with the adversarial losses on the domains “young” and “old”, it made sure that the transformed images still represent the same person in the original images. 


2. Obtain photos of one person that were taken at different ages is challenging and expensive. Therefore, we need an algorithm that can pass around domain knowledges between groups without paired input-output examples. CycleGAN can capture characteristics of faces of young people portraited in one image collection and figure out how these characteristics can be applied to those facial images in a collection of old people.

![Model Architecture](
        https://raw.githubusercontent.com/JunwenBu/ImageResources/master/CycelGANAgingModelArchitecture.png "Model Architecture"
      )

## Training


## Notes


## References
* CycleGAN paper [link](https://arxiv.org/abs/1703.10593)
* Official source code pyTorch implementation [link](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) 
