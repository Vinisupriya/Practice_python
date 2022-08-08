#Number pattern

n=6
for i in range(1,n):
    m=i
    for j in range (1,i+1):
        print(m,end='')
        m+=1
    m=m-2
    for k in range(1, i):
        print(m,end='')
        m-=1
    print()
