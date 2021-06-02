import problem1 as p1
import problem2 as p2
import problem3 as p3
import problem4 as p4

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

txtname=['citylinkCompile.txt','poslajuCompile.txt','gdexCompile.txt','j&tCompile.txt','dhlCompile.txt']
ration=[0]*len(txtname)

# x=p1.problem1(hub_name,hub_lats,hub_lngs,cus_no,cus_origin_lats,cus_origin_lngs,cus_dest_lats,cus_dest_lngs)
# ori_hub_dest=x.get_ori_hub_dest()
# x.solving_Problem1()

# for i in range(len(txtname)):
#     z=p2.problem2(txtname[i])
#     z.solving_Problem2()
#     ration[i]=z.get_ration()

# print(ration)

# y=p3.problem3(ori_hub_dest,hub_name,ration)
# y.solving_Problem3()

k=p4.problem4()
k.solving_Problem4()