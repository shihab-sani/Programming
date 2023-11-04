arry = [4,5,8,10,12,15,19,20,7]
target = 19
for i in range(len(arry)):
    for j in range(i+1, len(arry)):
        if arry[i] + arry[j] == target:
            print(arry[i], arry[j])
     
