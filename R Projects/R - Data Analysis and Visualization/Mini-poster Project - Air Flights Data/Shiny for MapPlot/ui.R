ui <- shinyUI(pageWithSidebar(
  headerPanel("Fig2: Customized Delay Situations"),
  sidebarPanel(
    textInput("lower_delay", "Enter the lower delay: ", "500"),
    textInput("upper_delay", "Enter the upper delay:", "600"),
    textInput("mini_delay", "Enter the minimum delay:", "300"),
    textInput("title", "Enter the chart title here:", "Fig2: Customized Delay Situations")
  ),
  mainPanel(
    plotOutput(outputId='main_plot')
)
)
)



