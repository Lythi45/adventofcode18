li = open("day13.txt","r").readlines()
ri=[(1,0),(0,1),(-1,0),(0,-1)]
zr={'>':0,'v':1,'<':2,'^':3}
rc={'/':[3,2,1,0],'\\':[1,0,3,2]}
tr=[]
for y in range(len(li)):
    l=li[y]
    for x in range(len(l)):
        c=l[x]
        if c in zr:
            tr.append([(x,y),zr[c],0])
print(li)
print(tr)
cont=True
while cont:
    tr.sort(key=lambda x: x[0][0]+x[0][1]*1000)
    cl=[]
    for i in range(len(tr)):
        if i not in cl:
            p=tr[i][0]
            rn=tr[i][1]
            rr=ri[rn]
            rrv=tr[i][2]
            np=(p[0]+rr[0],p[1]+rr[1])
            for j in range(len(tr)):
                if tr[j][0]==np and j not in cl:
                    print('Collision:',np)
                    cl.append(i)
                    cl.append(j)
                    break
            c=li[np[1]][np[0]]
            if c in rc:
                rn=rc[c][rn]
            elif  c=='+':
                rn=(rn-1+rrv)%4
                rrv=(rrv+1)%3
            tr[i]=[np,rn,rrv]
    cl.sort()
    for i in range(len(cl)):
        del tr[cl[i]-i]
    cont=len(tr)>1
    if not cont:
        print("Last Train: ",tr[0])
