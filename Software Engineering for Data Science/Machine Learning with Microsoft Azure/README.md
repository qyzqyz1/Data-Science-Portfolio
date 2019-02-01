# Building a Predictive Model with Microsoft Azure

## Project Description
A predictive model was built on the 2016-17 NBA Player Status Data Set ([link](https://www.basketball-reference.com/leagues/NBA_2017_advanced.html)) on Azure. In order to get the best results out of my experiment, I first prepared and cleaned the data using some of the built-in modules of Azure ML, and then compared the performances of two different machine learning alogrithms on my training data set. Based upon my trained model, a predictive experiment was further conducted for future predictions.

## Main Steps Followed:
1. **Importing Data set**
2. **Join Data Frames**: join data frames on their common characteristics
3. **Preprocess Text**: remove player names with special characters
4. **Edit Metadata**: replaced acronym column names with the more descriptive ones
5. **Apply SQL Transformation**: Use SQL statement to avoid duplicates and keep things simple, by assigning the clean value of the player name to the Player column, and also deleting all the header rows that we can find between data rows
6. **Edit Metadata**: make sure columns with numeric values are in integer or floating point types
7. **Clean Missing Data**: replaced missing values with the mean value in their columns
8. **Select Columns in Data set**
9. **Clip Values**: clip the values for the feature I want to predict (in this case, the PER - Player Efficiency Rating)
10. **Split Data**: split the data into training and testing sets
11. **Train Model**: trained the model using two different algorithms (linear & neural network) at the same time to compare them
12. **Score Model**: evaluate the each of the trained model by scoring them with the testing dataset
13. **Evaluate Model**: gain more empirical insights about the performance of the model and visualize the performance reports
14. **Predictive Experiment**: use the trained model to build predictive experiment for future predictions

## Links to Azure AI Gallery
The training model experiment can be viewed on my Azure AI Gallery [here](https://gallery.azure.ai/Experiment/Machine-Learning-Model-NBA-Data-Set), while the predictive model experiment can be viewed [there](https://gallery.cortanaintelligence.com/Experiment/Predictive-Model-NBA-Data-Set)

