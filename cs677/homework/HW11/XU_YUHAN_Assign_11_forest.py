from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df_y1 = pd.read_csv("./PINS_Y1.csv")
df_y2 = pd.read_csv("./PINS_Y2.csv")

X = df_y1[["Average", "Std"]]
y = df_y1["Label"]
X1 = df_y2[["Average", "Std"]]
y1 = df_y2["Label"]
error_rate = []

print("---------------------------------------------------------------------------------------")


def Randomforest(a, b, num, depth):
    X_train = X
    Y_train = y
    X_test = X1
    Y_test = y1
    model = RandomForestClassifier(n_estimators=num, max_depth=depth, criterion="entropy")
    model.fit(X_train, Y_train)
    pred_log = model.predict(X_test)
    er = np.mean(pred_log != Y_test)
    er = round(er, 2)
    error_rate.append(np.mean(pred_log != Y_test))
    print("The Error Rate is {} for n {} and d {}".format(str(round(er, 2)), num, depth))
    return pred_log, Y_test, er


for n in range(1, 11):
    for d in range(1, 6):
        pred_log, Y_test, er = Randomforest(X1, y1, n, d)
        plt.title('n vs.d error rates ')
        plt.xlabel('number of learners : n')
        plt.ylabel('depth ')
        if (er == 0.0):
            er = 0.001
        else:
            er = er

        plt.scatter(x=n, y=d, s=er * 1000)

plt.savefig("Error_Rate.pdf")


def RandomforestOptimal(a, b, num, depth):
    X_train = X
    Y_train = y
    X_test = X1
    Y_test = y1
    model = RandomForestClassifier(n_estimators=num, max_depth=depth, criterion="entropy")
    model.fit(X_train, Y_train)
    pred_log = model.predict(X_test)

    cf_1 = confusion_matrix(Y_test, pred_log)
    print('USING RANDOM FOREST CLASSIFIER:')
    print("Confusion matrix Using RANDOM FOREST for Year 2: ")
    print("TP: ", cf_1[0][0])
    print("FP: ", cf_1[0][1])
    print("FN: ", cf_1[1][0])
    print("TN: ", cf_1[1][1])
    print()
    tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
    tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
    print("TPR  for Year 2 is {}".format(round(tpr, 4)))
    print("TNR  for Year 2 is {}".format(round(tnr, 4)))


print("---------------------------------------------------------------------------------------")
print("According to the error rate we have calculated, please input the optimal value for Year 1 ")
num = int(input("n : "))
dep = int(input("d : "))
print("Optimal value for Year 1 is for n = {} and d = {}".format(str(num), str(dep)))
print("----------------------------------------------------------------------------------------")
RandomforestOptimal(X1, y1, num, dep)
