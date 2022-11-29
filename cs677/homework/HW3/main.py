import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./world_population.csv")

########################################################################################################################################################################################################

print("Q2: \n===========================================================================================================")
df_2020to1970 = data[['Country', '2020 Population', '1970 Population']]
df_2020to1970=df_2020to1970.copy()
df_2020to1970['Annual Growth Rate'] = df_2020to1970.apply(lambda x: ((x['2020 Population']/x['1970 Population'])**(1/5))-1, axis = 1)
df_2020to1970['Annual Growth Rate(%)'] = df_2020to1970['Annual Growth Rate'].apply(lambda x:format(x, '.2%'))
print(df_2020to1970)
print("The Top 5 Country with highest Annual Growth Rate\n-----------------------------------------------------------------------\n", df_2020to1970.nlargest(5, "Annual Growth Rate" ), "\n")
print("The Top 5 Country with lowest Annual Growth Rate\n-----------------------------------------------------------------------\n", df_2020to1970.nsmallest(5, "Annual Growth Rate" ))
print()
print("#####################################################################################################################")

print("Q3: \n===========================================================================================================")
df_2020to2010 = data[['Country', '2020 Population', '2010 Population']]
df_2020to2010=df_2020to2010.copy()
df_2020to2010['Annual Growth Rate'] = df_2020to2010.apply(lambda x: ((x['2020 Population']/x['2010 Population']))-1, axis = 1)
df_2020to2010['Annual Growth Rate(%)'] = df_2020to2010['Annual Growth Rate'].apply(lambda x:format(x, '.2%'))
print(df_2020to2010)
print("The Top 5 Country with highest Annual Growth Rate\n-----------------------------------------------------------------------\n", df_2020to2010.nlargest(5, "Annual Growth Rate" ), "\n")
print("The Top 5 Country with lowest Annual Growth Rate\n-----------------------------------------------------------------------\n", df_2020to2010.nsmallest(5, "Annual Growth Rate" ))
print("The 5 Countries which have the highest Annual Growth Rate or the lowest Annual Growth Rate are different with previous Question")
print()
print("#####################################################################################################################")

print("Q4: \n===========================================================================================================")
df_2020population = data[['Country', '2020 Population']]
print("The Top 5 Country with highest Population in 2020\n-----------------------------------------------------------------------\n", df_2020population.nlargest(5, "2020 Population" ), "\n")
print("The Top 5 Country with lowest Population in 2020\n-----------------------------------------------------------------------\n", df_2020population.nsmallest(5, "2020 Population" ))
print()
print("#####################################################################################################################")

print("Q5: \n===========================================================================================================")
df_1970population = data[['Country', '1970 Population']]
print("The Top 5 Country with highest Population in 1970\n-----------------------------------------------------------------------\n", df_1970population.nlargest(5, "1970 Population"), "\n")
print("The Top 5 Country with lowest Population in 1970\n-----------------------------------------------------------------------\n", df_1970population.nsmallest(5, "1970 Population"))
print()
df_2022population = data[['Country', '2022 Population']]
print("The Top 5 Country with highest Population in 2022\n-----------------------------------------------------------------------\n", df_2022population.nlargest(5, "2022 Population"), "\n")
print("The Top 5 Country with lowest Population in 2022\n-----------------------------------------------------------------------\n", df_2022population.nsmallest(5, "2022 Population"))
print()
print("In 2022, In top 5 country with highest Population, \n China;\n India;\n United States;\n Indonesia;\n Remain in the list")
print("In 2022, In top 5 country with lowest Population, \n Vatican City;\n Tokelau;\n Niue;\n Falkland Islands;\n Remain in the list")
print()
print("#####################################################################################################################")

print("Q6: \n===========================================================================================================")
df_2020pop = data[['Country', '2020 Population']]
print("Mean µ: ", df_2020pop['2020 Population'].mean())
print("Q1(25%): ", df_2020pop['2020 Population'].quantile(.25))
print("Q2(M): ", df_2020pop['2020 Population'].quantile(.5))
print("Q3(75%): ", df_2020pop['2020 Population'].quantile(.75))

print()
print("#####################################################################################################################")

print("Q7: \n===========================================================================================================")
print("Bahamas,Guadeloupe and Brunei are around Q1")
print("Finland,Slovakia and Lebanon are around Q2(Median)")
print("Mali, Burkina Faso and Sri Lanka are around Q3")
print("Angola, Uzbekistan and Saudi Arabia are around Mean µ")
print()
print("#####################################################################################################################")

print("Q8: \n===========================================================================================================")

"""1980"""
df_1980Pop = data[['CCA3', 'Country', '1980 Population']]
QuantileQ1_1980 = df_1980Pop['1980 Population'].quantile(.25)
QuantileQ3_1980 = df_1980Pop['1980 Population'].quantile(.75)
df_q11980q3 =df_1980Pop[(df_1980Pop['1980 Population'] >= QuantileQ1_1980) & (df_1980Pop['1980 Population'] <= QuantileQ3_1980)]

plt.tick_params(axis='x', labelsize=2)
plt.bar(df_q11980q3['Country'], df_q11980q3['1980 Population'],color = ['r'])
plt.xticks(rotation=-90)
plt.savefig('1980_Population_graph.pdf')
plt.figure()

"""1990"""
df_1990Pop = data[['CCA3', 'Country', '1990 Population']]
QuantileQ1_1990 = df_1990Pop['1990 Population'].quantile(.25)
QuantileQ3_1990 = df_1990Pop['1990 Population'].quantile(.75)
df_q11990q3 =df_1990Pop[(df_1990Pop['1990 Population'] >= QuantileQ1_1990) & (df_1990Pop['1990 Population'] <= QuantileQ3_1990)]

plt.tick_params(axis='x', labelsize=2)
plt.bar(df_q11990q3['Country'], df_q11990q3['1990 Population'],color = ['black'])
plt.xticks(rotation=-90)
plt.savefig('1990_Population_graph.pdf')
plt.figure()


"""2000"""
df_2000Pop = data[['CCA3', 'Country', '2000 Population']]
QuantileQ1_2000 = df_2000Pop['2000 Population'].quantile(.25)
QuantileQ3_2000 = df_2000Pop['2000 Population'].quantile(.75)
df_q12000q3 =df_2000Pop[(df_2000Pop['2000 Population'] >= QuantileQ1_2000) & (df_2000Pop['2000 Population'] <= QuantileQ3_2000)]

plt.tick_params(axis='x', labelsize=2)
plt.bar(df_q12000q3['Country'], df_q12000q3['2000 Population'],color = ['cyan'])
plt.xticks(rotation=-90)
plt.savefig('2000_Population_graph.pdf')
plt.figure()

"""2010"""
df_2010Pop = data[['CCA3', 'Country', '2010 Population']]
QuantileQ1_2010 = df_2010Pop['2010 Population'].quantile(.25)
QuantileQ3_2010 = df_2010Pop['2010 Population'].quantile(.75)
df_q12010q3 =df_2010Pop[(df_2010Pop['2010 Population'] >= QuantileQ1_2010) & (df_2010Pop['2010 Population'] <= QuantileQ3_2010)]

plt.tick_params(axis='x', labelsize=2)
plt.bar(df_q12010q3['Country'], df_q12010q3['2010 Population'],color = ['b'])
plt.xticks(rotation=-90)
plt.savefig('2010_Population_graph.pdf')
plt.figure()

"""2020"""
df_2020Pop = data[['CCA3', 'Country', '2020 Population']]
QuantileQ1_2020 = df_2020Pop['2020 Population'].quantile(.25)
QuantileQ3_2020 = df_2020Pop['2020 Population'].quantile(.75)
df_q12020q3 =df_2020Pop[(df_2020Pop['2020 Population'] >= QuantileQ1_2020) & (df_2020Pop['2020 Population'] <= QuantileQ3_2020)]

plt.tick_params(axis='x', labelsize=2)
plt.bar(df_q12020q3['Country'], df_q12020q3['2020 Population'],color = ['g'])
plt.xticks(rotation=-90)
plt.savefig('2020_Population_graph.pdf')
plt.figure()

print("Histograms Output Successfully!!!")

print()
print("#####################################################################################################################")

print("Q9: \n===========================================================================================================")
print("Question: Any interesting observations?")
print("-------------------------------------------------------------------")
print("   My Answer: Yes, in 5 Histograms, there are several countries \n"
      "that have been high columns in these 5 tables, with populations higher than Q1 and Q3, \n"
      "and several countries have been maintained low columns, with populations lower than Q1 ")
print()
print("#####################################################################################################################")

print("Q10: \n===========================================================================================================")

print("The Rank of Population density:\n ------------------------------------------------------------------------------- ")
df_density = data[['Country', 'Density (per km²)']]

df_density = df_density.copy()

df_density['Rank'] = df_density['Density (per km²)'].rank()
df_density.sort_values("Rank", inplace = True, ascending=True)

print(df_density)


print()
print("#####################################################################################################################")

print("Q11: \n===========================================================================================================")

df_1970and2020Pop = data[['Country', '1970 Population', '2020 Population']]
df_1970and2020Pop = df_1970and2020Pop.copy()

df_1970and2020Pop['1970 Population Rank'] = df_1970and2020Pop['1970 Population'].rank()
df_1970and2020Pop.sort_values("1970 Population Rank", inplace = True, ascending=True)

print("The Rank of Countries (By Population) in 1970: \n ----------------------------------------------------------------------------")
print(df_1970and2020Pop)

df_1970and2020Pop['2020 Population Rank'] = df_1970and2020Pop['2020 Population'].rank()

df_1970and2020Pop['RankChange'] = df_1970and2020Pop.apply(lambda x: x['2020 Population Rank'] - x['1970 Population Rank'], axis = 1)
print('The Top 5 Countries which have the largest Positive Rank Change from 1970 to 2020\n------------------------------------------------------------------------------\n',
      df_1970and2020Pop.nlargest(5, 'RankChange'))
print('The Top 5 Countries which have the largest Negative Rank Change from 1970 to 2020\n------------------------------------------------------------------------------\n',
      df_1970and2020Pop.nsmallest(5, 'RankChange'))

print()
print("#####################################################################################################################")

print("Q12: \n===========================================================================================================")

df_2020pop = df_2020pop.copy()

df_2020pop['1ST DIGIT'] = df_2020pop['2020 Population'].astype(str).str[0].astype(int)
print(df_2020pop)

df_firstDigit_percentage = df_2020pop['1ST DIGIT'].value_counts()/234
df_firstDigit_percentage= df_firstDigit_percentage.apply(lambda x:format(x, '.3%'))
print(df_firstDigit_percentage)