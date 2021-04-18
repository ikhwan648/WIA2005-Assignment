import gmplot
import requests
import json
from copy import deepcopy

######### Selection Sort ##############

def sort_hub(ori_hub_dest,copy_hub_name,copy_hub_lats,copy_hub_lngs):
    for idx in range(len(ori_hub_dest)):
        for i in range(len(ori_hub_dest[idx])):
            min_idx = i
            for j in range( i +1, len(ori_hub_dest[idx])):
                if ori_hub_dest[idx][min_idx] > ori_hub_dest[idx][j]:
                    min_idx = j
            ori_hub_dest[idx][i],ori_hub_dest[idx][min_idx] = ori_hub_dest[idx][min_idx],ori_hub_dest[idx][i]
            copy_hub_name[idx][i],copy_hub_name[idx][min_idx] = copy_hub_name[idx][min_idx],copy_hub_name[idx][i]
            copy_hub_lats[idx][i],copy_hub_lats[idx][min_idx] = copy_hub_lats[idx][min_idx],copy_hub_lats[idx][i]
            copy_hub_lngs[idx][i],copy_hub_lngs[idx][min_idx] = copy_hub_lngs[idx][min_idx],copy_hub_lngs[idx][i]


############# Part 1 ###############

# Create the map plotter:
api_key = 'AIzaSyDbyq06H7kJ'
gmap = gmplot.GoogleMapPlotter(3.0303666, 101.5501978, 10.5, apikey=api_key)
gmap.coloricon="http://www.googlemapsmarkers.com/v1/%s/"

hub_name, hub_lats, hub_lngs = zip(*[
    ('City-link Express (Port Klang)',3.0319924887507144, 101.37344116244806),
    ('Pos Laju (Petaling Jaya)',3.112924170027219, 101.63982650389863),
    ('GDEX (Batu Caves)',3.265154613796736, 101.68024844550233),
    ('J&T (Kajang)',2.9441205329488325, 101.7901521759029),
    ('DHL (Sungai Buloh)',3.2127230893650065, 101.57467295692778),
])

cus_no,cus_origin_lats, cus_origin_lngs = zip(*[
    ('Customer 1',3.3615395462207878, 101.56318183511695),
    ('Customer 2',3.049398375759954, 101.58546611160301),
    ('Customer 3',3.141855957281073, 101.76158583424586),
])

cus_dest_lats, cus_dest_lngs = zip(*[
    (3.1000170516638885, 101.53071480907951),   #Customer 1
    (3.227994355250716, 101.42730357605375),    #Customer 2
    (2.9188704151716256, 101.65251821655471),   #Customer 3
])

for i in range(len(hub_name)):
    gmap.marker(hub_lats[i],hub_lngs[i],color='blue',title=hub_name[i])
gmap.draw("map_mark_hub.html")

########### Part 2 ###############

url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
print("Distance between origin and destination")
for i in range(len(cus_origin_lats)):
    urlpanjang=url+'origins='+str(cus_origin_lats[i])+','+str(cus_origin_lngs[i])+'&destinations='+str(cus_dest_lats[i])+','+str(cus_dest_lngs[i])+'&key='+api_key
    r=requests.get(urlpanjang)
    x = r.json()
    print("Customer",[i+1],": ",x['rows'][0]['elements'][0]['distance']['text'])

print("")

######### Part 3 #############

ori_hub=([0]*len(hub_name),[0]*len(hub_name),[0]*len(hub_name))
hub_dest=([0]*len(hub_name),[0]*len(hub_name),[0]*len(hub_name))

# Distance between origin and destination
count=0
while count<3:
    for i in range(len(hub_name)):
        urlpanjang=url+'origins='+str(cus_origin_lats[count])+','+str(cus_origin_lngs[count])+'&destinations='+str(hub_lats[i])+','+str(hub_lngs[i])+'&key='+api_key
        r=requests.get(urlpanjang)
        x = r.json()
        ori_hub[count][i]=x['rows'][0]['elements'][0]['distance']['value']
    count+=1

# Distance between hub and destination
count=0
while count<3:
    for i in range(len(hub_name)):
        urlpanjang=url+'origins='+str(hub_lats[i])+','+str(hub_lngs[i])+'&destinations='+str(cus_dest_lats[count])+','+str(cus_dest_lngs[count])+'&key='+api_key
        r=requests.get(urlpanjang)
        x = r.json()
        hub_dest[count][i]=x['rows'][0]['elements'][0]['distance']['value']
    count+=1

print("Distance between origin and destination through hub")
ori_hub_dest=([0]*len(hub_name),[0]*len(hub_name),[0]*len(hub_name))
count=0
while count<3:
    for i in range(len(hub_name)):
        ori_hub_dest[count][i]=ori_hub[count][i]+hub_dest[count][i]
        print("customer",[count+1],": ",(ori_hub_dest[count][i]/1000),"km -> ",hub_name[i])
    count+=1

print("")

copy_ori_hub_dest=deepcopy(ori_hub_dest)
copy_hub_name=(list(hub_name),list(hub_name),list(hub_name))
copy_hub_lats=(list(hub_lats),list(hub_lats),list(hub_lats))
copy_hub_lngs=(list(hub_lngs),list(hub_lngs),list(hub_lngs))
sort_hub(copy_ori_hub_dest,copy_hub_name,copy_hub_lats,copy_hub_lngs)

print("")

print("The shortest distance ")
for i in range(len(copy_ori_hub_dest)):
    print("Customer",[i+1]," : ",(copy_ori_hub_dest[i][0]/1000),"km -> ",copy_hub_name[i][0])

############ Part 4 ###############

for i in range(len(cus_no)):
    gmap.directions(
    (cus_origin_lats[i],cus_origin_lngs[i]),
    (cus_dest_lats[i],cus_dest_lngs[i]),
    waypoints=[(cus_origin_lats[i],cus_origin_lngs[i]),(copy_hub_lats[i][0], copy_hub_lngs[i][0]),(cus_dest_lats[i],cus_dest_lngs[i])]
)

gmap.draw('map_line_shortest.html')