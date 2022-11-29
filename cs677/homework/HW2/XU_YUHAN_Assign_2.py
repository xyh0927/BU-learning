import pandas as pd

data = pd.read_csv('./ds_salaries.csv')

print("Q2:")
print("------------------------------------------------------------------------------------------")
df_SalarOf2020 = data.loc[data['work_year'] == 2020, ['salary_in_usd', 'work_year']]
df_SalarOf2020.loc['In 2020, the Average Salary is'] = df_SalarOf2020.apply(lambda x: x.mean())
df_SalarOf2021 = data.loc[data['work_year'] == 2021, ['salary_in_usd', 'work_year']]
df_SalarOf2021.loc['In 2021, the Average Salary is'] = df_SalarOf2021.apply(lambda x: x.mean())
df_SalarOf2022 = data.loc[data['work_year'] == 2022, ['salary_in_usd', 'work_year']]
df_SalarOf2022.loc['In 2022, the Average Salary is'] = df_SalarOf2022.apply(lambda x: x.mean())

df_MeanSalaryByYear = pd.concat([df_SalarOf2020.tail(1), df_SalarOf2021.tail(1), df_SalarOf2022.tail(1)])
print(df_MeanSalaryByYear)
print("###############################################################################################################################\n")

print("Q3:")
print("------------------------------------------------------------------------------------------")

df_SalarOf2020 = data.loc[data['work_year'] == 2020, ['work_year', 'salary_in_usd']]
df_SalarOf2020.loc['MeanSalary_2020'] = df_SalarOf2020.apply(lambda x: x.mean())
df_SalarOf2021 = data.loc[data['work_year'] == 2021, ['work_year', 'salary_in_usd']]
df_SalarOf2021.loc['MeanSalary_2021'] = df_SalarOf2021.apply(lambda x: x.mean())
df_SalarOf2022 = data.loc[data['work_year'] == 2022, ['work_year', 'salary_in_usd']]
df_SalarOf2022.loc['MeanSalary_2020'] = df_SalarOf2022.apply(lambda x: x.mean())

df_MeanSalaryByYear = pd.concat([df_SalarOf2020.tail(1), df_SalarOf2021.tail(1), df_SalarOf2022.tail(1)])

df_MeanSalaryByYear.loc['The highest salary year is'] = df_MeanSalaryByYear.apply((lambda x: x.max()))
print(df_MeanSalaryByYear.tail(1))
df_MeanSalaryByYear.loc['The lowest salary year is'] = df_MeanSalaryByYear.apply((lambda x: x.min()))
print(df_MeanSalaryByYear.tail(1))
print("###############################################################################################################################\n")

print("Q4:")
print("------------------------------------------------------------------------------------------")

print("The mean Salary of each Job Title with EN Entry-level: ")
df_SalaryByJT_EN = data.loc[data['experience_level'] == 'EN', ['salary_in_usd', 'job_title', 'experience_level']]
print(df_SalaryByJT_EN.groupby('job_title').mean(), "\n")
print("The mean Salary of each Job Title with Junior MI Mid-level: ")
df_SalaryByJT_MI = data.loc[data['experience_level'] == 'MI', ['salary_in_usd', 'job_title', 'experience_level']]
print(df_SalaryByJT_MI.groupby('job_title').mean(), "\n")
print("The mean Salary of each Job Title with Intermediate SE Senior-level: ")
df_SalaryByJT_SE = data.loc[data['experience_level'] == 'SE', ['salary_in_usd', 'job_title', 'experience_level']]
print(df_SalaryByJT_SE.groupby('job_title').mean(), "\n")
print("The mean Salary of each Job Title with Expert EX Executive-level: ")
df_SalaryByJT_EX = data.loc[data['experience_level'] == 'EX', ['salary_in_usd', 'job_title', 'experience_level']]
print(df_SalaryByJT_EX.groupby('job_title').mean())
print("###############################################################################################################################\n")

print("Q5:")
print("------------------------------------------------------------------------------------------")

df_SalaryByJT = data[['salary_in_usd', 'job_title']]
df_MeanSalaryByJT = df_SalaryByJT.groupby('job_title').mean()
print("The Job Title of the maximum Average Salary is", df_MeanSalaryByJT.stack().idxmax(), df_MeanSalaryByJT.stack().max())
print("The Job Title of the minimum Average Salary is", df_MeanSalaryByJT.stack().idxmin(), df_MeanSalaryByJT.stack().min())
print("###############################################################################################################################\n")

print("Q6:")
print("------------------------------------------------------------------------------------------")

df_SalaryByJT_2020 = data.loc[data['work_year'] == 2020, ['salary_in_usd', 'job_title']]
print("The Annual Salary for each job title in 2020:\n", df_SalaryByJT_2020.groupby('job_title').sum(), "\n")
df_SalaryByJT_2021 = data.loc[data['work_year'] == 2021, ['salary_in_usd', 'job_title']]
print("The Annual Salary for each job title in 2021:\n", df_SalaryByJT_2021.groupby('job_title').sum(), "\n")
df_SalaryByJT_2022 = data.loc[data['work_year'] == 2022, ['salary_in_usd', 'job_title']]
print("The Annual Salary for each job title in 2022:\n", df_SalaryByJT_2022.groupby('job_title').sum(), "\n")
print("###############################################################################################################################\n")

print("Q7:")
print("------------------------------------------------------------------------------------------")

df_SalaryByJT_2020 = data.loc[data['work_year'] == 2020, ['salary_in_usd', 'job_title']]
df_MeanSalaryByJT_2020 = df_SalaryByJT_2020.groupby('job_title').mean()
df_SalaryByJT_2021 = data.loc[data['work_year'] == 2021, ['salary_in_usd', 'job_title']]
df_MeanSalaryByJT_2021 = df_SalaryByJT_2021.groupby('job_title').mean()
dict = {
    'salary_in_usd': 'salary_in_usd_2021'
}
df_MeanSalaryByJT_2021.rename(columns= dict, inplace= True)
df_SalaryByJT_2022 = data.loc[data['work_year'] == 2022, ['salary_in_usd', 'job_title']]
df_MeanSalaryByJT_2022 = df_SalaryByJT_2022.groupby('job_title').mean()
dict = {
    'salary_in_usd': 'salary_in_usd_2022'
}
df_MeanSalaryByJT_2022.rename(columns= dict, inplace= True)
df_tmp = pd.concat([df_MeanSalaryByJT_2020, df_MeanSalaryByJT_2021, df_MeanSalaryByJT_2022], axis = 1)
df_tmp = df_tmp.fillna(0)
df_tmp["ChangeSalary(20-22)"] = df_tmp.apply(lambda x: abs(x['salary_in_usd_2022'] - x['salary_in_usd']), axis = 1)
df_ChangeMeanSalary20to22 = df_tmp['ChangeSalary(20-22)']
print(df_ChangeMeanSalary20to22.idxmin(), "Experienced minimum Salary Change")
print(df_ChangeMeanSalary20to22.idxmax(), "Experienced maximum Salary Change")

print("###############################################################################################################################\n")

print("Q8:")
print("------------------------------------------------------------------------------------------")

print("The Average Salaries For Each Remote Ratio are listed below:")
df_SalaryByRR = data[['salary_in_usd', 'remote_ratio']]
df_MeanSalaryByRR = df_SalaryByRR.groupby('remote_ratio').mean()
df_SalaryByRR_R0 = data.loc[data['remote_ratio'] == 0, ['salary_in_usd', 'remote_ratio']]
df_SalaryByRR_R50 = data.loc[data['remote_ratio'] == 50, ['salary_in_usd', 'remote_ratio']]
df_SalaryByRR_Rf = data.loc[data['remote_ratio'] == 100, ['salary_in_usd', 'remote_ratio']]
print(df_MeanSalaryByRR, "\n")
print("The entries for Remote Ration 0 is", df_SalaryByRR_R0.shape[0])
print("The entries for Remote Ration 50 is", df_SalaryByRR_R50.shape[0])
print("The entries for Remote Ration 100 is", df_SalaryByRR_Rf.shape[0])

print("###############################################################################################################################\n")

print("Q9:")
print("------------------------------------------------------------------------------------------")

df_SalaryByLoc = data[['salary_in_usd', 'company_location']]
df_MeanSalaryByLoc = df_SalaryByLoc.groupby('company_location').mean()

print("The Location where pays the hightest Salary is: ", df_MeanSalaryByLoc.stack().idxmax(), df_MeanSalaryByLoc.max())
print()
print("The Location where pays the lowest Salary is: ", df_MeanSalaryByLoc.stack().idxmin(), df_MeanSalaryByLoc.min())

print("###############################################################################################################################\n")

print("Q10:")
print("------------------------------------------------------------------------------------------")

print("Q: Would you change your resume after analyzing this dataset?")
print("----------------------------------------------------------------")
print("     My Answer: Yes, I would")

print("###############################################################################################################################")