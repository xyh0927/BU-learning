import pandas as pd
import numpy as np
import csv

print('\n')
print('Q1:')

data = pd.read_csv("tips.csv")

tipForLunch = 0.0
tipForDinner= 0.0

sumForLunch = 0.0
sumForDinner = 0.0
for i in range(len(data)):
    if(data.loc[i,'time']) == 'Lunch':
        tipForLunch += data.loc[i,'tip']
        sumForLunch += data.loc[i, 'total_bill']
    elif(data.loc[i,'time']) == 'Dinner':
        tipForDinner += data.loc[i, 'tip']
        sumForDinner += data.loc[i, 'total_bill']
    else:
        pass


l = round(tipForLunch/sumForLunch,4)
d = round(tipForDinner/sumForDinner,4)
l1 = l*100
d1 = d*100

print("Lunch: ")
print('The average tip: %.2f' %l1 +'%')
print("---------------------------------------")
print("Dinner: ")
print('The average tip: %.2f' %d1 +'%')
print('===============================================================================================================')
print('\n')

print('Q2:')

tip_4 = 0.0
tip_5 = 0.0
tip_6 = 0.0
tip_7 = 0.0


tip_4_sum = 0.0
tip_5_sum = 0.0
tip_6_sum = 0.0
tip_7_sum = 0.0


for i in range(len(data)):
    if(data.loc[i,'day']) == 'Thur':
        tip_4 += data.loc[i,'tip']
        tip_4_sum += data.loc[i, 'total_bill']
    elif(data.loc[i,'day']) == 'Fri':
        tip_5 += data.loc[i, 'tip']
        tip_5_sum += data.loc[i, 'total_bill']
    elif (data.loc[i, 'day']) == 'Sat':
        tip_6 += data.loc[i, 'tip']
        tip_6_sum += data.loc[i, 'total_bill']
    elif (data.loc[i, 'day']) == 'Sun':
        tip_7 += data.loc[i, 'tip']
        tip_7_sum += data.loc[i, 'total_bill']
    else:
        pass




tip_4 = round(tip_4/tip_4_sum,4)
tip_5 = round(tip_5/tip_5_sum,4)
tip_6 = round(tip_6/tip_6_sum,4)
tip_7 = round(tip_7/tip_7_sum,4)

l4 = tip_4 * 100
l5 = tip_5 * 100
l6 = tip_6 * 100
l7 = tip_7 * 100

print("The Average tip:")
print("--------------------------------------")
print('Thursday: %.2f' %l4 +'%')
print('Friday: %.2f' %l5 +'%')
print('Saturday: %.2f' %l6 +'%')
print('Sunday: %.2f' %l7 +'%')

print('===============================================================================================================')
print('\n')

print('Q3:')

max_tip = 0.0
count = 0

for i in range(len(data)):
    if(data.loc[i,'tip']) > max_tip:
        max_tip = data.loc[i,'tip']
        count = i
print("The highest tips is on {}urday {}, it is {}".format(str(data.loc[count,'day']),str(data.loc[count, 'time']),str(max_tip)))

print('===============================================================================================================')
print('\n')

print('Q4:')

data2 = data[['tip','total_bill']]
print(data2.corr())


print('===============================================================================================================')
print('\n')

print('Q5:')

data3 = data[['size','tip']]
print(data3.corr())

print('===============================================================================================================')
print('\n')

print('Q6:')

count_smk = 0

count_sum = 0

data4 = data[['smoker','size']]
for i in range(len(data4)):
    if(data.loc[i,'smoker'] == 'Yes'):
        count_smk += data.loc[i,'size']
        count_sum += data.loc[i, 'size']

    elif(data.loc[i,'smoker'] == 'No'):
        count_sum += data.loc[i,'size']

print('The percentage of people are smoking : {}%'.format((round(count_smk/count_sum,5)) * 100))

print('===============================================================================================================')
print('\n')

print('Q7:')
print('assume that rows in the tips.csv file are arranged in time. The tips are not be increasing with time in each day')
print('===============================================================================================================')
print('\n')

print('Q8:')

tip_smk = 0.0
tip_nsmk = 0.0
count_nsmk = 0

for i in range(len(data4)):
    if(data.loc[i,'smoker'] == 'Yes'):
        count_smk += data.loc[i,'size']
        tip_smk += data.loc[i, 'tip']

    elif(data.loc[i,'smoker'] == 'No'):
        count_nsmk += data.loc[i,'size']
        tip_nsmk += data.loc[i, 'tip']

print("The Average tips: ")
print('For people are smoking : {} ' .format(round(tip_smk/count_smk,5)))
print('For people are not smoking : {} ' .format(round(tip_nsmk/count_nsmk,5)))
print('===============================================================================================================')
print('\n')