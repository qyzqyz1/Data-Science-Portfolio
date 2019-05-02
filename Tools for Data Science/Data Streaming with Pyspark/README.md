# Data Streaming with Spark

## Objective

1. Understand the concepts of Spark Live Streaming
2. Write Spark programs to perform operations on streaming data

## Instructions

1. For question 1, 3 and 4, create a new Python 3 Jupyter Notebook.
2. For question 2, use the `server_template.py` file. After making necessary changes, rename and save the file as `server.py`.

## Questions 1:
Run a Netcat server program on your local machine at port `9999`. 

1. Write a Spark program to read numbers that are sent from the Netcat server. Note that to check this program, you need to manually send integer numbers, separated with commas (e.g., `10, 40, -20`), from the Netcat server. The Spark program should split the received data based on commas and cast them to correct data type (i.e., integers).
2. Write a query that appends the data into a memory table. 
3. Write a SQL query to show all the data, in ascending order.

**Output:**

|numbers|
|-------|
|    -20|
|     10|
|     40|


4. Write another SQL query to show the minimum, maximum and average of the given numbers.


|minimum|maximum|average|
|-------|-------|-------|
|    -20|     40|     10|



## Question 2:
You are given with a sample code (check `server_template.py` file) that can be updated to create a Python server. Modify the file (rename and save the file as 'server.py') to:
1. Create a server so that it reads data from the comma-separated value (CSV) file called data1.csv. Note that you can use any Python packages/functions to reading the file. 
2. Send the data to a client program once the client is connected to the Python Server. Send a single line/row data at a time. Also, make necessary changes to the code so that the program wait for a fixed interval (e.g., 1 second) after sending a line to the client to simulate streaming.

Once you finish your code, check the program by running a Netcat client application. In the command prompt, you can use `nc64.exe localhost 9999` command to connect to the server program at port 9999. Once you are connected, the python program should send data to the client program.


## Question 3:
1. Write a Spark program to read the data that are sent from the python server that you created in question 2. The program should split the data based on comma and cast it to correct data type. Note that Each line of the data contains: PassengerId, Survived, Pclass, Name, Sex, Age, Fare. You will find more information about the fields here: https://www.kaggle.com/c/titanic/data. Print the schema of your datafrmae.

How to split and cast:
```
df.withColumn("PId", split(col("value"), ",").getItem(0).cast(IntegerType())) \
  .withColumn("Name", split(col("value"), ",").getItem(1).cast(IntegerType()))
  ``` 

 **Output:**
```
root
 |-- PassengerId: integer (nullable = true)
 |-- Survived: integer (nullable = true)
 |-- Pclass: string (nullable = true)
 |-- Name: string (nullable = true)
 |-- Sex: string (nullable = true)
 |-- Age: double (nullable = true)
 |-- Fare: double (nullable = true)
 ```

2. Write a query that appends the data into a memory table. 
3. Write a SQL query to show the percentage of passengers who survived. 
 
 **Sample Output:**

|       Percentage|
|-----------------|
|46.15384615384615|

4. Write a SQL query to show the number of passengers surviving under each gender category. When getting continuous data, did you see any pattern in the data?

**Sample Output:**

|   Sex| Survived |
|------|-------------|
|female|          141|
|  male|           56|

Trend: <2-3 sentences>

5. Write a SQL query to show the percentage of passengers who survived under each class category. Show the results in ascending order by `Pclass`.
 
**Sample Output:**

|Pclass|       Percentage|
|------|-----------------|
|     1|18.69158878504673|
|     2|18.69158878504673|
|     3|62.61682242990654|

## Question 4:

For this question, modify the server program so that it reads from `data2.txt` instead of `data1.csv` and send one line at a time with a given interval. Note that the `data2.txt` file contains Twitter users bio data. 

1. Write a Spark program to read the data that are sent from the python server. The program should split the data based on space.  
2. Create a new DataFrame that only contains the hashtag words (i.e., words that start with a #). 
3. Write a query that appends the table into memory. 
4. Write a SQL query to show the top 10 popular hashtag words with the number of time they were mentioned.

**Sample Output:**


|        Word|Count|
|------------|-----|
|     #Hiring|   27|
|       #Jobs|   24|
|        #Job|   22|
|  #CareerArc|   17|
|        #job|   10|
|     #Retail|    8|
|       #job?|    6|
|#Hospitality|    5|
|   #Veterans|    4|
|    #hiring!|    4|
