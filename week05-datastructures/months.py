# months.py
# Description: tuple that stores the months of thr year
#               and prints months of the season
# Author: Olga Knoutova

months = ("January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
          )
spring = months[1:4]          
summer = months[4:7]
autumn = months[7:10]
winter = months[10:12]+months[0:1]
for month in winter:
    print (month)