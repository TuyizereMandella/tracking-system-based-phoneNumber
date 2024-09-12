import phonenumbers
import opencage
import folium
from number import numbers

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(numbers)
location = geocoder.description_for_number(pepnumber, "en")
print(location)
from  phonenumbers import carrier
service_pro = phonenumbers.parse(numbers)
print(carrier.name_for_number(service_pro,"en"))


from opencage.geocoder import OpenCageGeocode

key = '8b58448bd02c40168ee3135dfcb95d10'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

mymap = folium.Map(location=[lat,lng],zoom_start=90)
folium.Marker([lat,lng ], popup=location).add_to(mymap)

mymap.save("mylocation.html")
#-1.9646631 30.0644358
