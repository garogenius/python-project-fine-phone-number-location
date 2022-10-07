import phonenumbers
from myNumber import number 
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
pepnumber=phonenumber.parse(number)
location=geocoder.description_for_number(pepnumber, "en")
print(location)

ser_pr=phonenumbers.parse(number)
print(carrier.name_for_number(ser_pr,"en"))

key=""
geocoder=OpenCageGeocode(key)
query=str(location)
result=geocoder.geocode(query)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']

print(lat)
print(lng)

mymap=folium.Map(location[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(mymap)
mymap.save("location.html")