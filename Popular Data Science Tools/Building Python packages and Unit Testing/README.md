# Unit Testing and Travis CI

## Project Description
#### 1. Building python package
  In this project, I worked collatively with another group member - Jimmy Ding to develop a customized Python Package. The package we chose to build is the areaCalculator package which it is used to calculate the areas for various common shapes based on user inputs. More deatailed information regarding this package can be found inside the [areaCalculator](https://github.com/qyzqyz1/Data-Science-Portfolio/tree/master/Software%20Engineering%20Projects/Building%20Python%20packages%20and%20Unit%20Testing/areaCalculator) folder.

#### 2. Unit Testing
  After the package was built, five unit testing classes were created to validate the performance of our package. Those test classes were then collected by a test suit and the test suit was checked to ensure it can call the test classes properly.

#### 3. Try-Except as Exception Handlers
  In the last step, we integrated try-except syntax into our unit testing classes developed earlier to handle errors and exceptions gracefully. The codes are checked with coverage report to ensure maximum coverage (100%) is achieved. 

#### 4. Travis CI
  Continuous Integration testing is also setup using Travis and below is a status image showing the status of our build.

## Travis Status:
[![Build Status](https://travis-ci.org/qyzqyz1/DATA-533-lab-4-Tom-Jimmy-.svg?branch=jimmy)](https://travis-ci.org/qyzqyz1/DATA-533-lab-4-Tom-Jimmy-)

## File Descriptions
- **Coverage_Report**: contains screen shots showing that 100% coverage has been achieved for our testing codes
- **areaCalculator**: contains python package codes for calculating areas of various shapes based on user inputs
- **Other files in the main folder**: individual python package files from the areaCalculator folder. They are placed here to be accessible by Travis CI. 

## Practiced Skills:
- Building python package (with subpackages and inheritance structure)
- Creating unit testing classes
- Integrating try-except statements into unit testing
- Checking coverage reports
- Continuous Integration on Travis
