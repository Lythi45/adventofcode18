gl=open("day9.txt","r").readlines()[0].split()
print(gl)
np=int(gl[0])
nm=int(gl[6])
r=[0]
po=1
sc={}
print(np,nm)
for m in range(nm):
    p=m%np
    mm=m+1
    if mm%23==0:
        sc[p]=sc.get(p,0)+mm
        po=(po-7)%len(r)
        sc[p]+=r[po]
        #print(po,r[:po],r[po+1:])
        r=r[:po]+r[po+1:]
    else:
        po=(po+2)%len(r)
        r=r[:po]+[mm]+r[po:]
print(sc[max(sc,key=lambda x:sc[x])])
nm*=100
r=[[0,0,0]]
po=0
sc={}
for m in range(nm):
    p=m%np
    mm=m+1
    if mm%23==0:
        sc[p]=sc.get(p,0)+mm
        for i in range(7):
            po=r[po][1]
        sc[p]+=r[po][0]
        r[r[po][1]][2]=r[po][2]
        r[r[po][2]][1]=r[po][1]
        po=r[po][2]
    else:
        p2=r[po][2]
        p3=r[p2][2]
        po=len(r)
        r.append([mm,p2,p3])
        #print(po,mm)
        r[p2][2]=po
        r[p3][1]=po
print(sc[max(sc,key=lambda x:sc[x])])
