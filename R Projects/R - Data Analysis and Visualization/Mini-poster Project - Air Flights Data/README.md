# Mini-Poster Project for American Flights Data (R)

## Project Overview
This repository contains code  and datasets for analyzing the delay situation associated with the American airlines in the year 2008. A specific focus was given to the U.S. Airway company, and four different types of charts were created to visualize the delay conditions with respect to months and airport locations. Furthermore, a shiny app was also made for the last map plot, which allows users to input their customized delay levels and visualize the flight routes correspond to that level and the output will change instantly as user modify their input values.

Furthermore, a mini-poster was created in pdf format to present our findings to the general public who would be interested to know some general insights about the delays occured for the U.S. Airway in 2008.

## File Descriptions
- **data_sets**: contains partial datasets for the American flights and airports information in the year 2008. The complete *air.csv* file can be downloaded from: http://rtricks4kids.ok.ubc.ca/wjbraun/DS550/air.csv
- **outputs**: contains four different types of baisc plots created through R
- **shiny**: contains a shiny app made for the map plot that allows output to change with user inputs. **Note**: in order to use the shiny app, you will need to download the *air.csv* file first, and place that file to your current R working directory.
- **Final_Poster.pdf**: mini-poster in pdf format that is used to present our findings
- **Miniposter.r**: R scripts in R format
- **Miniposter.ipynb**: R scripts in ipynb format

## Package Requirements
To successfully run the R script, you need to first install the following packages in R by running `install.packages("package_name")`:
- **plotrix** package: Contains lots of plots, various labeling, axis and color scaling functions.
- **rworldmap** package: Enables mapping of country level and gridded user datasets.

## Practiced Skills
- Data Cleaning
- Data Manipulation
- Data Visualization
- R-Shiny
- Storytelling