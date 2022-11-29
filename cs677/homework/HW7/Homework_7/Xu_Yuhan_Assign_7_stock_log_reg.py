from sklearn.linear_model import LogisticRegression

X = [
[1,43.664,0.942605],[2,44.226,1.015512],[3,49.498,4.383981],[4,57.77,6.791654],[5,62.052,3.699153],
[6,60.0656,4.042109],[7,64.38,3.424844],[8,67.916,2.881615],[9,68.25,2.280316],[10,70.004,2.252399],
[11,70.85,1.433903],[12,71.0962,2.393075],[13,68.346,3.187298],[14,69.562,3.60637],[15,71.222,2.891901],
[16,72.578,1.904798],[17,69.74,4.718499],[18,77.7142,7.249087],[19,82.9648,3.14189],[20,86.376,2.022006],
[21,80.718,5.62324],[22,72.856,9.440966],[23,69.328,3.749775],[24,72.612,2.087413],[25,69.738,2.662296],
[26,74.1002,4.859638],[27,82.8748,3.530613],[28,80.3168,5.533173],[29,74.264,2.234561],[30,70.324,5.399026],
[31,62.17,4.111891],[32,57.778,2.096563],[33,59.466,2.245026],[34,63.696,2.203676],[35,64.166,1.774244],
[36,66.068,2.984724],[37,71.881,2.995692],[38,74.86,2.863033],[39,78.652,1.39428],[40,77.854,2.575301],
[41,72.192,4.389781],[42,73.046,5.170752],[43,65.85,8.88858],[44,58.923,1.320596],[45,57.169,1.543206],
[46,54.4802,1.698287],[47,55.9884,1.749408],[48,56.702,0.890334],[49,55.202,1.329427],[50,54.404,0.980808],
]

Y = [1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0]

model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(X,Y)

print("q1: ")
print("-----------------------------------------------------------------------------------------------------------------")
b0 = model.intercept_
b1 = model.coef_
b1_1 = b1.mean()
print("The equation of Logistic Regression is:")
print("y = e^(",b0,"+",b1_1,"*x)","/(1 + e^(",b0,"+",b1_1,"*x))")
print("ln(y/1-y) = ",b0,"+",b1_1,"*x")
print("=================================================================================================================")

print("q2: ")
print("q3: ")

#Year 2
data_test = [
[1,51.497,1.329465],[2,52.08,1.104934],[3,57.086,5.298081],[4,46.87,3.035061],[5,45.444,1.345476],
[6,46.178,0.97772],[7,45.893,1.764625],[8,43.158,1.382438],[9,38.584,3.66162],[10,37.07,2.357914],
[11,36.286,1.152277],[12,36.874,1.234043],[13,36.679,1.163901],[14,34.04,2.33407],[15,32.683,1.367274],
[16,30.833,1.864241],[17,27.872,1.8449],[18,27.1796,1.9798],[19,26.224,1.13025],[20,24.5236,0.944739],
[21,24.972,1.73577],[22,25.104,1.3375],[23,23.628,1.09053],[24,24.74,2.003587],[25,25.79,0.659181],
[26,25.293,0.827283],[27,24.668,1.87032],[28,22.71,0.753445],[29,20.75,1.494148],[30,20.11,1.143853],
[31,22.1166,1.487073],[32,21.207,1.505329],[33,22.285,1.068841],[34,20.52,2.425259],[35,19.657,0.696805],
[36,19.692,0.742063],[37,18.253,0.809058],[38,20.166,1.611292],[39,19.824,1.762925],[40,19.426,1.198075],
[41,19.744,1.250242],[42,19.307,1.57438],[43,18.677,1.077876],[44,21.398,1.960912],[45,23.2502,0.644949],
[46,22.471,1.006382],[47,22.3744,1.368715],[48,22.484,0.772207],[49,23.97,1.955842],[50,24.964,0.766983],
]
print(model.predict(data_test))

#Year 1
list0 = [1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,1]
#Year 2
listl = [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

listl_1 = [None] * 50

print("The confusion matrix for Year 2:")

for i in range(50):
    if(list0[i] == 0) and (listl[i] == 0):
        listl_1[i] = 'TN'
    elif(list0[i] == 0) and (listl[i] == 1):
        listl_1[i] = 'FP'
    elif(list0[i] == 1) and (listl[i] == 1):
        listl_1[i] = 'TP'
    elif(list0[i] == 1) and (listl[i] == 0):
        listl_1[i] = 'FN'
    else:
        continue
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
for i in range(50):
    if(listl_1[i] == 'TN'):
        temp1 += 1
    elif(listl_1[i] == 'FP'):
        temp2 += 1
    elif(listl_1[i] == 'TP'):
        temp3 += 1
    elif(listl_1[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Accuracy: %d' % int(temp5 * 100) + '%')
print("=================================================================================================================")

print("q4: ")
print("-----------------------------------------------------------------------------------------------------------------")

temp6 = temp3/(temp3+temp4)
temp7 = temp1/(temp1+temp2)
print('TPR: %f' % temp6)
print('TNR: %f' % temp7)