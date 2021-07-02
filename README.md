# CCFEBRAS-VolcanoAlgorithmAnalisys
This project is used for the needs of improvement of volcano eruption detection algorithm.

The idea:<br>
Input consists of 2 types of images.<br>Ones are just images of volcano:<br>
![Иллюстрация к проекту](https://github.com/aANAESTHESIAa/CCFEBRAS-VolcanoAlgorithmAnalisys/raw/master/KLYU2_20210224095601_21355477.jpg)<br>
And others are the result of volcano eruption detection algorithm where the field of eruption is highlighted:<br>
![Иллюстрация к проекту](https://github.com/aANAESTHESIAa/CCFEBRAS-VolcanoAlgorithmAnalisys/raw/master/KLYU2_20210224095601_21355477.png)<br>
As we can see, sometimes algorithm work improperly causing  partial highlighting of eruption activity as on picture above(the central one).<br>
<br>
Thus we need to understand, why the border was drawn this way. <br>
For this purpose was decided to process every pixel of incorrect highlighting and to print its Luminance on it like this:<br>
![Иллюстрация к проекту](https://github.com/aANAESTHESIAa/CCFEBRAS-VolcanoAlgorithmAnalisys/raw/master/result.png)<br>
Green labeled pixels are those, where the algorithm boundary was drawn.<br><br>

How-to-use:<br>
<b>Step 1:</b> Select the unmarked image.<br>
<b>Step 2:</b> Select the image with algorithm result. <b>Note:</b> It should be the same volcano shot. Check the name of selected files. Id should be the same.<br>
<b>Step 3:</b> The marked image is opened in standart graph editor. Move the cursor to the <b>UPPER LEFT</b> corner of desired processing area, thus the expecting anomaly hignlighting lies below and further to the right. The editor shows the coordinates of your cursor. Remember them. First one stands for X, second - for Y coordinate.<br>
<b>Step 4:</b> Close the picture editor.<br>
<b>Step 5:</b> Enter the coordinates as programm asks you to.<br>
<b>Step 6:</b> Select the form of the anomaly, horizontal ellipse, vertical ellipse or diaganolly placed ellipse.<br>
The program outputs the processed image area that you set to expect.
