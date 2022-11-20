from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd

df_Y1 = pd.read_csv("./PINS_Y1.csv")
df_Y2 = pd.read_csv("./PINS_Y2.csv")

print('#######################################################################')

X = df_Y1[["Average", "Std"]]
y = df_Y1["Label"]
x1 = df_Y2[["Average", "Std"]]
y1 = df_Y1["Label"]

def naive_bayesian(a, b):
    X_train = X
    Y_train = y
    X_test = x1
    Y_test = y1
    NB_classifier = GaussianNB().fit(X_train, Y_train)
    pred_log = NB_classifier.predict(X_test)
    accuracy = np.mean(pred_log == Y_test)
    print("The Accuracy is {}%  with Naive Bayesian for Year 2".format(round(accuracy*100,2)))
    return pred_log, Y_test


pred_log, Y_test = naive_bayesian(X, y)

cf_1 = confusion_matrix(Y_test, pred_log)
print("Confusion matrix for Year 2  is")
print("TP: ", cf_1[0][0])
print("FP: ", cf_1[0][1])
print("FN: ", cf_1[1][0])
print("TN: ", cf_1[1][1])
print("--------------------------------------------")
tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
print("TPR  for Year 2 is {}".format(tpr))
print("TNR  for Year 2 is {}".format(tnr))