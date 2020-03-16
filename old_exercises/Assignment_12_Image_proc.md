# Image processing

### Exercise 1

1. From [Data](https://unsplash.com/search/photos/jeep) use selenium to download all images of jeeps
2. Use OpenCV to reduce the amount of colors in the images
3. Use OpenCV to find corners [Help](https://docs.opencv.org/master/d8/dd8/tutorial_good_features_to_track.html)
4. (EXTRA) Find all the wheels

### Exercise 2
https://unsplash.com/search/photos/basketball

1. Download all the images from the given link
2. Reduce the amount of colors in the images
3. Find all images with a basketball

### Exercise 3

This assignment is based on the tutorial found here: https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/

- Remember to install opencv: `conda install -c menpo opencv`
- A useful practice is to install imutils, which is also used in the tutorial: `pip install imutils`
- Please use the image primary-shapes.jpg included in this repo.

#### Questions
- Display the image and print width, height and depth of the image.
- Resize the image. The imutils package is useful for this.
- Convert the image to greyscale, then show the edges found in the image.
Make a thresholding of the image, then use this thresholding for finding contours in the image.
- Loop over, and display a visualization of the original image where the contours are outlined.


### Exercise 4

https://unsplash.com/photos/4HG5hlhmZg8

- In this assignment you are going to make a photograph look like it was painted with the pointillism technique.
- There is a fine library to do this at https://github.com/matteo-ronchetti/Pointillism but you still have to use OpenCV to read the image and get the colors.

#### Part 1
1. Download the picture and read it in the program.
2. Show the picture in the notbook using `OpenCv` and `matplotlib`

#### Part 2
1. Find the 20 most dominant colors. You will use them later to "paint" the picture.
2. Show the colors in the notebook.

#### Part 3
1. Use `pointillism` to create the painting.
2. Show the painting in the notebook.

## Exercise 5
Find a picture of your preference	
1. Download a picture programmatically 
2. Make a numpy-array of all the pixelcolors. 
3. Inverse all the colorvalues, so that the image becomes a "negative image"

### Exercise 6

Count the number of corners in a black and white figure.

* [Triangle](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4Tf0_mwmTo7d_AyFGP_TAgkZF_huAfIDNcgKF0WHqvrg5ewyx)
* [Square](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRif8vMomA-yAO8tr4WIcdr6YJbyMRlonXNJGlN5eqfe0kgQ0NM)
* [Pentagon](https://dejpknyizje2n.cloudfront.net/svgcustom/clipart/preview/pentagon-shape-2628-13890-300x300.png)

#### Count

- Create a python script that can count the number of corners in a figure, when provided the filename to the image. The filename should be provided as a command-argument.

- Extra points for using [argparse](https://docs.python.org/2/library/argparse.html).

The number of corners should be written to stdout.

#### Mark

- Create a new python script that can mark the corners in a figure, when provided the filename to the image. The script should also be provided a destination to the output image.

- Mark the detected corners with a red dot.

- Save the image to the provided destination path.
