# Storytelling Presentation for American Flights Data (R)

## Project Overview
Analyzed the 2008 American Airlines dataset and self-developed an interesting topic for storytelling and presentation purpose. The presentation was oriented towards the general public to share my storyline and findings.

Idea: since flights can be delayed by weather, but it is hard to tell which airports are responsible for those delays if just by simply looking at the flight information. That is, were the extreme weather conditions occuring at the destination airports or at the departure airports? To answer this, a data analysis has been conduted in R and visualization plots were also made to give the auidence an intuition of where were the bad weathers occuring on a given date.

Furthermore, a shiny app was developed for a more versatile demonstration purpose. Here is also a [short explanation for the sample outputs from shiny app](https://github.com/qyzqyz1/Data-Science-Portfolio/tree/master/R%20Projects/R%20-%20Data%20Analysis%20and%20Visualization/Storytelling%20(R%20Shiny)%20-%20Air%20Flights%20Data/shiny%20outputs).

## File Descriptions
- **data_sets**: contains summary datasets for the American flights and airports information in the year 2008, while the complete *air.csv* file was used in the analysis and can be [downloaded here](http://rtricks4kids.ok.ubc.ca/wjbraun/DS550/air.csv). **Note**: this is a huge dataset (755MB, 7001975rows x 29cols) and will take a few minutes to download
- **shiny**: contains a shiny app made for displaying two plots:
    - A map plot showing the weather delay conditions vs. airports on a user defined date
    - A barplot showingt the top outstanding weather-delayed airports in a specified month
    
    *_Note_*: in order to use the shiny app, you will need to download the *air.csv* file first, and place that file to your current R working directory.
- **shiny outputs**: contains sample outputs from the shiny app
- **Presentation Slides.pdf**: presentation slides in pdf format that is used for storytelling my findings
- **Storytelling.r**: data analysis R scripts in .R format
- **Storytelling.ipynb**: data analysis R scripts in .ipynb format

## Package Requirements
To successfully run the R script, you need to first install the following packages in R by running `install.packages("package_name")`:
- **rworldmap** package: Enables mapping of country level and gridded user datasets.

## Practiced Skills
- R-Shiny
- Storytelling/Presentation
- Data Visualization
- Data Cleaning
- Data Manipulation
