import pandas as pd
import numpy as np
import math

data = pd.read_csv('./BreadBasket_DMS_output.csv')

print(
    "#################################################################################################################")
print("Q1: ")
print("==============================================================================================")

print("q(1):")
print("------------------------------------------------------------------------")
df_busiest_hr = data[['Hour', 'Transaction']]
print("The busiest hour is", df_busiest_hr.groupby('Hour').sum().stack().idxmax(),
      df_busiest_hr.groupby('Hour').sum().stack().max())
print("==============================================================================================")

print("q(2):")
print("------------------------------------------------------------------------")
df_busiest_weekday = data[['Weekday', 'Transaction']]
print("The busiest day of week is", df_busiest_weekday.groupby('Weekday').sum().stack().idxmax(),
      df_busiest_weekday.groupby('Weekday').sum().stack().max())
print("==============================================================================================")

print("q(3):")
print("------------------------------------------------------------------------")
df_busiest_Period = data[['Period', 'Transaction']]
print("The busiesr period is", df_busiest_Period.groupby('Period').sum().stack().idxmax(),
      df_busiest_Period.groupby('Period').sum().stack().max())
print(
    "#################################################################################################################")

print("Q2: ")
print("==============================================================================================")

print("q(1):")
print("------------------------------------------------------------------------")
df_temp = data[['Hour', 'Transaction', 'Item_Price']]
df_temp = df_temp.copy()
df_temp['Revenue'] = df_temp['Transaction'].mul(df_temp['Item_Price'])
df_Revenue_hr = df_temp[['Hour', 'Revenue']]
print("The most profitable hour is", df_Revenue_hr.groupby('Hour').sum().stack().idxmax(),
      df_Revenue_hr.groupby('Hour').sum().stack().max())
print("==============================================================================================")

print("q(2):")
print("------------------------------------------------------------------------")
df_temp1 = data[['Weekday', 'Transaction', 'Item_Price']]
df_temp1 = df_temp1.copy()
df_temp1['Revenue'] = df_temp1['Transaction'].mul(df_temp1['Item_Price'])
df_Revenue_dw = df_temp1[['Weekday', 'Revenue']]
print("The most profitable day of the week is", df_Revenue_dw.groupby('Weekday').sum().stack().idxmax(),
      df_Revenue_dw.groupby('Weekday').sum().stack().max())
print("==============================================================================================")

print("q(3):")
print("------------------------------------------------------------------------")
df_temp2 = data[['Period', 'Transaction', 'Item_Price']]
df_temp2 = df_temp2.copy()
df_temp2['Revenue'] = df_temp2['Transaction'].mul(df_temp2['Item_Price'])
df_Revenue_pr = df_temp2[['Period', 'Revenue']]
print("The most profitable period is", df_Revenue_pr.groupby('Period').sum().stack().idxmax(),
      df_Revenue_pr.groupby('Period').sum().stack().max())
print(
    "#################################################################################################################")

print("Q3: ")
print("------------------------------------------------------------------------")
df_item = data[['Item', 'Transaction']]
print("The most popular item is ", df_item.groupby("Item").sum().stack().idxmax(), df_item.groupby("Item").sum().max())
print()
print("The least popular item is ", df_item.groupby("Item").sum().stack().idxmin(), df_item.groupby("Item").sum().min())
print()
print(
    "#################################################################################################################")

print("Q4: ")
print("------------------------------------------------------------------------")
df_temp3 = data[['Month', 'Weekday', 'Transaction']]
df_barrista = df_temp3.groupby(["Month", "Weekday"]).sum().max() / 50
df_barrista = df_barrista.apply(lambda x: math.ceil(x))
print("The number of barristas we need is ", df_barrista)
print(
    "#################################################################################################################")

data1 = pd.read_csv('./BreadBasket_DMS_output_withGroup.csv')

print("Q5:")
print("------------------------------------------------------------------------")
df_t1 = data1.loc[data1['Groups'] != "unknown", ['Item_Price', 'Groups']]
df_gp = df_t1.groupby(['Groups']).mean()
print(df_gp)
print(
    "#################################################################################################################")

print("Q6:")
print("------------------------------------------------------------------------")
df_t2 = data1.loc[data1['Groups'] != "unknown", ['Transaction', 'Item_Price', 'Groups']]

df_t2 = df_t2.copy()
df_t2['Revenue'] = df_t2['Transaction'].mul(df_t2['Item_Price'])

df_t2_1 = df_t2[['Groups', 'Revenue']]

print("This coffee shop should make money from :", df_t2_1.groupby('Groups').sum().stack().idxmax(),
      df_t2_1.groupby('Groups').sum().max())
print(
    "#################################################################################################################")

print("Q7:")
data1['Groups'] = data1.loc[data1["Weekday"] == "Monday", "Groups"]
data1.loc[data1["Weekday"] == "Monday", "Groups"] = 'Monday'
Monday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Monday.nlargest(5))

print("===================================================================")
data1['Groups'] = data1.loc[data1["Weekday"] == "Tuesday", "Groups"]
data1.loc[data1["Weekday"] == "Tuesday", "Groups"] = 'Tuesday'
Tuesday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Tuesday.nlargest(5))

print("===================================================================")
data1['Groups'] = data1.loc[data1["Weekday"] == "Wednesday", "Groups"]
data1.loc[data1["Weekday"] == "Wednesday", "Groups"] = 'Wednesday'
Wednesday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Wednesday.nlargest(5))

print("===================================================================")
data1['Groups'] = data1.loc[data1["Weekday"] == "Thursday", "Groups"]
data1.loc[data1["Weekday"] == "Thursday", "Groups"] = 'Thursday'
Thursday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Thursday.nlargest(5))

print("===================================================================")
data1['Groups'] = data1.loc[data1["Weekday"] == "Friday", "Groups"]
data1.loc[data1["Weekday"] == "Friday", "Groups"] = 'Friday'
Friday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Friday.nlargest(5))

print("===================================================================")
data1['Groups'] = data1.loc[data1["Weekday"] == "Saturday", "Groups"]
data1.loc[data1["Weekday"] == "Saturday", "Groups"] = 'Saturday'
Saturday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Saturday.nlargest(5))

print("===================================================================")
data1['Groups'] = data1.loc[data1["Weekday"] == "Sunday", "Groups"]
data1.loc[data1["Weekday"] == "Sunday", "Groups"] = 'Sunday'
Sunday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Sunday.nlargest(5))

print(
    "#################################################################################################################")

print("Q8:")
data1['Groups'] = data1.loc[data1["Weekday"] == "Monday", "Groups"]
data1.loc[data1["Weekday"] == "Monday", "Groups"] = 'Monday'
Monday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Monday.nsmallest(5))

print("===================================================================")
data1['Groups'] = data1.loc[data1["Weekday"] == "Tuesday", "Groups"]
data1.loc[data1["Weekday"] == "Tuesday", "Groups"] = 'Tuesday'
Tuesday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Tuesday.nsmallest(5))

print("===================================================================")
data1['Groups'] = data1.loc[data1["Weekday"] == "Wednesday", "Groups"]
data1.loc[data1["Weekday"] == "Wednesday", "Groups"] = 'Wednesday'
Wednesday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Wednesday.nsmallest(5))

print("===================================================================")
data1['Groups'] = data1.loc[data1["Weekday"] == "Thursday", "Groups"]
data1.loc[data1["Weekday"] == "Thursday", "Groups"] = 'Thursday'
Thursday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Thursday.nsmallest(5))

print("===================================================================")
data1['Groups'] = data1.loc[data1["Weekday"] == "Friday", "Groups"]
data1.loc[data1["Weekday"] == "Friday", "Groups"] = 'Friday'
Friday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Friday.nsmallest(5))

print("===================================================================")
data1['Groups'] = data1.loc[data1["Weekday"] == "Saturday", "Groups"]
data1.loc[data1["Weekday"] == "Saturday", "Groups"] = 'Saturday'
Saturday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Saturday.nsmallest(5))

print("===================================================================")
data1['Groups'] = data1.loc[data1["Weekday"] == "Sunday", "Groups"]
data1.loc[data1["Weekday"] == "Sunday", "Groups"] = 'Sunday'
Sunday = data1.groupby(['Groups', 'Item']).sum(numeric_only = True)['Transaction']
print(Sunday.nsmallest(5))
print(
    "#################################################################################################################")

print("Q9")
data1['Groups'] = 'unknown'
data1.loc[data1["Item"]=="Coffee","Groups"] = 'drink'
data1.loc[data1["Item"]=="Coffee granules ","Groups"] = 'drink'
data1.loc[data1["Item"]=="Coke","Groups"] = 'drink'
data1.loc[data1["Item"]=="Hearty & Seasonal","Groups"] = 'drink'
data1.loc[data1["Item"]=="Hot chocolate","Groups"] = 'drink'
data1.loc[data1["Item"]=="Juice","Groups"] = 'drink'
data1.loc[data1["Item"]=="Mineral water","Groups"] = 'drink'
data1.loc[data1["Item"]=="My-5 Fruit Shoot","Groups"] = 'drink'
data1.loc[data1["Item"]=="Smoothies","Groups"] = 'drink'
data1.loc[data1["Item"]=="Soup","Groups"] = 'drink'
data1.loc[data1["Item"]=="Tea","Groups"] = 'drink'

drinks =sum(data1.loc[data1['Groups']=='drink']['Transaction']) / data1.sum(numeric_only = True)["Transaction"]
print("There are", drinks.round(2), "drinks per transactions")
