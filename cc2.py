import csv
f=open("restaurantsa9126b3.csv","r")
for row in f:
    print(row[0].read())