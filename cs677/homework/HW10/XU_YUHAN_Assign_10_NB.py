from sklearn.metrics import confusion_matrix
from scipy import stats
import numpy as np
import pandas as pd

df_y1 = pd.read_csv("./PINS_Y1.csv")
df_y2 = pd.read_csv("./PINS_Y2.csv")

Xy2_mr = df_y2[["Average"]]
Xy2_vol = df_y2[["Std"]]
Xy2_Label = df_y2['Label']

Label0_y1 = df_y1[df_y1.Label.isin([0])]
Label1_y1 = df_y1[df_y1.Label.isin([1])]

df_red = df_y1.groupby(['Label']).agg({'Average': 'count'}).reset_index()
red = (df_red.loc[df_red.Label == 0, 'Average']).values
green = (df_red.loc[df_red.Label == 1, 'Average']).values
totr = df_red.sum()
totr = totr.to_numpy()
p_red = (red / totr[1])
totg = df_red.sum()
totg = totg.to_numpy()
p_green = (green / totg[1])

print("####################################################")

error_rate = []
d_lst = [0.5, 1, 5]

# print('For Label 1 2019')
X11 = Label1_y1[["Average"]]
df11, location11, scale11 = stats.t.fit(X11)
X12 = Label1_y1[["Std"]]
df12, location12, scale12 = stats.t.fit(X12)

# print('For Label 0 2019')
X01 = Label0_y1[["Average"]]
df01, location01, scale01 = stats.t.fit(X01)
X02 = Label0_y1[["Std"]]
df02, location02, scale02 = stats.t.fit(X02)


def Student_t(degree):
    for d in degree:

        value11 = stats.t.pdf(Xy2_mr, d, location11, scale11)
        value11 = value11.tolist()

        value12 = stats.t.pdf(Xy2_vol, d, location12, scale12)
        value12 = value12.tolist()

        value01 = stats.t.pdf(Xy2_mr, d, location01, scale01)
        value01 = value01.tolist()

        value02 = stats.t.pdf(Xy2_vol, d, location02, scale02)
        value02 = value02.tolist()

        pred_lst = []

        for i in range(0, len(value11)):
            posterior_red = p_red * value01[i] * value02[i]
            a_red = list(posterior_red)
            post_red = a_red[0]
            posterior_green = p_green * value11[i] * value12[i]
            a_green = list(posterior_green)
            post_green = a_green[0]
            normalized_red = post_red / (post_red + post_green)
            normalized_green = post_green / (post_red + post_green)
            if (normalized_red >= normalized_green):
                pred_lst.append(0)
            else:
                pred_lst.append(1)
        accuracy = np.mean(pred_lst == Xy2_Label)
        error_rate.append(accuracy)
        print("Accuracy for df {} is {}%: ".format(d, round(accuracy*100, 2)))
        print("--------------------------------------------")
        cf_1 = confusion_matrix(Xy2_Label, pred_lst)
        print("Confusion matrix for Y2 with (df = {}) is".format(d))
        print("TP: ", cf_1[0][0])
        print("FP: ", cf_1[0][1])
        print("FN: ", cf_1[1][0])
        print("TN: ", cf_1[1][1])
        print("--------------------------------------------")
        tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
        tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
        print("TPR  for Year 2 (df = {}) is {}".format(d, round(tpr, 3)))
        print("TNR  for Year 2 (df = {}) is {}".format(d, round(tnr,3)))
        print("####################################################")

    max_value = max(error_rate)
    max_index = error_rate.index(max_value)
    maxd = d_lst[max_index]
    print('Best value for df is : ', d_lst[max_index])
    return maxd


maxd = Student_t(d_lst)
