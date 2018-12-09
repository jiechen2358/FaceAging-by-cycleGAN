rm -r datasets/young2old/trainA
rm -r datasets/young2old/trainB
rm -r datasets/young2old/testA
rm -r datasets/young2old/testB
tar zxvf datasets/young2old/trainA_men.tar.gz -C datasets/young2old/
tar zxvf datasets/young2old/trainB_men.tar.gz -C datasets/young2old/
tar zxvf datasets/young2old/testA_men.tar.gz -C datasets/young2old/
tar zxvf datasets/young2old/testB_men.tar.gz -C datasets/young2old/
tar zxvf datasets/young2old/trainA_women.tar.gz -C datasets/young2old/
tar zxvf datasets/young2old/trainB_women.tar.gz -C datasets/young2old/
tar zxvf datasets/young2old/testA_women.tar.gz -C datasets/young2old/
tar zxvf datasets/young2old/testB_women.tar.gz -C datasets/young2old/
mkdir datasets/young2old/trainA
mkdir datasets/young2old/trainB
mkdir datasets/young2old/testA
mkdir datasets/young2old/testB
mv datasets/young2old/trainA_men/* datasets/young2old/trainA/
mv datasets/young2old/trainB_men/* datasets/young2old/trainB/
mv datasets/young2old/testA_men/* datasets/young2old/testA/
mv datasets/young2old/testB_men/* datasets/young2old/testB/
mv datasets/young2old/trainA_women/* datasets/young2old/trainA/
mv datasets/young2old/trainB_women/* datasets/young2old/trainB/
mv datasets/young2old/testA_women/* datasets/young2old/testA/
mv datasets/young2old/testB_women/* datasets/young2old/testB/
rm -r datasets/young2old/trainA_men
rm -r datasets/young2old/trainB_men
rm -r datasets/young2old/testA_men
rm -r datasets/young2old/testB_men
rm -r datasets/young2old/trainA_women
rm -r datasets/young2old/trainB_women
rm -r datasets/young2old/testA_women
rm -r datasets/young2old/testB_women
