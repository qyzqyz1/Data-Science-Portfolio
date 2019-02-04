setwd('C:/Users/yizhe/Desktop/MDS/Term4/data_550/miniposter/')
air <- read.csv("air.csv")
source("airports.R")
source("cancellations.R")
source("FlightBehaviour.R")

server <-
function(input,output){
  
    output$main_plot <- renderPlot({
      
      day <- as.numeric(input$user_day)
      month <- as.numeric(input$user_month)
      cutoff_delays <- as.numeric(input$user_delays)
      map_title <- input$map_title
      
      winter_day <- subset(air, Month==month)

      if (!is.null(day)){
        winter_day <- subset(winter_day, DayofMonth==day)
      }
      
      NNA_wd <- winter_day[complete.cases(winter_day[ , 'WeatherDelay']),]
      
      NNA_wd <- subset(NNA_wd, WeatherDelay > 0)
      
   
      
      # Exploring dataset
      ori_name <- unique(NNA_wd$Origin)
      dest_name <- unique(NNA_wd$Dest)
      
      # Adding latitude and longitude information from the airport.R dataframe to our air dataframe
      listofdfs <- list()
      for(item in ori_name){
        latOrigin <- subset(airports,iata_code==item)['latitude_deg'][1,]
        longOrigin <- subset(airports,iata_code==item)['longitude_deg'][1,]
        s <- subset(NNA_wd, Origin==item)
        s$latOrigin <- latOrigin
        s$longOrigin <- longOrigin
        listofdfs[[item]] <- s
      }
      
      
      NNA_wd <- do.call("rbind", listofdfs)
      
      listofdfs <- list()
      for(item in dest_name){
        latDest <- subset(airports,iata_code==item)['latitude_deg'][1,]
        longDest <- subset(airports,iata_code==item)['longitude_deg'][1,]
        s <- subset(NNA_wd, Dest==item)
        s$latDest <- latDest
        s$longDest <- longDest
        listofdfs[[item]] <- s
      }
      NNA_wd <- do.call("rbind", listofdfs)
      

      
      dest_count <- as.data.frame(table(NNA_wd$Dest))

      
      origin_count <- as.data.frame(table(NNA_wd$Origin))

      
      total_count <- merge(dest_count, origin_count, by="Var1")
      total_count$total <- total_count$Freq.x + total_count$Freq.y
      colnames(total_count) <- c("iata_code","dest_count","origin_count","total_delay_counts")
      

      
      new_airports <- merge(airports, total_count, by="iata_code")
      top_10 <- head(new_airports[order(new_airports$total_delay_counts, decreasing = TRUE),], 10)
      
      top_10
      
      collection <- c()
      i <- 1
      for(item in top_10$iata_code){
        collection[i] <- mean(subset(NNA_wd, Dest==item|Origin==item)$WeatherDelay)
        i <- i+1
      }
      top_10_mean_delay <- as.matrix(collection)
      top_10_mean_delay <- as.data.frame(top_10_mean_delay)
      colnames(top_10_mean_delay) <- "mean_delay"
      top_10 <- cbind(top_10, top_10_mean_delay)
      added_data <- top_10[,c("iata_code","mean_delay")]
      
      airports_plot <- merge(new_airports, added_data, by="iata_code", all.x=TRUE)
      
      airports_plot[is.na(airports_plot)] <- 0
      
      # Map plot to visualize the flight routes where extreme delays occured
      # The circle and code size also show the number of visits by US airline at each airport 
      colfunc <- colorRampPalette(c("green","red"))
      library(rworldmap)
      newmap <- getMap(resolution = "low")
      plot(newmap,  ylim=c(21, 50), xlim=c(-125, -65),col = "gray98")
      par(new=TRUE)
      
      plot(latitude_deg ~ longitude_deg, data = airports_plot,
           cex=sqrt(mean_delay)/1.2, ylim=c(21, 50), xlim=c(-125, -65), axes=FALSE, xlab="", ylab="", col="red") 
      
      title("Weather Delay Conditions vs. Airports")
      
      
      
      legend("bottomleft", legend=c("size: Average Delay per Flight"), pch=c(1), col="red",cex=0.9)
      legend("bottomright", legend=c("Code size: Total Delayed Flights"), cex=0.9)
      
      
      with(subset(NNA_wd, WeatherDelay>15 & WeatherDelay<cutoff_delays), segments(longOrigin, latOrigin,
                                                                       longDest, latDest, col="green", lwd=1.5))
      
      with(subset(NNA_wd, WeatherDelay>cutoff_delays), segments(longOrigin, latOrigin,
                                                     longDest, latDest, col="pink", lwd=2))
      
      
      text(latitude_deg ~ longitude_deg, label=iata_code, data = subset(airports_plot, total_delay_counts>0), 
           ylim=c(21, 50), xlim=c(-125, -65),cex=sqrt(total_delay_counts)/8, adj=1, col="blue", font=2)
      
      legend("topright", legend=c("Medium Delay", "Severe Delay"),
             col=c("green", "pink"), lty=1, lwd=c(2,2), cex=0.7, box.lty=0)
    })
  
    
    output$bar_plot <- renderPlot({
      month <- as.numeric(input$user_month2)
      top <- as.numeric(input$user_top)
      # Compute the weather dealyed frequency 
      counts <- list()
      winter_day <- subset(air, Month==month)
      max_days <- max(winter_day$DayofMonth)
      for(day in seq(max_days)){
        winter_day <- subset(air, Month==month)
        winter_day <- subset(winter_day, DayofMonth==day)
        
        
        NNA_wd <- winter_day[complete.cases(winter_day[ , 'WeatherDelay']),]
        NNA_wd <- subset(NNA_wd, WeatherDelay > 0)

        # Exploring dataset
        ori_name <- unique(NNA_wd$Origin)
        dest_name <- unique(NNA_wd$Dest)
        
        # Adding latitude and longitude information from the airport.R dataframe to our air dataframe
        listofdfs <- list()
        for(item in ori_name){
          latOrigin <- subset(airports,iata_code==item)['latitude_deg'][1,]
          longOrigin <- subset(airports,iata_code==item)['longitude_deg'][1,]
          s <- subset(NNA_wd, Origin==item)
          s$latOrigin <- latOrigin
          s$longOrigin <- longOrigin
          listofdfs[[item]] <- s
        }
        
        
        NNA_wd <- do.call("rbind", listofdfs)
        
        listofdfs <- list()
        for(item in dest_name){
          latDest <- subset(airports,iata_code==item)['latitude_deg'][1,]
          longDest <- subset(airports,iata_code==item)['longitude_deg'][1,]
          s <- subset(NNA_wd, Dest==item)
          s$latDest <- latDest
          s$longDest <- longDest
          listofdfs[[item]] <- s
        }
        NNA_wd <- do.call("rbind", listofdfs)
        
        dest_count <- as.data.frame(table(NNA_wd$Dest))
        origin_count <- as.data.frame(table(NNA_wd$Origin))
        
        total_count <- merge(dest_count, origin_count, by="Var1")
        total_count$total <- total_count$Freq.x + total_count$Freq.y
        colnames(total_count) <- c("iata_code","dest_count","origin_count","total_delay_counts")
        
        new_airports <- merge(airports, total_count, by="iata_code")
        top_5 <- head(new_airports[order(new_airports$total_delay_counts, decreasing = TRUE),], 5)
        
        collection <- c()
        i <- 1
        for(item in top_5$iata_code){
          collection[i] <- mean(subset(NNA_wd, Dest==item|Origin==item)$WeatherDelay)
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
      df <- counts[[1]]
      for(i in seq(2:max_days)){
        df <- rbind(df, counts[[i]])
      }
      
      data <- table(df)
      colfunc <- colorRampPalette(c("purple", "violet"))
      
      
      xx <- barplot(head(sort(data,decreasing = TRUE),top), cex.names=1,
                    col=colfunc(top), ylab='Weather-Delay Frequency in December', xlab='Airport Code', ylim=c(0,31))

      y <- head(sort(data,decreasing = TRUE),top)
      
      title('Fig2: Top Weather-Delayed Airports in the Month', cex = 1.5,   font.main= 2, line=-0.2)
      
    }
      )
    
}


