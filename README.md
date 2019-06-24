# Low-Saturation-Image-Classifier
<br>
Use the K Means algorithm, one of the machine learning techniques, to classify whether the image has low saturation or not.
Set the value of k to 3 to extract the three colors representing the whole image. Then, compare the RGB values of the three colors. If the RGB values are similar, they are classified as a grayscale image.
<br><br><br>

## 1. Gray Factor

Gray Factor is the basis of comparison. Add the absolute values ​​of R-G, R-B and G-B in all three colors representing the image. There are 3 values ​​per color and 9 values ​​are output. When all these values ​​are added, if it is over 125, it is classified as a color image. If it is lower than 125, it is classified as a grayscale.
<br><br><br>

## 2. Test

## 2-1. Color Image

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990475-42aa1800-967e-11e9-93a9-8e32d5b528cf.jpg></img>
<br> grayfactor is 470.433684348195
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990477-4342ae80-967e-11e9-8491-184ededa2a64.jpg></img>
<br> grayfactor is 220.00078428233624
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990478-4342ae80-967e-11e9-99cd-37a3ab855188.jpg></img>
<br> grayfactor is 361.9403200650253
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990479-4342ae80-967e-11e9-8978-ffb537da597e.jpg></img>
<br> grayfactor is 394.7566669657726
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990480-4342ae80-967e-11e9-9f69-8c1f7b07bc1f.jpg></img>
<br> grayfactor is 657.9671760918529
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990481-43db4500-967e-11e9-968f-b927de583f0b.jpg></img>
<br> grayfactor is 206.07376379585685
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990482-43db4500-967e-11e9-903e-11251459caf9.jpg></img>
<br> grayfactor is 175.778811114855
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990483-43db4500-967e-11e9-9bc3-7f0461afcebf.jpg></img>
<br> grayfactor is 219.33294774865516
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990484-43db4500-967e-11e9-9096-fb5dedc5493e.jpg></img>
<br> grayfactor is 120.08708814516638
<br> this image is grayscale image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990485-4473db80-967e-11e9-8370-63901208b31e.jpg></img>
<br> grayfactor is 166.23216016614876
<br> this image is color image
<br><br><br>

## 2-2. Low Saturation Image

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990709-32466d00-967f-11e9-8f1e-6f51c857100c.jpg></img>
<br> grayfactor is 74.21911310513414
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990710-32df0380-967f-11e9-8030-c412d201aeff.jpg></img>
<br> grayfactor is 16.921373829598963
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990711-32df0380-967f-11e9-89c6-25e0d4e154dd.jpg></img>
<br> grayfactor is 74.8569993561774
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990712-32df0380-967f-11e9-8aaf-b5b707c56edb.jpg></img>
<br> grayfactor is 21.336244560550085
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990713-32df0380-967f-11e9-913f-2530dfc8768e.jpg></img>
<br> grayfactor is 39.46925756428328
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990715-33779a00-967f-11e9-939c-5a68fba98691.jpg></img>
<br> grayfactor is 83.9590711276494
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990716-33779a00-967f-11e9-81c0-194b424e3be0.jpg></img>
<br> grayfactor is 50.64524879463909
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990717-33779a00-967f-11e9-85b5-36499b40d85d.jpg></img>
<br> grayfactor is 29.222783415229628
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990718-33779a00-967f-11e9-8783-ab795236e50b.jpg></img>
<br> grayfactor is 44.29888605893774
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990719-34103080-967f-11e9-8cdd-476a6bec6a06.jpg></img>
<br> grayfactor is 30.120887800532955
<br> this image is color image
<br><br>

## 2-3. Test Accuracy

The test resulted in 19 images out of a total of 20 images. An accuracy of 95% indicates that this classifier works correctly.
<br>
<br>

