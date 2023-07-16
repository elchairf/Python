# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:52:57 2022

@author: Elchai Refoua
"""
#Numpy :multi-dimensional array מערך רב ממדי
#Pandas : Data analysis library- data frame- two dimensional data structure similar to excel spreadsheet rows an columns 
#MatplotLib : two dimensional plotting library for creating graphs and plots
#scikit-Learn : popular machine learning librariesprovides common algorithms: decision trees neural networks... 
#jupiter
#kaggle Video Game Sales



import pandas as pd
from matplotlib import pyplot as plt

#1 leaner

x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]
w = [4,5,3]
plt.plot(x, y)
plt.plot(x, z)
plt.plot(x,w)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z and w")
plt.legend(["this is y", "this is z"])
plt.show()

#2 

#file = open(r'C:\Users\User\Desktop\dests.txt')
sample_data = pd.read_csv(r'C:\Users\User\Desktop\sample_data.csv')
sample_data
type(sample_data)
sample_data.column_c
type(sample_data.column_c)
#כדי לקבל עמודה ושורה מסוימת
sample_data.column_c.iloc[1]
type(sample_data.column_c.iloc[1])

#בכדי לעשות פלט איקס A וואי זה B

plt.plot(sample_data.column_a,sample_data.column_b)


plt.plot(sample_data.column_a,sample_data.column_c,'o')
plt.show()

#אם נריץ ביחד זה מה שיצא
# o- נקודות

#ניתוח אמיתי
@מדינות

data = pd.read_csv(r'C:\Users\User\Desktop\countries.csv')



data
data.shape
data.describe()

#להשוות הגילוי אוכלוסיה בין ארהב וסין וצריך לבודד
us=data[data.country=='United States']
data.country=='United States'
כותב מתי זה אמת#
us

china=data[data.country=='China']
data.country=='China'
#כנל
china
#נשווה את קצב גידול האוכלוסיה

plt.plot(us.year,us.population)
plt.plot(china.year,china.population)
plt.legend(['United States','China'])#עושה הסברים
plt.ylabel('population')
plt.xlabel('year')

#להשוות מספרית
#השואה מספרית

us.population
לתת את השנה הראשונה אוכלוסייה של ארהב#
us.population.iloc[0]
#157553000
#זה הפופיוליישן השראשוני ואז נחלק כך
usgrouth=(us.population/157553000)*100

new
#בכמה האוכלוסייה גדלה באחוזים
#plt.plot(us.year,us.population)
plt.plot(us.year,usgrouth)

china.population
china.population.iloc[0]
#556263527
chinagrouth=(china.population/556263527)*100
#plt.plot(us.year,us.population)

plt.plot(china.year,chinagrouth)


plt.legend(['United States','China'])#עושה הסברים
plt.ylabel('population growth in %')
plt.xlabel('year')

#יפה
