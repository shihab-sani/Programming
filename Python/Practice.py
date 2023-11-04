t = int(input())
for i in range(t):
    x,y,k = map(int,input().split())
    if (x+k) >= y:
        print(x+k)
    else:
        s1 = (y-(x+k))*2
        print((x+k)+s1)        
