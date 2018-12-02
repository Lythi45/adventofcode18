bl=list(map(lambda x:x.strip(),open("day2.txt","r").readlines()))
n2=0
n3=0
for b in bl:
    d={}
    for c in b:
        d[c]=d.get(c,0)+1
    vd=d.values()
    n2+=[0,1][2 in vd]
    n3+=[0,1][3 in vd]
print(n2*n3)

for po in range(len(bl[0])):
    bset=set()
    for b in bl:
        bb=b[:po]+b[po+1:]
        if bb in bset:
            print(bb)
        bset.add(bb)
