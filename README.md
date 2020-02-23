# GoodShows
This is my first attempt at building a recommender system for live music

## Project Layout and functionality
1. Current shows will be stored in Postgres
2. I'll make a python script to do a few things:
    1. load the data from a csv into PG
    2. retrieve the data from PG
    3. display the following stats:
        1. most popular artist (by year, all time)
        2. most popular venues (by year, all time)
        3. Charts (for both)
        4. Map - use google maps api maybe to get the geolocation of the venues and cluster / heatmap accordingly
        5. Try to find the cost of each show on songkick to estimate total cost overall
    4. Recommender System using Spotify and/or last.fm
    5. Make a playlist based on shows I've been to (Spotify)
   
To start I'll use Flask for all the back end stuff but I'll leave room to revise into a full on WS if I like it enough.
