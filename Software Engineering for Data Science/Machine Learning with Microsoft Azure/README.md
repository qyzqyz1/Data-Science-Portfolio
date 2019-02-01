# Building a Predictive Model with Microsoft Azure

## Project Description
A predictive model was built on the [2016-17 NBA Player Status Dataset](https://www.basketball-reference.com/leagues/NBA_2017_advanced.html) on Azure. In order to get the best results out of my experiment, I first prepared and cleaned the data using some of the built-in modules of Azure ML, and then compared the performances of two different machine learning alogrithms on my training data set. Based upon my trained model, a predictive experiment was further conducted for future predictions.

## Link to Azure AI Gallery
The machine learning experiments I have created can be viewed on my Azure AI Gallery: 
- [Training model experiment](https://gallery.azure.ai/Experiment/Machine-Learning-Model-NBA-Data-Set)
- [Predictive model experiment](https://gallery.cortanaintelligence.com/Experiment/Predictive-Model-NBA-Data-Set)

## Main Steps:
- **_Import Data set_**
- **_Join Data Frames_**: join data frames on their common characteristics
- **_Preprocess Text_**: remove player names with special characters
- **_Edit Metadata_**: replace acronym column names with the more descriptive ones
- **_Apply SQL Transformation_**: Use SQL statement to avoid duplicates and keep things simple, by assigning the clean value of the player name to the Player column, and also deleting all the header rows that we can find between data rows
- **_Edit Metadata_**: make sure columns with numeric values are in integer or floating point types
- **_Clean Missing Data_**: replace missing values with the mean value in their columns
- **_Select Columns in Data set_**: select the features of interest
- **_Clip Values_**: clip the values for the feature I want to predict (in this case, the PER - Player Efficiency Rating)
- **_Split Data_**: split the data into training and testing sets
- **_Train Model_**: train the model using two different algorithms (linear & neural network) at the same time to compare them
- **_Score Model_**: evaluate the each of the trained model by scoring them with the testing dataset
- **_Evaluate Model_**: gain more empirical insights about the performance of the model and visualize the performance reports
- **_Predictive Experiment_**: use the trained model to build predictive experiment for future predictions

## Practiced Skills:
- Microsoft Azure Machine Learning Studio
- Data Cleaning
- Data Manipulation
- Building Machine Learning Model

