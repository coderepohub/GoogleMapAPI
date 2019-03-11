# A Python Project to interact with Google Map API 
## This is a simple project Containing two solutions which will accept Source location and destination location from user and return the total distance between source and destination as well as total time for travel between the two

1- *CalculateDistance.py* - This file will call the Google MAp API as a rest service and deserialize the response as JSON 

2- *CalculateDistanceWithGMap.py* - This fill will call the Gmap API using **Google Map** library , the response will be a JSON response from the library.
NOTE - To use this we need to install this first by running *pip install googlemaps* command in CMD.

### To make this solution working we need to have Google map api for this visit [Google Developer Portal](https://console.cloud.google.com/) and then search for [Direction API] (https://developers.google.com/maps/documentation/directions/start) add it and note down the key