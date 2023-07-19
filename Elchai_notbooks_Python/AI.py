# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:07:29 2022

@author: Elchai Refoua
"""
#importent


#REGRESIA LINARIT- קו מודל שמחבר את הנקודות

#data set y=mx+n. n=chitooch, m=shipoooa

# summin=(yi-yi')^2 את זה הפייתון עושה 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#matlotlib inline 

df=pd.read_csv('cars.csv')
df=pd.DataFrame()

#df=pd.read_csv('cars.csv', usecols=[price])

data= pd.read_csv('linear_regression_ds.csv')
data
#: לוקח את כל השורות ובוחר איזה עמודות
x=data.iloc[:,:-1].values
#כל העמודות פחות העמודה האחרונה
#ואליוס זה מספרים

y=data.iloc[:,1].values
#לוקח את העמודה השנייה כלומר מספר 1 מאפס
#יש 30 נקודות מידע ורוצים מתוכם חלק לבנות ולאמן מודל ולבחון את המודל

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=1/3,random_state=0)
#random=0 זה אומר רנדום זהה למתרגל
#train=20, test=10
#פיצלנו את השתנים ל2 סטים אחד של אימון מודל ואחד בחינה אחרי אימון ובנייה

x_train
y_train
y_test
x_test

#building model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

#object oreinted מונחה עצמים
#מייצגים אובייקטים או יישות מסוימת מהעולם האמיתי על ידי קוד 
#לאובייקט יש גם תכונות וגם שיטות\אופרציות התנהגויות 
#לדוגמא למסך יש תכונות ושיטות ועל ידם מיוצג
#תכונות:שחור אפור או לבן-צבע
#תכונה:צבע: 4K או HD
#שיטות אופרציות התנגויות: כיבוי הדלקה, עוצמת קול, בהירות,
#מתאר אובייקטים מהעולם האמיתי על ידי קוד
#מכונית:צבע, גודל מספר מקומות ישיבה מספ חלונות זה תכונות
#שיטות להדליק אורות לכבות ליסוע, לתת ברקס או גז
#אוסף התכונות והשיטות של האובייקט נקרא אובייקט עצמו
#CLASS המקום שבו נמצאים כל התכונות והשיטות הוראות ההכנה של האובייקט
#תכונות
#שיטות
#ליצור אובייקט מהקלסא אני יורש ממנו תכונות ושיטות
#מCLASS
#FIT זה דוגמא דשיטה של רגרסיה לינאירת ולהתאים את הקו
#מכניס את הנקודות של האימון כדי להגיע כנאמר לרגרסייה לסכום הטעויות הקטן ביותר
#בנינו מודל מובנה מבוסס בינה מלאכותית
#נציג מודל על גרף
#יוצר איור שזה פיגר ואז סקטר זה פיזור של המודל של הנקודות
#עם מודל של רגרסיה של ניבוי

import matplotlib.pyplot as plt
plt.figure()
plt.scatter(x_train,y_train,color='blue')
plt.plot(x_train,regressor.predict(x_train),color='red')
plt.title('linear regression model vs. dataset')
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.show()
 

#בנינו את המודל מ20 נקודות של טריין 
#ועכשיו נוכל לנבא אם נביא את המשתנה הבלתי תלוי מה יהיה המשתנה התלוי
#נעשה את המודל עבור הטסט סט נעתיק את הקוד עבור הטריינינג
#עכשיו רואים את המודל מול דטא שלא נבנה איתו שזה הטסט סט שלנו כי בנינו טריינינג ואז על דטא שלא ראה מעולם ורואים שיש התאמה טובה
#לתקן את Text(0, 0.5, 'salary')
# להוסיף שורה של 


plt.figure()
plt.scatter(x_test,y_test,color='blue')
plt.plot(x_test,regressor.predict(x_test),color='red')
plt.title('linear regression model vs. dataset')
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.show()


#moltipiple linear regression רגרסייה לינארית מרובה
#יש מספר משתנים בלתי תלויים גדול מאחד
#y=m1x1+m2x2+......mixi
#חוץ משנות נסיון גם ידע בשפות יכול להשפיע על השכר 
#תלת מימד
#הופכים משתנה בלתי תלוי במילים למספרים 
#משתני דמה - dummy variables
 #משתנה תלוי יש אחד#
#משתנה בלתי תלוי יש כמה #
#נייבא תיקיות פנדה ונאמפאי חבילה שיודעת לעבוד עם ערכים 

import pandas as pd
import numpy as np

data= pd.read_csv()










