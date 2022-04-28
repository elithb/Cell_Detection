# Cell_Detection

This repository is for our Master 1 Project : Absolute cell quantification from phasecontraste microscopy images

We decided to explore two solutions :
* YOLOv5 from https://github.com/ultralytics/yolov5
* Fiji from https://imagej.net/software/fiji/

We need to quantify the cells on images like this :
![exemple](https://user-images.githubusercontent.com/71750909/164416508-9a5814de-7389-4406-82e7-7c3a833b027c.png)

### The YOLOv5 Architecture

This solution isn't working for two main reasons :
* Some cells are detected several times (Can be resolved with the parameters of detect.py)

![image](https://user-images.githubusercontent.com/71750909/165713013-69e9e480-fad5-4bb4-9167-52c75f562a99.png)

* Insufficient detection in images with a large number of cells 

![image](https://user-images.githubusercontent.com/71750909/165713113-1b1acaa3-52a4-4e1a-a0f9-4e9b35a2a99c.png)


### The Fiji Software

A Fiji macro with 10% margin of error at most.
On Fiji, click on Plugins > Macros > Run and select the macro after opening the image to be analysed.

![image](https://user-images.githubusercontent.com/71750909/165713325-9f8f1256-bbd1-4f7a-9e97-fe8b04548361.png)

