library(shiny)
library(leaflet)
library(htmltools)
library(plotly)

ui <- fluidPage(
  titlePanel("Storytelling - 2008 U.S. Airline Dataset"),
  
  tabsetPanel(
    tabPanel("Single Day - Weather Condition",
    sidebarLayout(
    sidebarPanel(
    img(src = "flight_wd.jpg", height = 72, width = 220),
    helpText("Select a date of interest to visualize the weather-delay situations 
    versus airport locations on that date."),
    dateInput("user_date", label = h4("Select a date of interest"), value = "2008-12-25",
              min="2008-01-01",max="2008-12-31"),
    sliderInput("user_delays", label=h4("Select a cutoff point for severe delay"),
                min = 60, max = 180, step = 1, value=120)
  ),
    mainPanel(
      h4("Where are the Bad Weathers",align = "center"),
      leafletOutput("main_plot"), 
      h4("Top 5 Airports with Worst Weather",align = "center"),
      dataTableOutput("table")
    )
  )
  ),
  
    tabPanel("Single Month - Weather Condition",
    sidebarLayout(
    sidebarPanel(
    img(src = "worst.jpg", height = 72, width = 220),
    helpText("Select a particular month to visualize the top weather-delayed
              airports or the change of delay conditions for that month"),
    selectInput("user_month2", label=h4("Select a month"),
                choices = list("January" = 1, "Feburary" = 2,
                              "March" = 3,"April" = 4,
                              "May" = 5,"June" = 6,
                              "July" = 7,"August" = 8,
                              "September" = 9,"October" = 10,
                              "November" = 11,"December" = 12), selected = 12),
    radioButtons("graph_choice", label=h4("Select a plot to display"),
                 choices = list("Top Weather-Delayed Airports" = 1, 
                                "Change in Delay Conditions (Animated)" = 2),
                                selected = 1)
    ),
    mainPanel(
      conditionalPanel(
        condition = "input.graph_choice == 1", 
        h4("Top 8 Weather-Delayed Airports for the Month", align='center'),
        plotOutput("bar_plot")),
      
      conditionalPanel(
        condition = "input.graph_choice == 2", 
        h4("Change of Mean Weather Delays for the Month", align='center'),
        plotlyOutput("plot"))
    )
    )
    )
  )
  )










