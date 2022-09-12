import csv

########################################################################################################################
# Variable Part

data = []

AverageSalaryByYear = []
Year = ["2020", "2021", "2022"]
romote_ratio = ["0", "50", "100"]

numfor2020 = 0
sumSalaryfor2020 = 0
AverageSalaryfor2020 = 0

numfor2021 = 0
sumSalaryfor2021 = 0
AverageSalaryfor2021 = 0

numfor2022 = 0
sumSalaryfor2022 = 0
AverageSalaryfor2022 = 0

MIN_averageSalarybyYear = 0
MAX_averageSalarybyYear = 0

sumSalaryForEN = 0
AverageSalaryForEN = 0

job_title_rpt = []
job_title = []
AveSalaryByjt = []

num_EN = 0
num_MI = 0
num_SE = 0
num_EX = 0
sumSalary_EN = 0
sumSalary_MI = 0
sumSalary_SE = 0
sumSalary_EX = 0
sumSalary = 0
num = 0
order = 0
maxAveSalaryByJT = 0
minAveSalaryByJT = 0
index_maxAveSalaryByJT = 0
index_minAveSalaryByJT = 0

num_2020 = 0
num_2021 = 0
num_2022 = 0
sumSalary_2020 = 0
sumSalary_2021 = 0
sumSalary_2022 = 0

cgSalaryByjt = []
changeSalary = 0

minChange = 0
maxChange = 0
index_minCg = 0
index_maxCg = 0

numforR0 = 0
numforR50 = 0
numforRF = 0

sumSalary_RO = 0
sumSalary_R50 = 0
sumSalary_RF = 0

########################################################################################################################
# File Read Part for Q2 and Q3

with open(r'ds_salaries.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)

    for row in reader:
        if row[1] == '2020':
            numfor2020 += 1
            sumSalaryfor2020 += int(row[5])
        elif row[1] == '2021':
            numfor2021 += 1
            sumSalaryfor2021 += int(row[5])
        elif row[1] == '2022':
            numfor2022 += 1
            sumSalaryfor2022 += int(row[5])
        elif row[9] == "0":
            numforR0 += 1
            sumSalary_RO += int(row[5])
        elif row[9] == "50":
            numforR50 += 1
            sumSalary_R50 += int(row(5))
        elif row[9] == "100":
            numforRF += 1
            sumSalary_RF += int(row(5))
        else:
            break

    for i in job_title_rpt:
        if i not in job_title:
            job_title.append(i)

########################################################################################################################
# Analysis Part for Q2 Q3
AverageSalaryfor2020 = sumSalaryfor2020 / numfor2020
AverageSalaryfor2021 = sumSalaryfor2021 / numfor2021
AverageSalaryfor2022 = sumSalaryfor2022 / numfor2022

AverageSalaryByYear.append(AverageSalaryfor2020)
AverageSalaryByYear.append(AverageSalaryfor2021)
AverageSalaryByYear.append(AverageSalaryfor2022)

MAX_averageSalarybyYear = max(AverageSalaryByYear)
maxAverageSalaryByYearIndex = AverageSalaryByYear.index(MAX_averageSalarybyYear)
MaxAverageSalaryYear = Year[maxAverageSalaryByYearIndex]

MIN_averageSalarybyYear = min(AverageSalaryByYear)
minAverageSalaryByYearIndex = AverageSalaryByYear.index(MIN_averageSalarybyYear)
MinAverageSalaryYear = Year[minAverageSalaryByYearIndex]

print("Q2:\n In 2020, the Average Salary is ", AverageSalaryfor2020,
      "\n In 2021, the Average Salary is ", AverageSalaryfor2021,
      "\n In 2022, the Average Salary is ", AverageSalaryfor2022)
print(
    "################################################################################################################")
print()
print("Q3:\n The highest salary year is : ", MaxAverageSalaryYear,
      "\n The lowest salary year is : ", MinAverageSalaryYear)
print(
    "################################################################################################################")

########################################################################################################################
# File Read Part for Q4
print("\nQ4: ")
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
        jt = job_title[i]
        order = 0
        num_EN = 0
        num_MI = 0
        num_SE = 0
        num_EX = 0
        sumSalary_EN = 0
        sumSalary_MI = 0
        sumSalary_SE = 0
        sumSalary_EX = 0
        with open(r'ds_salaries.csv') as f:
            readerx = csv.reader(f)
            headers = next(readerx)

            for row in readerx:
                order += 1
                j = row[4]
                if j == jt and row[2] == "EN":
                    num_EN += 1
                    sumSalary_EN += int(row[5])
                elif j == jt and row[2] == "MI":
                    num_MI += 1
                    sumSalary_MI += int(row[5])
                elif j == jt and row[2] == "SE":
                    num_SE += 1
                    sumSalary_SE += int(row[5])
                elif j == jt and row[2] == "EX":
                    num_EX += 1
                    sumSalary_EX += int(row[5])
                elif order == 607:
                    break
                else:
                    continue

############################################################################################################################
##### Analysis Part for Q4
            if num_EN == 0:
                print("The Average Salary of ", jt, "with Entry-Level is ", 0)
            else:
                print("The Average Salary of ", jt, "with Entry-Level is ", (sumSalary_EN / num_EN))
            if num_MI == 0:
                print("The Average Salary of ", jt, "with Mid-Level is ", 0)
            else:
                print("The Average Salary of ", jt, "with Mid-Level is ", (sumSalary_MI / num_MI))
            if num_SE == 0:
                print("The Average Salary of ", jt, "with Senior-Level is ", 0)
            else:
                print("The Average Salary of ", jt, "with Senior-Level is ", (sumSalary_SE / num_SE))
            if num_EX == 0:
                print("The Average Salary of ", jt, "with Executive-Level is ", 0)
            else:
                print("The Average Salary of ", jt, "with Executive-Level is ", (sumSalary_EX / num_EX))

            print()
            i += 1
print(
    "################################################################################################################")

########################################################################################################################
# File Read Part for Q5
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
        jt = job_title[i]
        order = 0
        num = 0
        sumSalary = 0
        with open(r'ds_salaries.csv') as f:
            readerx = csv.reader(f)
            headers = next(readerx)

            for row in readerx:
                order += 1
                j = row[4]
                if j == jt:
                    num += 1
                    sumSalary += int(row[5])
                elif order == 607:
                    break
                else:
                    continue
            AveSalaryByjt.append(sumSalary / num)
            i += 1

############################################################################################################################
##### Analysis Part for Q5
    minAveSalaryByJT = min(AveSalaryByjt)
    index_minAveSalaryByJT = AveSalaryByjt.index(minAveSalaryByJT)
    MinAveSalaryJT = job_title[index_minAveSalaryByJT]

    maxAveSalaryByJT = max(AveSalaryByjt)
    index_maxAveSalaryByJT = AveSalaryByjt.index(maxAveSalaryByJT)
    MaxAveSalaryJT = job_title[index_maxAveSalaryByJT]

    print()
    print("Q5:")
    print("The Job Title of the maximum Average Salary is : ", MaxAveSalaryJT, maxAveSalaryByJT)
    print("The Job Title of the minimum Average Salary is : ", MinAveSalaryJT, minAveSalaryByJT)
print(
    "################################################################################################################")
print()

########################################################################################################################
# File Read Part for Q6
print("Q6:")

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
    print("--------------------------")
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

############################################################################################################################
##### Analysis Part for Q6

    print("   2020 Annual Salary is : ", sumSalary_2020)
    print("   2021 Annual Salary is : ", sumSalary_2021)
    print("   2022 Annual Salary is : ", sumSalary_2022)
    print()

print(
    "################################################################################################################")
print()

########################################################################################################################
# File Read Part for Q7

print("Q7: ")
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
        jt = job_title[i]
        order = 0
        num = 0
        changeSalary = 0
        with open(r'ds_salaries.csv') as f:
            readerx = csv.reader(f)
            headers = next(readerx)

            for row in readerx:
                order += 1
                j = row[4]
                if j == jt:
                    num += 1
                    changeSalary += int(row[7]) - int(row[5])

                elif order == 607:
                    break
                else:
                    continue
            cgSalaryByjt.append(abs(changeSalary))
            i += 1

############################################################################################################################
##### Analysis Part for Q7

minChange = min(cgSalaryByjt)

maxChange = max(cgSalaryByjt)

numMIN = 0
numMAX = 0
min_index = []
max_index = []

minCgJT = []
maxCgJT = []

for i in range(len(cgSalaryByjt)):
    if cgSalaryByjt[i] == minChange:
        min_index.append(i)
    elif cgSalaryByjt[i] == maxChange:
        max_index.append(i)
    else:
        continue

for i in range(len(min_index)):
    minCgJT.append(job_title[min_index[i]])
print("   ", minCgJT, "Experienced minimum Salary Change\n")

for i in range(len(max_index)):
    maxCgJT.append(job_title[max_index[i]])
print("   ", maxCgJT, "Experienced maximum Salary Change")
print(
    "################################################################################################################")
print()

########################################################################################################################
# File Read Part for Q7

with open(r'ds_salaries.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)

    for row in reader:
        if row[9] == "0":
            numforR0 += 1
            sumSalary_RO += int(row[5])
        elif row[9] == "50":
            numforR50 += 1
            sumSalary_R50 += int(row[5])
        elif row[9] == "100":
            numforRF += 1
            sumSalary_RF += int(row[5])
        else:
            break

############################################################################################################################
##### Analysis Part for Q8

print("Q8:")
print("   The Average Salary for Ratio 0 is: ", sumSalary_RO/numforR0)
print("   The Entries for Ratio 0 is: ", numforR0)
print("   The Average Salary for Ratio 50 is: ", sumSalary_R50/numforR50)
print("   The Entries for Ratio 50 is: ", numforR50)
print("   The Average Salary for Ratio 100 is: ", sumSalary_RF/numforRF)
print("   The Entries for Ratio 0 is: ", numforRF)
print(
    "################################################################################################################")
print()

########################################################################################################################
# File Read Part for Q9

cp_loc = []
cp_location = []
AverageSalaryByLoc = []

print("Q9: ")
with open(r'ds_salaries.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)

    for row in reader:
        cp_loc.append(row[10])

    for i in cp_loc:
        if i not in cp_location:
            cp_location.append(i)

for i in range(len(cp_location)):
    cl = cp_location[i]
    order = 0
    num = 0
    sumSalary = 0

    with open(r'ds_salaries.csv') as f:
        readerx = csv.reader(f)
        headers = next(readerx)

        for row in readerx:
            order += 1
            if row[10] == cl:
                num += 1
                sumSalary += int(row[5])
            elif order == 607:
                break
            else:
                continue
    AverageSalaryByLoc.append(sumSalary/num)

############################################################################################################################
##### Analysis Part for Q9

minlocSalary = min(AverageSalaryByLoc)
maxlocSalary = max(AverageSalaryByLoc)

min_index = []
max_index = []

minLoc = []
maxLoc = []

for i in range(len(AverageSalaryByLoc)):
    if AverageSalaryByLoc[i] == minlocSalary:
        min_index.append(i)
    elif AverageSalaryByLoc[i] == maxlocSalary:
        max_index.append(i)
    else:
        continue

for i in range(len(min_index)):
    minLoc.append(cp_location[min_index[i]])
print("   ", minLoc, "Pays the lowest Salary    ")

for i in range(len(max_index)):
    maxLoc.append(cp_location[max_index[i]])
print("   ", maxLoc, "Pays the highest Salary")
print(
    "################################################################################################################")
print()

############################################################################################################################
##### Answer Part for Q10
print("Q10: Would you change your resume after analyzing this dataset?")
print("----------------------------------------------------------------")
print("     My Answer: Yes, I would")