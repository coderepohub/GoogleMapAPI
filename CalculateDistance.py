import requests
import json

apiKey = 'YOUR_GMAP_API_KEY'
source = input("Please Enter Source Location : ") #input source distance 
destination = input("Please Enter Destination Location : ") #input destination

url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
requestUrl = url+'origins='+source+'&destinations='+destination+'&key='+apiKey
res = requests.get(requestUrl)

result = res.json()
total_distance = result['rows'][0]['elements'][0]['distance']['text']
total_time_taken = result['rows'][0]['elements'][0]['duration']['text']
print('Total Distance - ',total_distance)
print('Total Travelling time - ',total_time_taken)