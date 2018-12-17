## Model Architecture
![Generator-ResNet-Discriminator](https://raw.githubusercontent.com/jiechen2358/FaceAging-by-cycleGAN/master/imgs/Generator-ResNetBlock-Discriminator.PNG)

## Base Network Detail
Our base model followed following layers architecture. By using different options, you can use other structure:
> **Supported models for generator**: 'resnet_9blocks', 'resnet_6blocks', 'unet_128', 'unet_256'

> **Supported models for discriminator**: 'basic', 'n_layers', 'pixel'

### Generator
* Encoder
>1 Conv(7x7)-BatchNorm-ReLU layer with stride 1
>2 Conv(3x3)-BatchNorm-ReLU layers with stride 2

* Transformer (ResNet-9)
>9 residual blocks

>Each block follows the structure of Conv(3x3)-BatchNorm-ReLU-Conv(3x3)-BatchNorm residual connection structure.

* Decoder
>2 fraction-strided-Conv(3x3)-BatchNorm-ReLU layer with stride ½

>1 Conv(7x7)-tanh layer with stride 1. 

### Discriminator
The discriminator is simply a convolutional network contains 5 downsampling layers.
