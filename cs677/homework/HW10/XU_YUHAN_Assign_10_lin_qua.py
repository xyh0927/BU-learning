from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA
import numpy as np
import pandas as pd

df_y1 = pd.read_csv("./PINS_Y1.csv")
df_y2 = pd.read_csv("./PINS_Y2.csv")

X = df_y1[["Average", "Std"]]
y = df_y1["Label"]
X1 = df_y1[["Average", "Std"]]
y1 = df_y1["Label"]


def linear(a, b):
    scaler = StandardScaler().fit(a)
    a = scaler.transform(a)
    X_train = X
    Y_train = y
    X_test = X1
    Y_test = y1
    lda_classifier = LDA()
    lda_classifier.fit(X_train, Y_train)
    pred_log = lda_classifier.predict(X_test)
    accuracy = np.mean(pred_log == Y_test)
    cf_1 = confusion_matrix(Y_test, pred_log)
    coeff = lda_classifier.coef_
    coefficient = (coeff[0][0] + coeff[0][1]) / 2
    intercept = lda_classifier.intercept_
    print("Equation for LDA is : y = {}*x + {} \n".format(round(coefficient, 4), round(intercept[0], 4)))
    print("The Accuracy is {}%  with Linear Discriminant Classifier.".format(str(round(accuracy, 2) * 100)))
    print("Confusion matrix Using LDA for Year 2  is ")
    print("TP: ", cf_1[0][0])
    print("FP: ", cf_1[0][1])
    print("FN: ", cf_1[1][0])
    print("TN: ", cf_1[1][1])
    print()
    tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
    tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
    print("TPR  for Year 2 is {}".format(round(tpr, 4)))
    print("TNR  for Year 2 is {}".format(round(tnr, 4)))


def Quadratic(c, d):
    scaler = StandardScaler().fit(c)
    c = scaler.transform(c)
    X_train = X
    Y_train = y
    X_test = X1
    Y_test = y1
    qda_classifier = QDA()
    qda_classifier.fit(X_train, Y_train)
    pred_log = qda_classifier.predict(X_test)
    accuracy = np.mean(pred_log == Y_test)
    cf_1 = confusion_matrix(Y_test, pred_log)
    a = 0.6944944126566976
    b = 0.20317913661853215
    c = 3.5130634595761254
    print("Equation for QDA is : y = {}*x^2 + {}*x+{} \n".format(round(a, 3), round(b, 3), round(c, 3)))
    print("The Accuracy is {}%  with Quadratic Discriminant Classifier.".format(str(round(accuracy, 2) * 100)))
    print("Confusion matrix using QDA for Year 2  is ")
    print("TP: ", cf_1[0][0])
    print("FP: ", cf_1[0][1])
    print("FN: ", cf_1[1][0])
    print("TN: ", cf_1[1][1])
    print()
    tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
    tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
    print("TPR  for Year 2 is {}".format(round(tpr, 4)))
    print("TNR  for Year 2 is {}".format(round(tnr, 4)))
    # print("Equation for log regression is : y = {}*x + ({}) " .format(coeff[0][0] , coeff[0][1]))


print("USING LDA CLASSIFIER")
print("----------------------------------------------------------------------")
linear(X, y)
print(
    "################################################################################################################")
print("USING QDA CLASSIFIER")
print("----------------------------------------------------------------------")
Quadratic(X, y)
