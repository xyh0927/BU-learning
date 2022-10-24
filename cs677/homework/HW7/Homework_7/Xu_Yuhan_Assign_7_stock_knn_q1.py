import numpy as np
from sklearn.neighbors import KNeighborsClassifier

print("q1: ")
print("=================================================================================================================")
data2 = [[1,69.738,2.662296,1],[2,74.1002,4.859638,0],[3,82.8748,3.530613,0],[4,80.3168,5.533173,1],
[5,74.264,2.234561,1],[6,70.324,5.399026,1],[7,62.17,4.111891,1],[8,57.778,2.096563,1],
[9,59.466,2.245026,0],[10,63.696,2.203676,0],[11,64.166,1.774244,1],[12,66.068,2.984724,0],
[13,71.881,2.995692,0],[14,74.86,2.863033,0],[15,78.652,1.39428,0],[16,77.854,2.575301,1],
[17,72.192,4.389781,1],[18,73.046,5.170752,0],[19,65.85,8.88858,1],[20,58.923,1.320596,1],
[21,57.169,1.543206,1],[22,54.4802,1.698287,1],[23,55.9884,1.749408,0],[24,56.702,0.890334,1],
[25,55.202,1.329427,1],[26,54.404,0.980808,0],[27,53.718,1.261387,0],[28,52.606,1.265868,1],
[29,51.497,1.329465,1],[30,52.08,1.104934,0],[31,57.086,5.298081,0],[32,46.87,3.035061,1],
[33,45.444,1.345476,0],[34,46.178,0.97772,1],[35,45.893,1.764625,1],[36,43.158,1.382438,1],
[37,38.584,3.66162,1],[38,37.07,2.357914,0],[39,36.286,1.152277,1],[40,36.874,1.234043,0],
[41,36.679,1.163901,1],[42,34.04,2.33407,1],[43,32.683,1.367274,0],[44,30.833,1.864241,1],
[45,27.872,1.8449,1],[46,27.1796,1.9798,0],[47,26.224,1.13025,1],[48,24.5236,0.944739,1],
[49,24.972,1.73577,0],[50,25.104,1.3375,1],[51,23.628,1.09053,1],[52,24.74,2.003587,0],]

data3= [[1,43.664,0.942605],[2,44.226,1.015512],[3,49.498,4.383981],[4,57.77,6.791654],
[5,62.052,3.699153],[6,60.0656,4.042109],[7,64.38,3.424844],[8,67.916,2.881615],
[9,68.25,2.280316],[10,70.004,2.252399],[11,70.85,1.433903],[12,71.0962,2.393075],
[13,68.346,3.187298],[14,69.562,3.60637],[15,71.222,2.891901],[16,72.578,1.904798],
[17,69.74,4.718499],[18,77.7142,7.249087],[19,82.9648,3.14189],[20,86.376,2.022006],
[21,80.718,5.62324],[22,72.856,9.440966],[23,69.328,3.749775],[24,72.612,2.087413],
[25,69.738,2.662296],[26,74.1002,4.859638],[27,82.8748,3.530613],[28,80.3168,5.533173],
[29,74.264,2.234561],[30,70.324,5.399026],[31,62.17,4.111891],[32,57.778,2.096563],
[33,59.466,2.245026],[34,63.696,2.203676],[35,64.166,1.774244],[36,66.068,2.984724],
[37,71.881,2.995692],[38,74.86,2.863033],[39,78.652,1.39428],[40,77.854,2.575301],
[41,72.192,4.389781],[42,73.046,5.170752],[43,65.85,8.88858],[44,58.923,1.320596],
[45,57.169,1.543206],[46,54.4802,1.698287],[47,55.9884,1.749408],[48,56.702,0.890334],
[49,55.202,1.329427],[50,54.404,0.980808],[51,53.718,1.261387],[52,52.606,1.265868],]
list0 = [1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,1,1] #第一年正确的结果
datamat = np.array(data2)
X = datamat[:,0:3]
Y = datamat[:,3]
knn = KNeighborsClassifier(n_neighbors=3,weights='distance')
knn.fit(X,Y)
print("k = 3")

# for i in range(52):
#     print(knn.predict([data3[i]]))
print()
list1 = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1]

list1_1 = [None] * 52

for i in range(52):
    if(list0[i] == 0) and (list1[i] == 0):
        list1_1[i] = 'TN'
    elif(list0[i] == 0) and (list1[i] == 1):
        list1_1[i] = 'FP'
    elif(list0[i] == 1) and (list1[i] == 1):
        list1_1[i] = 'TP'
    elif(list0[i] == 1) and (list1[i] == 0):
        list1_1[i] = 'FN'
    else:
        continue
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
for i in range(52):
    if(list1_1[i] == 'TN'):
        temp1 += 1
    elif(list1_1[i] == 'FP'):
        temp2 += 1
    elif(list1_1[i] == 'TP'):
        temp3 += 1
    elif(list1_1[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Accuracy: %d' % int(temp5 * 100) + '%')
temp6 = temp3/(temp3+temp4)
temp7 = temp1/(temp1+temp2)
print('TPR: %f' % temp6)
print('TNR: %f' % temp7)
print("-----------------------------------------------------------------------------------------------------------------")
knn = KNeighborsClassifier(n_neighbors=5,weights='distance')
knn.fit(X,Y)
print("k = 5")
# for i in range(52):
#     print(knn.predict([data3[i]]))
print()

list2 = [1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1]

list2_1 = [None] * 52

for i in range(52):
    if(list0[i] == 0) and (list2[i] == 0):
        list2_1[i] = 'TN'
    elif(list0[i] == 0) and (list2[i] == 1):
        list2_1[i] = 'FP'
    elif(list0[i] == 1) and (list2[i] == 1):
        list2_1[i] = 'TP'
    elif(list0[i] == 1) and (list2[i] == 0):
        list2_1[i] = 'FN'
    else:
        continue
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
for i in range(52):
    if(list2_1[i] == 'TN'):
        temp1 += 1
    elif(list2_1[i] == 'FP'):
        temp2 += 1
    elif(list2_1[i] == 'TP'):
        temp3 += 1
    elif(list2_1[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Accuracy: %d' % int(temp5 * 100) + '%')
temp6 = temp3/(temp3+temp4)
temp7 = temp1/(temp1+temp2)
print('TPR: %f' % temp6)
print('TNR: %f' % temp7)

print("-----------------------------------------------------------------------------------------------------------------")
knn = KNeighborsClassifier(n_neighbors=7,weights='distance')
knn.fit(X,Y)
print("k = 7")
# for i in range(52):
#     print(knn.predict([data3[i]]))
print()

list3 = [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1]

list3_1 = [None] * 52

for i in range(52):
    if(list0[i] == 0) and (list3[i] == 0):
        list3_1[i] = 'TN'
    elif(list0[i] == 0) and (list3[i] == 1):
        list3_1[i] = 'FP'
    elif(list0[i] == 1) and (list3[i] == 1):
        list3_1[i] = 'TP'
    elif(list0[i] == 1) and (list3[i] == 0):
        list3_1[i] = 'FN'
    else:
        continue
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
for i in range(52):
    if(list3_1[i] == 'TN'):
        temp1 += 1
    elif(list3_1[i] == 'FP'):
        temp2 += 1
    elif(list3_1[i] == 'TP'):
        temp3 += 1
    elif(list3_1[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Accuracy: %d' % int(temp5 * 100) + '%')
temp6 = temp3/(temp3+temp4)
temp7 = temp1/(temp1+temp2)
print('TPR: %f' % temp6)
print('TNR: %f' % temp7)

print("-----------------------------------------------------------------------------------------------------------------")
knn = KNeighborsClassifier(n_neighbors=9,weights='distance')
knn.fit(X,Y)
print("k = 9")
# for i in range(52):
#     print(knn.predict([data3[i]]))
print()

list4 = [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1]
list4_1 = [None] * 52

for i in range(52):
    if(list0[i] == 0) and (list4[i] == 0):
        list4_1[i] = 'TN'
    elif(list0[i] == 0) and (list4[i] == 1):
        list4_1[i] = 'FP'
    elif(list0[i] == 1) and (list4[i] == 1):
        list4_1[i] = 'TP'
    elif(list0[i] == 1) and (list4[i] == 0):
        list4_1[i] = 'FN'
    else:
        continue
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
for i in range(52):
    if(list4_1[i] == 'TN'):
        temp1 += 1
    elif(list4_1[i] == 'FP'):
        temp2 += 1
    elif(list4_1[i] == 'TP'):
        temp3 += 1
    elif(list4_1[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Accuracy: %d' % int(temp5 * 100) + '%')
temp6 = temp3/(temp3+temp4)
temp7 = temp1/(temp1+temp2)
print('TPR: %f' % temp6)
print('TNR: %f' % temp7)

print("-----------------------------------------------------------------------------------------------------------------")
knn = KNeighborsClassifier(n_neighbors=11,weights='distance')
knn.fit(X,Y)
print("k = 11")
# for i in range(52):
#     print(knn.predict([data3[i]]))
print()

list5 = [1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,]

list5_1 = [None] * 52

for i in range(52):
    if(list0[i] == 0) and (list5[i] == 0):
        list5_1[i] = 'TN'
    elif(list0[i] == 0) and (list5[i] == 1):
        list5_1[i] = 'FP'
    elif(list0[i] == 1) and (list5[i] == 1):
        list5_1[i] = 'TP'
    elif(list0[i] == 1) and (list5[i] == 0):
        list5_1[i] = 'FN'
    else:
        continue
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
for i in range(52):
    if(list5_1[i] == 'TN'):
        temp1 += 1
    elif(list5_1[i] == 'FP'):
        temp2 += 1
    elif(list5_1[i] == 'TP'):
        temp3 += 1
    elif(list5_1[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Accuracy: %d' % int(temp5 * 100) + '%')
temp6 = temp3/(temp3+temp4)
temp7 = temp1/(temp1+temp2)
print('TPR: %f' % temp6)
print('TNR: %f' % temp7)
print("-----------------------------------------------------------------------------------------------------------------")
print("Because the accuracy of k = 9 is 57% which is higher than any other k, k* = 9")
print("#################################################################################################################")