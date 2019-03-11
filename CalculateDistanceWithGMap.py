import googlemaps

gmaps = googlemaps.Client(key='YOUR_GMAP_API_KEY')

source = input("Please Enter Source Location : ") #input source distance 
destination = input("Please Enter Destination Location : ") #input destination

myDistance = gmaps.distance_matrix(source,destination)['rows'][0]['elements'][0]

total_distance = myDistance['distance']['text']
total_time_taken = myDistance['duration']['text']

print('Total Distance - ',total_distance)
print('Total Travelling time - ',total_time_taken)