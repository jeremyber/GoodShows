import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


showsDF = pd.read_csv("../data/shows_2.23.2020.csv")
showsDF = showsDF.head(50)


locator = Nominatim(user_agent="myGeocoder")

# 1 - convenient function to delay between geocoding calls
#geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

# 2- - create location column
showsDF['location'] = showsDF['Venue'].apply(locator.geocode)

# 3 - create lon, lat and altitude from location column (tuple)
showsDF['point'] = showsDF['location'].apply(lambda loc: tuple(loc.point) if loc else None)

#4 split point column  into lat lon and altitude
showsDF[['latitude', 'longitude', 'altitude']] = pd.DataFrame(showsDF['point'].tolist(), index=showsDF.index)
print(showsDF.to_string())
