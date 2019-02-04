ui <- fluidPage(
  titlePanel("Storytelling Presentations"),
  
  tabsetPanel(
    tabPanel("Plot1: Where Are the Bad Weahters",
    sidebarLayout(
    sidebarPanel(
    img(src = "flight_wd.jpg", height = 72, width = 220),
    helpText("Enter a day of interest to visualize the flights weather-delay situations 
    versus airports on that day"),
    selectInput("user_month", 
                label = "Select a month",
                choices = list(1,2,3,4,5,6,7,8,9,10,11,12),
                selected = 12),
    textInput("user_day", "Enter the day of month:", "25"),
    sliderInput("user_delays", label="Select a cutoff severe delay point",
                min = 80, max = 150, step = 1, value=90)
  ),
    mainPanel(
      plotOutput("main_plot")
    )
  )
  ),
  
    tabPanel("Plot2: Worst Airports for the Month",
    sidebarLayout(
    sidebarPanel(
    img(src = "worst.jpg", height = 72, width = 220),
    helpText("Select a particular month to visualize the top 8 most weather-delayed
             U.S. airports for the month"),
    sliderInput("user_month2", label="Select a month",
                min = 1, max = 12, step = 1, value=12)
    ),
    mainPanel(
      plotOutput("bar_plot")
    )
    )
    )
  )
  )










