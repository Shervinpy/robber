ferniture = {"laptop":[3,1200],"compiuter":[17,700],"freezer":[450,700], "tv":[50,200] ,"microphone" :[0.5,200]
, "gold":[5,3000], "chair":[50,100], "carpet":[70,1300], "desk":[350,150], "phone":[0.5,1800],"motorcycle":[80,800],
"bycycle":[10,900]
}
truck = 0
listrye = []
keyss = []

for i in ferniture.items():
    add = keyss.append(i[0])
    hight = i[1][0]
    dollar = i[1][1]
    poan = round(dollar / hight)
    listrye.append(poan) 
    margein = dict(zip(keyss,listrye))

while truck <=500:
 
     print(margein)
     x = input("enter your select : ")
     
     if x == "laptop":
          del margein ["laptop"] 
          truck+=3
          print("truck hight =",truck)
     
     elif x == "compiuter" :
          del margein ["compiuter"]
          truck+=17
          print("truck hight =",truck)

     elif x == "freezer" :
          del margein ["freezer"]
          truck+=500
          print("truck hight =",truck)

     elif x == "microphone" :
          del margein ["microphone"]
          truck+=1
          print("truck hight =",truck)     

     elif x == "gold" :
          del margein ["gold"]
          truck+=30
          print("truck hight =",truck)

     elif x == "tv" :
          del margein ["tv"]
          truck+=50
          print("truck hight =",truck)

     elif x == "chair" :
          del margein ["chair"]
          truck+=80
          print("truck hight =",truck)

     elif x == "carpet" :
          del margein ["carpet"]
          truck+=100
          print("truck hight =",truck)

     elif x == "desk" :
          del margein ["desk"]
          truck+=400
          print("truck hight =",truck)

     elif x == "phone" :
          del margein ["phone"]
          truck+=0.5
          print("truck hight =",truck) 

     elif x == "motorcycle" :
          del margein ["motorcycle"]
          truck+=80
          print("truck hight =",truck) 

     elif x == "bycycle" :
          del margein ["bycycle"]
          truck+=10
          print("truck hight =",truck)                   
          



