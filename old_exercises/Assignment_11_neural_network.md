# Neural Networks

### Exercise 1
https://keras.io/datasets/	
- Firstly load the fashion_mnist dataset from keras.datasets. 
- Secondly define the training and testing data	
- Build the model and train (fit) it with training images and determine the test accuracy	
- Randomly select some testing images and classify them	

#### Review questions
- Was the dataset loaded properly? 
- Was the training and test data defined?
- Was the test accuracy determined?	
- Were all the selected images classified?

### Exercise 2 

https://github.com/PranayMalhotra/NBA-player-career-lengths/blob/master/nba_logreg.csv

Predict whether or not a player will play at least five years in the NBA, based on performance attributes.

![asd](https://data.world/api/exercises/dataset/logistic-regression-exercise-1/file/raw/Screen%20Shot%202017-01-25%20at%2010.20.38%20AM.png)

#### Part 1

1. Programatically download the raw csv data.
2. Import the data into a pandas dataframe.
3. Print the head of the dataset.

#### Part 2

1. Find the names of the top 10 3-point shooters (`3p_made`) in the dataset.
2. On a scatter plot, show the relationship between `x=GP` and `y=target_5yrs`.
3. Does the scatter plot show a relationship between the two attributes?

#### Part 3

1. Create a classifier that can predict whether or not a player will play for 5 years in the NBA.
2. Use your classifier, find examples where the result is both `0` and `1`.
3. Reflect on the importance of the `GP` attribute. Is it more or less important, than the other attributes.


## Review questions

1. Did the student correctly and programmatically download and import the csv data? Was the head of the data shown?
2. Did the student correctly display the scatter plot? Could anything be improved about the code in question?
3. Did the student reflect on the importance of the `GP` attribute. Do you have any comments about the reflection on the `GP` attribute?

### Exercise 3 


#### Part 1

1. Use `sklearn.datasets.load_wine` to load wine data
2. Show all target names
3. Show all feature names

Read the documentation for the dataset [here](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)

#### Part 2

1. Visualize the data (scatter) with Alcohol as x and Malic Acid as y
2. Comment on what you see

#### Part 3

1. Build a perceptron
2. Find and plot the line that slices the feature space
3. Comment on what you see

## Review Questions

- Was data loaded and target names and features shown correctly?
- Was the data visualized in a meaningful way?
- Does the explaination describe the visualization in an understandable way? If not why not?
- Was the perceptron correctly used to find the line slicing the feature space?
- Does the explaination describe the visualization in an understandable way? If not why not?

### Exercise 4

## Info
You are welcome to extract the data however you want.

4chan has a read-only API you can use to get the JSON of all threads and posts.
If you choose to use their API, the link is as follows: ```https://api.4chan.org/[board]/thread/[thread ID].json```

If you don't want to use their API, just use ```beautifulsoup``` instead.

## Questions

### Part 1
1. Find a thread with a fairly large amount of pictures and videos (25+)
2. Get the source from the page
3. Use ```beautifulsoup``` or the 4chan API to extract all links and original filenames for all picture and video files on the page
4. Show the links and filenames in the notebook

### Part 2
1. Create a folder with the subject or ID of the thread
2. Save all the files to that folder
3. Print a message every time a file has or hasn't been saved (so we can see something in the notebook)

### Part 3
1. Use ```argparse``` to create a script that takes arguments
2. Implement an argument for the thread URL
3. Implement an argument for the path to the directory where you want the folder with the saved files to be stored

## Review Questions

### Part 1
1. Was the source loaded and the links and filenames shown?

### Part 2
1. Was a folder named with the subject or ID of the thread created?
2. Was all the files downloaded and given their original filenames?

### Part 3
1. Does the script take the specified arguments+ Why/why not?


### Exercise 5
[Clothing assignment Data](https://www.kaggle.com/zalando-research/fashionmnist)

#### Using TesorFlow

- Given a revolutionary dataset of high-end fashion clothing items, can you create a groundbreaking neural network that can predict the unique categories of a given item?

### Questions/Exercises:
1. Download the dataset programatically, and split the data into a train-test set.
2. Using TensorFlow, create a neural network and train it.
3. Use the provided test data, and evaluate the accuracy of the network.

### Review Questions:
1. Did the student download the data programatically and split it into a train-test set?
2. Did the student use tesorflow to create a neural network and train it?
3. Did the student reflect on the accuracy of the network?



