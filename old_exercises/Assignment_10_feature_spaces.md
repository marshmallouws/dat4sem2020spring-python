# Feature spaces
### Exercise 1: 

https://www.kaggle.com/PromptCloudHQ/imdb-data
- [PREDICTING MOVIE REVENUE (IMDB)](https://www.kaggle.com/PromptCloudHQ/imdb-data)


- Given a data set of the 1,000 most popular movies on IMDB in the last 10 years, can you predict the revenue of a given movie?
- Create a user for kaggle if not already done.

### Questions/Exercises:

**1.** Download the data programatically with python. 

(**Hint:** To generate your own kaggle.json file go to *your profile* -> *account* -> *Create new API Token*, and then place the file it in ~/.kaggle/)

<hr/>

You will now have to make a train-test-split of the data so that you have a way of verifying the model later. (We suggest 2/3 for training and 1/3 for testing)
	
Here is a link to the [train-test-split documentation for sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

**2.** Fit the training-data into a model, present it visually and reflect on wether it is a good fit or not.

<hr/>

**3.** Now take the test-data, test the model and evaluate how accurate the model is.


<br>

### Review Questions:
1. Was the data downloaded programatically with python?
2. Was the training-data fitted into the model, presented visually and reflected on?
3. Was the model tested with the training data, and was the accuracy of the model evaluated?

### Exercise 2: 

https://www.kaggle.com/spscientist/students-performance-in-exams/version/1	
- Download the data programatically with python.	
- Fit the data for the different scores in math, writing and reading into a model. 
- present it visually and explain what you see.	Predict the next semesters scores.	

#### review questions
- Was the data downloaded programatically with python?	
- Was the data fitted into the model, presented visually and as the data explained in a  good way?	
- was the scores for the next semester predicted.

### Exercise 3: 
https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016	
- Download the data programmatically	Plot amount of suicides/100k pop per year with an age group and gender of your choice	
- Make a prediction for a higher GDP per capita, and a lower GDP per capita. 
- Is there a correlation between amount of suicides per 100k pop and having a higher or lower gdp?	Was the data programmed programmatically? 

#### review questions
- Do you have any improvements?	
Was the data plotted in a meaningful way?	
- Was a prediction made? Was a valid conclusion made of the prediction?

### Exercise 4

https://think.cs.vt.edu/corgis/csv/cars/cars.html

#### Download the data

- Programatically download the data from the above link.
- Import the data into a Pandas dataframe.
- Show the head of the Pandas dataframe.

#### Linear regression

- Perform linear regression on the downloaded dataset, where `y=Highway mpg` and `x=Horsepower`.
- What is the coefficient (slope) of your model? What does this number mean?
- According to your model, what is `y` when `x=2000`.
- Show the regression line on a scatterplot with the other datapoints.

#### Classification

- Using `sklearn` create a classifier that can predict the make of a car, based on provided features. The following features should be included:
  - `City mpg`
  - `Highway mpg`
  - `Height`
  - `Width`
  - `Length`
  - `Horsepower`
  - `Year`
- Show the decisiontree of your model.
- Use your model to predict the make of a car.

## Review questions 

1. Did the student programatically download and import the data?
2. Did the student correctly display the regression line in a graph`?
3. Did the student find the coefficient of the line, and reflect on its meaning?
4. Did the student correctly provide their classification model with imported data?

### Exercise 5
https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009	

- Download the data programatically	
Find all wines with a high score(you decide what a high score is) and make a visual representation of their content.	
- Find out if there is a context, link, between the percentage of alcohol and the score of the wine. 
- (Optional) which percentage of alcohol has the highest average score?	

#### review questions
Was the data downloaded programatically?	
- Was the data visualized properly, and in a readable way? Were all wine contents included in the visualization?	
- Was the result well documented and/or visualized? (Optional) 
- was the alcohol percentage with the highest average score found?

### Exercise 6 

###¤ Part 1

1. Download the file `ExtractedTweets.csv`programmatically from this website: https://www.kaggle.com/kapastor/democratvsrepublicantweets#ExtractedTweets.csv

#### Part 2

1. Find the word distribution for each party using `CountVectorizer`
  * Make a histogram of the top 10 most used words for each party
2. Find the total word distribution using `CountVectorizer`
  * Plot a histogram of the top 10 most used words in total

### Part 3

1. Plot the number of tweets over time, so that time is on the x-axis and number of tweets is on the y-axis.
2. Find the biggest peak in tweets and find out what they were tweeting about: is there a big event that made everyone push a tweet? Hand-in a description of what happened and a link to a larger news site (BBC/CNN/Times/etc.)

## Review Questions

- Is the data correctly and automatically downloaded?
- Is the `CountVectorizer` used correctly?
- Are the histogram correctly made and do they have labelled axes?
- Are the tweets correctly counted over time?
- Does the plot correctly show the tweet count over time and does it include axes labels?

### Exercise 7
https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009	
- Download the data programatically	
Make a bar plot where the x-axis is the quality and the y-axis is the number of wines with the given quality	
- Use machine learning to determine the quality of the given wine parameters: Fixed acidity: 7.9, volatile acidity: 0.35, citric acid: 0.46, residual sugar: 3.6, chlorides: 0.078, free sulfur dioxide: 15.0, total sulfur dioxide: 37.0, density: 0.9973, pH: 3.35, sulphates: 0.86, alcohol: 12.8	

#### Review questions
- Was the data downloaded programatically?	
- Was the data visualized with a bar plot?	
- Was the quality calculated by machine learning and was it found to be around 8?


### Exercise 8
[Currency Exchange Rates](https://www.kaggle.com/thebasss/currency-exchange-rates)

## Questions

**1.** Download the data programatically with python. 
(**Hint:** To generate your own kaggle.json file go to *your profile* -> *account* -> *Create new API Token*, and then place the file it in ~/.kaggle/)
**2.** Plot the US Dollars compared to other currencies  
You decide how you wonna plot it - However, we expect that you can give an explanation as to why and how.
**3.** Try and predict the exchange rate for the US dollars the next X years!  
(**Hint:** *X* meaning you should make a modular method that takes years as an argument'
#### Review questions

**1.** Was the data downloaded programmticly with Python?
**2.** Was the data plottet in a meaningfull way? - Could it be improved? if yes how?
**3.** Was the exhange rate predicted? and does it seem reaonsable?

### Exercise 9
https://developer.github.com/v3/	
- List all (names) of your GitHub repositories	
- Sort the list by the repository size in descending order	
- Make a visualisation of all the languages you have used for all your projects	

#### Review questions
- was a list printed with all repositories?	
- Was the list sorted? Could it have been sorted more efficiently; if yes, then how?	
- Was the data visualised properly? How would you visualise the data?
