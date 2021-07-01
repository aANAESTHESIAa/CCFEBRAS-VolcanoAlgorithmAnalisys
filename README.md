# CCFEBRAS-VolcanoAlgorithmAnalisys
This project is used for the needs of improvement of volcano eruption detection algorithm.

The idea:
Input consists of 2 types of images.
Ones are just images of volcano
![Иллюстрация к проекту](https://github.com/aANAESTHESIAa/CCFEBRAS-VolcanoAlgorithmAnalisys/raw/master/KLYU2_20210224095601_21355477.jpg)
And others are the result of volcano eruption detection algorithm where the field of eruption is supposed to be highlighted.
![Иллюстрация к проекту](https://github.com/aANAESTHESIAa/CCFEBRAS-VolcanoAlgorithmAnalisys/raw/master/KLYU2_20210224095601_21355477.png)
As we can see, sometimes algorithm work improperly causing  partial highlighting of eruption activity as on picture above(the central one).

Thus we need to understand, why the border was drawn this way. 
For this purpose was decided to process every pixel of incorrect highlighting and to print its Luminance on it like this:
![Иллюстрация к проекту](https://github.com/aANAESTHESIAa/CCFEBRAS-VolcanoAlgorithmAnalisys/raw/master/result.png)
Current version.

