t = int(input())
l = 0
for i in range(t):
    l += 1
    s = []
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for j in range(n):
        if k==1:
            pass
            break
        if a[j] == k :
            s.append(a[j])
        elif a[j]%k==0:
            s.append(k)
                
    print(f"Case {l}: {len(s)}")
            
            
            


