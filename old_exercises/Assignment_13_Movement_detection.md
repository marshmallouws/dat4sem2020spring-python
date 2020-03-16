# Movement Detection

### Exercise 1
Write a program that capture video from your webcam, that finds and marks faces and eyes

### Exercise 2
- Using OpenCV, Python and Template Matching to play “Where’s Waldo?”
- Take a look at the Where’s Waldo puzzle below. How long does it take you to find Waldo? 10 seconds? 30 seconds? Over a minute?

- Now lets use our recently acquired knowledge to complete this task much faster :)

- You should use [template matching](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html) to find waldo in the below scene.

##### The Scene
Use this image below as your scene  
![scene](https://i.imgur.com/8vEQ4rV.jpg)

##### Waldo
Use an image to find waldo in the scene (you should crop waldo out of the original picture yourself - He is located in the bottom left cornor! :))

### Exercise 3
https://streamable.com/pnv70	
- Detect the fishing bobber in the video	
- Resize the fishing bobber to be bigger	
- Display the new video in a new window	
- Detect shapes tutorial https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/

### Exercise 4

## Part 1

Use `cv2.VideoCapture` to capture the stream from your webcam.

[movement detection.py](https://github.com/datsoftlyngby/dat4sem2019spring-python-materials/blob/master/movement_detection.py)

## Part 2

Perform facedetection on the incoming frames. Mark the detected faces with a rectangle on the frame.

[Object recognition.py](https://github.com/datsoftlyngby/dat4sem2019spring-python-materials/blob/master/24-Object%20recognition.ipynb)

## Part 3

Output the stream into a window.

