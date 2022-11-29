from sklearn.metrics import confusion_matrix
from sklearn import tree
import numpy as np
import pandas as pd

df_y1 = pd.read_csv("./PINS_Y1.csv")
df_y2 = pd.read_csv("./PINS_Y2.csv")

X = df_y1[["Average", "Std"]]
y = df_y1["Label"]
X1 = df_y2[["Average", "Std"]]
y1 = df_y2["Label"]


def decisionTree(a, b):
    X_train = X
    Y_train = y
    X_test = X1
    Y_test = y1
    tree_classifier = tree.DecisionTreeClassifier(criterion="entropy")
    tree_classifier = tree_classifier.fit(X_train, Y_train)
    pred_log = tree_classifier.predict(X_test)
    accuracy = np.mean(pred_log == Y_test)

    cf_1 = confusion_matrix(Y_test, pred_log)
    print('USING Decision Tree CLASSIFIER: \n------------------------------------------------------------------------')
    print("Accuracy with Decision Tree Classifier: {}%".format(str(round(accuracy*100, 2))))
    print("Confusion matrix Using Decision Tree for Year 2  is:")
    print("TP: ", cf_1[0][0])
    print("FP: ", cf_1[0][1])
    print("FN: ", cf_1[1][0])
    print("TN: ", cf_1[1][1])
    print()
    tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
    tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
    print("TPR  for Year 2 is {}".format(round(tpr, 4)))
    print("TNR  for Year 2 is {}".format(round(tnr, 4)))

decisionTree(X1,y1)