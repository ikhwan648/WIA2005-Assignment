import gmplot
import requests
import json
import googlemaps

# Create the map plotter:
apikey = 'AIzaSyDbyq06H7kJtIKqnU7dBtLybsn5_O-LUOA' # (your API key here)
gmap = gmplot.GoogleMapPlotter(3.0303666, 101.5501978, 11, apikey=apikey)

hub_lats, hub_lngs = zip(*[
    (3.0319924887507144, 101.37344116244806),
    (3.112924170027219, 101.63982650389863),
    (3.265154613796736, 101.68024844550233),
    (2.9441205329488325, 101.7901521759029),
    (3.2127230893650065, 101.57467295692778),
])

cus_origin_lats, cus_origin_lngs = zip(*[
    (3.3615395462207878, 101.56318183511695),   #Customer 1
    (3.049398375759954, 101.58546611160301),    #Customer 2
    (3.141855957281073, 101.76158583424586),    #Customer 3
])

cus_dest_lats, cus_dest_lngs = zip(*[
    (3.1000170516638885, 101.53071480907951),   #Customer 1
    (3.227994355250716, 101.42730357605375),    #Customer 2
    (2.9188704151716256, 101.65251821655471),   #Customer 3
])

gmap.scatter(hub_lats, hub_lngs, color='#000000', size=100, marker=True)
gmap.scatter(cus_origin_lats, cus_origin_lngs, color='#ff0000', size=100, marker=True)
gmap.scatter(cus_dest_lats, cus_dest_lngs, color='#0000ff', size=100, marker=True)
gmap.draw('D:\\Users\\muham\\Visual Studio Projects\\WIA2005-Assignment\\maptest.html')


url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
urlpanjang=url+'origins='+str(cus_origin_lats[0])+','+str(cus_origin_lngs[0])+'&destinations='+str(cus_dest_lats[0])+','+str(cus_dest_lngs[0])+'&key='+apikey
print(urlpanjang)
# r = requests.get(url +'origins=', ,
#                    '&destinations=',3.1000170516638885,',',101.53071480907951,
#                    '&key=',apikey)
r=requests.get(urlpanjang)
x = r.json()
print(x['rows'][0]['elements'][0]['distance']['value'])
