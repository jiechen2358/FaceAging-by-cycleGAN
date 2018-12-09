import models.networks as net

# image channels
input_nc_a, input_nc_b = 3, 3
output_nc_a, output_nc_b = 3, 3

# number of gen filters in first conv layer
ngf_a, ngf_b = 64, 64
# number of discrim filters in first conv layer
ndf_a, ndf_b = 64, 64

# generator: 'resnet_9blocks', 'resnet_6blocks', 'unet_128', 'unet_256'
netG_a, netG_b = 'resnet_9blocks', 'resnet_9blocks'

# discriminator: 'basic', 'n_layers', 'pixel'
netD_a, netD_b = 'basic', 'basic'

netG_A = net.define_G(input_nc_a, output_nc_a, ngf_a, netG_a)
netG_B = net.define_G(input_nc_b, output_nc_b, ngf_b, netG_b)

netD_A = net.define_D(output_nc_a, ndf_a, netD_a)
netD_B = net.define_D(output_nc_b, ndf_b, netD_b)

with open('net_structure.txt', 'w') as outfile:
    print('############ Generator A ############', file=outfile)
    print(netG_A, file = outfile, end = '\n\n\n')
    print('############ Generator B ############', file=outfile)
    print(netG_B, file = outfile, end = '\n\n\n')
    print('############ Discriminator A ############', file=outfile)
    print(netD_A, file = outfile, end = '\n\n\n')
    print('############ Discriminator B ############', file=outfile)
    print(netD_B, file = outfile, end = '\n\n\n')