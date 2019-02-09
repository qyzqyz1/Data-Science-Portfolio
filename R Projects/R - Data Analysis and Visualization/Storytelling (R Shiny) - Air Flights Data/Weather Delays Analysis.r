
# Load the datasets
setwd('C:/Users/yizhe/Desktop/MDS/Term4/data_550/miniposter/')
air <- read.csv("air.csv")
source("airports.R")
source("cancellations.R")
source("FlightBehaviour.R")

head(air)

winter_day <- subset(air, Month==12)
day <- 25
if (!is.null(day)){
    winter_day <- subset(winter_day, DayofMonth==day)
}

NNA_wd <- winter_day[complete.cases(winter_day[ , 'WeatherDelay']),]

NNA_wd <- subset(NNA_wd, WeatherDelay > 0)

head(sort(table(NNA_wd$Origin),decreasing = T),10)

head(sort(table(NNA_wd$Dest),decreasing = T),10)

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

head(airports)

dest_count <- as.data.frame(table(NNA_wd$Dest))
head(dest_count)

origin_count <- as.data.frame(table(NNA_wd$Origin))
head(origin_count)

total_count <- merge(dest_count, origin_count, by="Var1")
total_count$total <- total_count$Freq.x + total_count$Freq.y
colnames(total_count) <- c("iata_code","dest_count","origin_count","total_delay_counts")

head(total_count)

new_airports <- merge(airports, total_count, by="iata_code")
top_10 <- head(new_airports[order(new_airports$total_delay_counts, decreasing = T),], 10)

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

airports_plot <- merge(new_airports, added_data, by="iata_code", all.x=T)

airports_plot[is.na(airports_plot)] <- 0

# Map plot to visualize the delayed flight routes caused by extreme weather condition
# The code size indicates the total number of weather-delayed flights associated with that airport, the larger the code size, 
# the more weather-delayed flights are related to the airport, therefore the more likely the delay is due to the 
# weather condition at that aiport 
# The circle size shows the amount of average weather delay experienced per flight at that airport. It can potentially indicate
# how bad the weather could be at that airport. The worse the weather, the more average delay per flight might experience

colfunc <- colorRampPalette(c("green","red"))
library(rworldmap)
newmap <- getMap(resolution = "low")
plot(newmap,  ylim=c(21, 50), xlim=c(-125, -69),col = "gray98", asp=1.6)
par(new=TRUE)

plot(latitude_deg ~ longitude_deg, data = airports_plot,
cex=sqrt(mean_delay)/1.2, ylim=c(21, 50), xlim=c(-125, -70), axes=FALSE, xlab="", ylab="", col="red") 

title("Fig1: Weather Delay vs. Airports on Christmas")



legend("bottomleft", legend=c("size: No. Average Delay Amount"), pch=c(1), col="red",cex=0.9)
legend("bottomright", legend=c("Code size: No. Total Delays"), cex=0.9)


with(subset(NNA_wd, WeatherDelay>15 & WeatherDelay<90), segments(longOrigin, latOrigin,
longDest, latDest, col="green", lwd=1.5))

with(subset(NNA_wd, WeatherDelay>90), segments(longOrigin, latOrigin,
longDest, latDest, col="pink", lwd=2))


text(latitude_deg ~ longitude_deg, label=iata_code, data = subset(airports_plot, total_delay_counts>0), 
     ylim=c(21, 50), xlim=c(-125, -65),cex=sqrt(total_delay_counts)/8, adj=1, col="blue", font=2)

legend("topright", legend=c("Medium Delay (<90 mins)", "Severe Delay (>90 mins)"),
       col=c("green", "pink"), lty=1, lwd=c(2,2), cex=0.7, box.lty=0)

# The top 5 obvious airports with bad weather on Christmas day in 2008 are SLC, LAS, SEA, ORD and DEN
# Salt Lake City is definitely the worst airport with the probability of having the worst weather on that day
# since it has both the largest number of weather-delayed flights and the highest average delayed time per flight

# However, this is a single analysis on a particular day... How about the overall condition for the entire month?
# Is SLC still the worst?

# Compute the weather dealyed frequency 
counts <- list()
winter_day <- subset(air, Month==12)
max_num <- max(winter_day$DayofMonth)
for(day in seq(max_num)){
    

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
top_5 <- head(new_airports[order(new_airports$total_delay_counts, decreasing = T),], 5)

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

airports_plot <- merge(new_airports, added_data, by="iata_code", all.x=T)

airports_plot[is.na(airports_plot)] <- 0

counts[[day]] <- top_5$iata_code

}

df <- counts[[1]]
for(i in seq(2:31)){
    df <- rbind(df, counts[[i]])
}

data <- table(df)
colfunc <- colorRampPalette(c("purple", "violet"))


xx <- barplot(head(sort(data,decreasing = T),8), cex.names=1,
       col=colfunc(8), ylab='Weather-Delay Frequency in December', xlab='Airport Code', ylim=c(0,31))

values <- c("Chicago","Atlanta","Dallas","Hebron","Denver","Detroit","Newark","Houston")

y <- head(sort(data,decreasing = T),8)

text(xx, y+1.8, label = values, cex = 1, col = "black", srt=30)
title('Fig2: Top 8 Weather-Delayed Airports in December?', cex = 1.5,   font.main= 2, line=-0.2)


names(y)

# After iterating the above analysis for every single day in December, I performed a summarization and plotted the top 8 
# weather-delayed airports for the month. Clearly, ORD, ATL, and IAH are on average the top 3 common airports with weather delays 
# in December, which could suggest that for your next year's winter travel, they may not be among your top choice list 
# not only because there is a large chance for you to experience weather delay at the airports 
# but also you may be less likely to enjoy the weather in the city.

unique(air$Dest)
