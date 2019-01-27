
air <- read.csv("air.csv")
source("airports.R")
source("cancellations.R")
source("FlightBehaviour.R")

server <-
function(input,output){
    output$main_plot <- renderPlot({
      
      # Map plot to visualize the flight routes where extreme delays occured
      # The circle and code size also show the number of visits by US airline at each airport 
      l_delay <- as.numeric(input$lower_delay)
      u_delay <- as.numeric(input$upper_delay)
      mi_delay <- as.numeric(input$mini_delay)
      title <- input$title
      
      # Subset to obtains the US airline flight data
      US <- subset(air, UniqueCarrier == 'US')

      
      # Drop NA values in the dataset
      US_NNA <- US[complete.cases(US[ , c("ArrDelay","DepDelay","CarrierDelay","WeatherDelay","NASDelay","SecurityDelay","LateAircraftDelay")]), ]

      
      # Exploring dataset
      ori_name <- unique(US_NNA$Origin)
      dest_name <- unique(US_NNA$Dest)
      
      # Adding latitude and longitude information from the airport.R dataframe to our air dataframe
      listofdfs <- list()
      for(item in ori_name){
        latOrigin <- subset(airports,iata_code==item)['latitude_deg'][1,]
        longOrigin <- subset(airports,iata_code==item)['longitude_deg'][1,]
        s <- subset(US_NNA, Origin==item)
        s$latOrigin <- latOrigin
        s$longOrigin <- longOrigin
        listofdfs[[item]] <- s
      }
      
      
      US_NNA <- do.call("rbind", listofdfs)
      
      listofdfs <- list()
      for(item in dest_name){
        latDest <- subset(airports,iata_code==item)['latitude_deg'][1,]
        longDest <- subset(airports,iata_code==item)['longitude_deg'][1,]
        s <- subset(US_NNA, Dest==item)
        s$latDest <- latDest
        s$longDest <- longDest
        listofdfs[[item]] <- s
      }
      US_NNA <- do.call("rbind", listofdfs)
      
      # Adding US airline visits at each airport to the airport.R dataframe
      c <- as.data.frame(table(US_NNA$Dest))
      d <- as.data.frame(table(US_NNA$Origin))
      df <- merge(c,d,by="Var1",all=TRUE)
      df$US_visits <- df$Freq.x + df$Freq.y
      colnames(df)[1] <- c("iata_code")

      
      airports <- merge(x=airports,y=df,by='iata_code',all.x=TRUE)

      
      colfunc <- colorRampPalette(c("green","red"))
      library(rworldmap)
      newmap <- getMap(resolution = "low")
      plot(newmap,  ylim=c(21, 50), xlim=c(-125, -65), col = "ghostwhite")
      par(new=TRUE)
      
      plot(latitude_deg ~ longitude_deg, data = airports,
           cex=sqrt(US_visits)/15, ylim=c(21, 50), xlim=c(-125, -65), axes=FALSE, xlab="", ylab="", col="purple")
      title(title)
      
      legend("bottomleft", legend=c("size & code size: No. US Airline Visits"), pch=c(1),cex=0.8, col="purple")
      
      with(subset(US_NNA, ArrDelay>mi_delay& ArrDelay<l_delay), segments(longOrigin, latOrigin,
                                                                longDest, latDest, col="green", lwd=1))
      
      with(subset(US_NNA, ArrDelay>l_delay & ArrDelay<u_delay), segments(longOrigin, latOrigin,
                                                                 longDest, latDest, col="orange", lwd=2))
      
      with(subset(US_NNA, ArrDelay>u_delay), segments(longOrigin, latOrigin,
                                                  longDest, latDest, col="red", lwd=2.5))
      
      
      text(latitude_deg ~ longitude_deg, label=iata_code,data = subset(airports, US_visits>1000), 
           ylim=c(21, 50), xlim=c(-125, -65),cex=sqrt(US_visits)/100, adj=1)
      
      legend("topright", legend=c("Moderate Delay (4-6 hrs)", "High Delay (6-10 hrs)", "Severe Delay (>10 hrs)"),
             col=c("green", "orange","red"), lty=1, lwd=c(1,1.5,2), cex=0.7, box.lty=0)
    })
}


