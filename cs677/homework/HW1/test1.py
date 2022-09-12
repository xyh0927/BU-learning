import csv

cp_loc = []
cp_location = []
AverageSalaryByLoc = []

order = 0

num = 0
sumSalary = 0

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
print("   ", minLoc, "Pays the lowest Salary\n")

for i in range(len(max_index)):
    maxLoc.append(cp_location[max_index[i]])
print("   ", maxLoc, "Pays the highest Salary")