import csv

job_title_rpt = []
job_title = []

num_2020 = 0
num_2021 = 0
num_2022 = 0
sumSalary_2020 = 0
sumSalary_2021 = 0
sumSalary_2022 = 0

num = 0
order = 0
AveSalaryByjt = []

with open(r'ds_salaries.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)

    for row in reader:
        job_title_rpt.append(row[4])

    for i in job_title_rpt:
        if i not in job_title:
            job_title.append(i)

    lenth = len(job_title)

for i in range(len(job_title)):
    print(job_title[i])
    jt = job_title[i]
    order = 0
    num_2020 = 0
    num_2021 = 0
    num_2022 = 0
    sumSalary_2020 = 0
    sumSalary_2021 = 0
    sumSalary_2022 = 0
    with open(r'ds_salaries.csv') as f:
        readerx = csv.reader(f)
        headers = next(readerx)

        for row in readerx:
            order += 1
            j = row[4]
            if j == jt and row[1] == "2020":
                num_2020 += 1
                sumSalary_2020 += int(row[5])
            elif j == jt and row[1] == "2021":
                num_2021 += 1
                sumSalary_2021 += int(row[5])
            elif j == jt and row[1] == "2022":
                num_2022 += 1
                sumSalary_2022 += int(row[5])
            elif order == 607:
                break
            else:
                continue

        i += 1
    print("2020 Annual Salary is : ", sumSalary_2020)
    print("2021 Annual Salary is : ", sumSalary_2021)
    print("2022 Annual Salary is : ", sumSalary_2022)