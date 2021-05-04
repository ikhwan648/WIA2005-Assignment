import gmplot
import requests
import json
from copy import deepcopy

api_key = 'AIzaSyDbyq06H7kJtIKq'
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

class problem1:

    def __init__(self, hub_name, hub_lats, hub_lngs, cus_no, cus_origin_lats, cus_origin_lngs, cus_dest_lats,
                 cus_dest_lngs):
        self._hub_name = hub_name
        self._hub_lats = hub_lats
        self._hub_lngs = hub_lngs
        self._cus_no = cus_no
        self._cus_origin_lats = cus_origin_lats
        self._cus_origin_lngs = cus_origin_lngs
        self._cus_dest_lats = cus_dest_lats
        self._cus_dest_lngs = cus_dest_lngs
        self._ori_hub_dest = tuple((([0 for i in range(len(self._hub_name))]) for i in range(len(self._cus_no))))
        self._copy_ori_hub_dest = ()
        self._copy_hub_name = (list(self._hub_name), list(self._hub_name), list(self._hub_name))
        self._copy_hub_lats = (list(self._hub_lats), list(self._hub_lats), list(self._hub_lats))
        self._copy_hub_lngs = (list(self._hub_lngs), list(self._hub_lngs), list(self._hub_lngs))

    def solving_Problem1(self):
        gmap = gmplot.GoogleMapPlotter(3.0303666, 101.5501978, 10.5, apikey=api_key)
        gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

        for i in range(len(self._hub_name)):
            gmap.marker(self._hub_lats[i], self._hub_lngs[i], color='blue', title=self._hub_name[i])
        gmap.draw("map_mark_hub.html")

        print("Distance between origin and destination")
        for i in range(len(self._cus_origin_lats)):
            urlpanjang = url + 'origins=' + str(self._cus_origin_lats[i]) + ',' + str(
                self._cus_origin_lngs[i]) + '&destinations=' + str(self._cus_dest_lats[i]) + ',' + str(
                self._cus_dest_lngs[i]) + '&key=' + api_key
            r = requests.get(urlpanjang)
            x = r.json()
            print("Customer", [i + 1], ": ", x['rows'][0]['elements'][0]['distance']['text'])
        print("")

        ori_hub = tuple((([0 for i in range(len(self._hub_name))]) for i in range(len(self._cus_no))))
        hub_dest = tuple((([0 for i in range(len(self._hub_name))]) for i in range(len(self._cus_no))))

        # Distance between origin and destination
        count = 0
        n = len(self._cus_no)
        while count < n:
            for i in range(len(self._hub_name)):
                urlpanjang = url + 'origins=' + str(self._cus_origin_lats[count]) + ',' + str(
                    self._cus_origin_lngs[count]) + '&destinations=' + str(self._hub_lats[i]) + ',' + str(
                    self._hub_lngs[i]) + '&key=' + api_key
                r = requests.get(urlpanjang)
                x = r.json()
                ori_hub[count][i] = x['rows'][0]['elements'][0]['distance']['value']
            count += 1

        # Distance between hub and destination
        count = 0
        while count < n:
            for i in range(len(self._hub_name)):
                urlpanjang = url + 'origins=' + str(self._hub_lats[i]) + ',' + str(
                    self._hub_lngs[i]) + '&destinations=' + str(self._cus_dest_lats[count]) + ',' + str(
                    self._cus_dest_lngs[count]) + '&key=' + api_key
                r = requests.get(urlpanjang)
                x = r.json()
                hub_dest[count][i] = x['rows'][0]['elements'][0]['distance']['value']
            count += 1

        print("Distance between origin and destination through hub")
        count = 0
        while count < n:
            for i in range(len(self._hub_name)):
                self._ori_hub_dest[count][i] = ori_hub[count][i] + hub_dest[count][i]
                print("customer", [count + 1], ": ", round((self._ori_hub_dest[count][i] / 1000), 1), "km -> ",self._hub_name[i])
            count += 1
        
        print('')

        self._copy_ori_hub_dest = deepcopy(self._ori_hub_dest)
        
        self.__sorting()

        for idx in range(len(self._ori_hub_dest)):
            for i in range(len(self._ori_hub_dest[idx])):
                print("Customer", [idx + 1], ": ", round((self._copy_ori_hub_dest[idx][i] / 1000), 1), "km -> ",self._copy_hub_name[idx][i])

        print('')

        print("The shortest distance ")
        for i in range(len(self._copy_ori_hub_dest)):
            print("Customer", [i + 1], ": ", round((self._copy_ori_hub_dest[i][0] / 1000), 1), "km -> ",self._copy_hub_name[i][0])

        for i in range(len(self._cus_no)):
            gmap.directions(
                (self._cus_origin_lats[i], self._cus_origin_lngs[i]),
                (self._cus_dest_lats[i], self._cus_dest_lngs[i]),
                waypoints=[(self._cus_origin_lats[i], self._cus_origin_lngs[i]),
                           (self._copy_hub_lats[i][0], self._copy_hub_lngs[i][0]),
                           (self._cus_dest_lats[i], self._cus_dest_lngs[i])]
            )
        gmap.draw('map_line_shortest.html')

    def get_copy_ori_hub_dest(self):
        return self._copy_ori_hub_dest

    def get_ori_hub_dest(self):
        return self._ori_hub_dest

    def get_copy_hub_name(self):
        return self._copy_hub_name

    def __sorting(self):
        for idx in range(len(self._copy_ori_hub_dest)):
            for i in range(len(self._copy_ori_hub_dest[idx])):
                min_idx = i
                for j in range(i + 1, len(self._copy_ori_hub_dest[idx])):
                    if self._copy_ori_hub_dest[idx][min_idx] > self._copy_ori_hub_dest[idx][j]:
                        min_idx = j
                self._copy_ori_hub_dest[idx][i], self._copy_ori_hub_dest[idx][min_idx] = self._copy_ori_hub_dest[idx][min_idx], self._copy_ori_hub_dest[idx][i]
                self._copy_hub_name[idx][i], self._copy_hub_name[idx][min_idx] = self._copy_hub_name[idx][min_idx],self._copy_hub_name[idx][i]
                self._copy_hub_lats[idx][i], self._copy_hub_lats[idx][min_idx] = self._copy_hub_lats[idx][min_idx],self._copy_hub_lats[idx][i]
                self._copy_hub_lngs[idx][i], self._copy_hub_lngs[idx][min_idx] = self._copy_hub_lngs[idx][min_idx],self._copy_hub_lngs[idx][i]
