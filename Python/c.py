def count(l,arry,count1):
    
    for i in range(len(arry)):
        for j in range(i+1,len(arry)):
            if arry[i] + arry[j] >= a and arry[i] + arry[j] <= b:
                count1 += 1
    return count1
n = int(input())
count1 = 0
h = 0
for k in range(n):
    l = int(input())
    f = l//2
    a,b = map(int,input().split())
    
    h += 1
    arry = list(map(int,input().split()))
    
    s = count(l,arry,count1)
    print(f"Case {h}: {s}")
    
    