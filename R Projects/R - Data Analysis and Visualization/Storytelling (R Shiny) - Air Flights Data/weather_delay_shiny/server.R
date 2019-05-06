library(shiny)
library(leaflet)
library(htmltools)
library(ggplot2)

air <- read.csv("air_new.csv")
source("airports.R")


server <-
function(input,output, session){
    # User input into the main program
    output$main_plot <- renderLeaflet({
      date <- as.character(input$user_date)
      day <- as.numeric(substr(date, start = 9, stop = 10))
      month <- as.numeric(substr(date, start = 6, stop = 7))
      cutoff_delays <- as.numeric(input$user_delays)
      map_title <- input$map_title
      
      df <- subset(air, Month==month)

      if (!is.null(day)){
        df <- subset(df, DayofMonth==day)
      }
      
      # Count total number of weather delays at each airport
      dest_count <- as.data.frame(table(df$Dest))
      origin_count <- as.data.frame(table(df$Origin))
      
      total_count <- merge(dest_count, origin_count, by="Var1")
      total_count$total <- total_count$Freq.x + total_count$Freq.y
      colnames(total_count) <- c("iata_code","dest_count","origin_count","total_delay_counts")
      new_airports <- merge(airports, total_count, by="iata_code")
      
      # Get the top 10 airports with the most number of weather delay flights
      top_10 <- head(new_airports[order(new_airports$total_delay_counts, decreasing = TRUE),], 10)
      
      collection <- c()
      i <- 1
      for(item in top_10$iata_code){
        collection[i] <- mean(subset(df, Dest==item|Origin==item)$WeatherDelay)
        i <- i+1
      }
      top_10_mean_delay <- as.matrix(collection)
      top_10_mean_delay <- as.data.frame(top_10_mean_delay)
      colnames(top_10_mean_delay) <- "mean_delay"
      top_10 <- cbind(top_10, top_10_mean_delay)
      
      top_5 <- head(top_10[order(top_10$mean_delay, decreasing = TRUE),], 5)
      top_5 <- top_5[c(1,2,3,4,10,11)]
      
      # Create a DataTable showing the top 5 most weather delayed airports
      output$table <- renderDataTable(
        top_5, 
        options = list(searching = FALSE, paging=FALSE, autowidth=TRUE)
        )
      
      added_data <- top_10[,c("iata_code","mean_delay")]
      
      # Create the final dataframe for plotting
      airports_plot <- merge(new_airports, added_data, by="iata_code", all.x=TRUE)
      airports_plot[is.na(airports_plot)] <- 0
      
      # Create a Leaflet map plot to visualize the airports/cities where extreme weather delays occured
      # The circle size indicates the mean value of the weather delay at each airport
      # The larger the circle, the more severe weather occurs here

      
      circle_df <- subset(airports_plot, mean_delay>0)
      
      labs <- lapply(seq(nrow(circle_df)), function(i) {
        paste0( "IATA: ", circle_df[i, "iata_code"], '<br />', "Mean_Delay: ",
                round(circle_df[i, "mean_delay"],2)) 
      })
      
      map <- leaflet(circle_df) %>% addTiles() %>%
        addCircles(lng = ~longitude_deg, lat = ~latitude_deg, weight = 10,
                   radius = ~ mean_delay^2*30, stroke=FALSE, fillOpacity = 0.7,
                   color = "blue",label = lapply(labs, HTML), 
                   labelOptions = labelOptions(textsize = "15px")
        )
    
    # Add flight weather delay polylines on the map
    
    mydf <- subset(df, Origin %in% top_10$iata_code | Dest %in% top_10$iata_code)
    mydf <- subset(df, WeatherDelay < cutoff_delays & WeatherDelay > 30)
    ### --- reshaping the data ----
    ## keep the order - but because we're going to split the data, only use odd numbers
    ## and we'll combine the even's on later
    mydf$myOrder <- seq(from = 1, to = ((nrow(mydf) * 2) - 1), by = 2)
    
    ## put the data in long form by splitting into two sets and then rbinding them
    ## I'm renaming the columns using setNames, as we need to `rbind` them
    ## together later
    df1 <- setNames(mydf[, c("Origin","Dest","origin_lat","origin_lon", "myOrder")],
                    c("Origin","Dest", "lat","lon", "myOrder"))
    
    df2 <- setNames(mydf[, c("Origin","Dest","dest_lat","dest_lon", "myOrder")],
                    c("Origin","Dest", "lat","lon", "myOrder"))
    
    ## make df2's order even
    df2$myOrder <- (df2$myOrder + 1)
    
    line_df <- rbind(df1, df2)
    
    ## can now sort the dataframe
    line_df <- line_df[with(line_df, order(myOrder)), ]
    
    ## and de-dupelicate it
    line_df <- unique(line_df[, c("Origin","Dest", "lat","lon")])
    ### -----------------------------
    line_df$id <- paste0(line_df$Origin,line_df$Dest)
    ## without using any spatial objects, you add different lines in a loop
    for(i in unique(line_df$id)){
      map <- addPolylines(map, data = line_df[line_df$id == i,], 
                          lat = ~lat, lng = ~lon, group = ~id, weight=1.5, 
                          fillColor = "green", color="green",
                          fillOpacity = 0.1, opacity=0.1)
    }
    
    mydf <- subset(df, Origin %in% top_10$iata_code | Dest %in% top_10$iata_code)
    mydf <- subset(df, WeatherDelay > cutoff_delays)
    ### --- reshaping the data ----
    ## keep the order - but because we're going to split the data, only use odd numbers
    ## and we'll combine the even's on later
    mydf$myOrder <- seq(from = 1, to = ((nrow(mydf) * 2) - 1), by = 2)
    
    ## put the data in long form by splitting into two sets and then rbinding them
    ## I'm renaming the columns using setNames, as we need to `rbind` them
    ## together later
    df1 <- setNames(mydf[, c("Origin","Dest","origin_lat","origin_lon", "myOrder")],
                    c("Origin","Dest", "lat","lon", "myOrder"))
    
    df2 <- setNames(mydf[, c("Origin","Dest","dest_lat","dest_lon", "myOrder")],
                    c("Origin","Dest", "lat","lon", "myOrder"))
    
    ## make df2's order even
    df2$myOrder <- (df2$myOrder + 1)
    
    line_df2 <- rbind(df1, df2)
    
    ## can now sort the dataframe
    line_df2 <- line_df2[with(line_df2, order(myOrder)), ]
    
    ## and de-dupelicate it
    line_df2 <- unique(line_df2[, c("Origin","Dest", "lat","lon")])
    ### -----------------------------
    line_df2$id <- paste0(line_df2$Origin,line_df2$Dest)
    ## without using any spatial objects, you add different lines in a loop
    for(i in unique(line_df2$id)){
      map <- addPolylines(map, data = line_df2[line_df2$id == i,], 
                          lat = ~lat, lng = ~lon, group = ~id, weight=3, 
                          fillColor = "red", color="red",
                          fillOpacity = 0.1, opacity=0.1)
    }
    map <-  addLegend(map, colors=c("green","red"), 
                      label=c("moderate-delay","severe-delay"), opacity = 0.3,
                      position="bottomleft")
    
    map
    
})

    
  
    # Create barplot to summarize worst weahter-delayed airports in a month
    output$bar_plot <- renderPlot({
      month <- as.numeric(input$user_month2)
      # Compute the weather dealyed frequency 
      counts <- list()
      
      df <- subset(air, Month==month)
      max_days <- max(df$DayofMonth)
      for(day in seq(max_days)){
        df <- subset(air, Month==month)
        df <- subset(df, DayofMonth==day)
        
        
        dest_count <- as.data.frame(table(df$Dest))
        origin_count <- as.data.frame(table(df$Origin))
        
        total_count <- merge(dest_count, origin_count, by="Var1")
        total_count$total <- total_count$Freq.x + total_count$Freq.y
        colnames(total_count) <- c("iata_code","dest_count","origin_count","total_delay_counts")
        
        new_airports <- merge(airports, total_count, by="iata_code")
        top_5 <- head(new_airports[order(new_airports$total_delay_counts, decreasing = TRUE),], 5)
        
        collection <- c()
        i <- 1
        for(item in top_5$iata_code){
          collection[i] <- mean(subset(df, Dest==item|Origin==item)$WeatherDelay)
          i <- i+1
        }
        top_5_mean_delay <- as.matrix(collection)
        top_5_mean_delay <- as.data.frame(top_5_mean_delay)
        colnames(top_5_mean_delay) <- "mean_delay"
        top_5 <- cbind(top_5, top_5_mean_delay)
        added_data <- top_5[,c("iata_code","mean_delay")]
        
        airports_plot <- merge(new_airports, added_data, by="iata_code", all.x=TRUE)
        
        airports_plot[is.na(airports_plot)] <- 0
        
        counts[[day]] <- top_5$iata_code
        
      }
      df2 <- counts[[1]]
      for(i in seq(2:max_days)){
        df2 <- rbind(df2, counts[[i]])
      }
      
      data <- table(df2)
      data <- as.data.frame(head(sort(data,decreasing = TRUE),8))
      colnames(data) <- c("Aiport_Code","Weather_Delay_Frequency")
      # Plot the bar charts
      colfunc <- colorRampPalette(c("purple", "violet"))

      ggplot(data, aes(x=Aiport_Code, y=Weather_Delay_Frequency)) +
        geom_bar(stat="identity", fill=colfunc(8))+
        geom_text(aes(label=Aiport_Code), vjust=-0.3, size=3.5)+
        theme_minimal()
      
    }
      )
    
}

