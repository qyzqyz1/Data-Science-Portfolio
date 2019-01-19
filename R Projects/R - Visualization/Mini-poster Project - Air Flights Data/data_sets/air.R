source("airports.R")
names(airports)[4] <- "Origin"
air <- merge(air, airports)
names(airtest)[29] <- "lat_Origin"
names(airtest)[30] <- "long_Origin"
names(airtest)[32] <- "elev_Origin"
names(airport)[4] <- "Dest"
air <- merge(air, airports)
names(air)[33] <- "lat_Dest"
names(air)[34] <- "long_Dest"
names(air)[35] <- "elev_Dest"

