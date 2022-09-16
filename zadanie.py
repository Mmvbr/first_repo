n=5
m=6
([[i*n+j+i for j in range(m)] for i in range(n)])
([[0 if i==j else 1 if j>i else 2 for j in range(m)]for i in range(n)])
([[max(i,j) for j in range(n)]for i in range(n)])
lines=open('input.txt','r',encoding='utf-8').readlines()
mx=[0,0,0]
for a in lines:
    a=a.splite()
    if int(a[3])>mx[int(a[2]-9)]:
        mx[int(a[2]-9)]=int(a[3])
print(mx[0],mx[1],mx[2])
