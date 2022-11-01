import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./heart_failure_clinical_records_dataset.csv')

print("Question 1")
print("-------------------------------------------------------------------------------")
print("q1: ")
print("DEATH EVENT= 0")
df_0 = data.loc[data['DEATH_EVENT'] == 0,['creatinine_phosphokinase','serum_creatinine','serum_sodium','platelets','DEATH_EVENT']]
print(df_0)
print("")
print("DEATH EVENT= 1")
df_1 = data.loc[data['DEATH_EVENT'] == 1,['creatinine_phosphokinase','serum_creatinine','serum_sodium','platelets','DEATH_EVENT']]
print(df_1)
print("=================================================================")

print("q2: ")
plt.matshow(df_0.corr())
plt.savefig("plot_of_surviving.pdf")

plt.matshow(df_1.corr())
plt.savefig("plot_of_deceased.pdf")

print("=================================================================")

print("q3: ")
print('----------------------------------------------')
print('Corr of surviving:')
print(df_0.corr())
print('----------------------------------------------')
print('Corr of deceased:')
print(df_1.corr())