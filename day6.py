li= open("day6.txt","r").readlines()
ri=[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
n=1
pd={}
for p in li:
    pe=p.split(',')
    pd[(int(pe[0]),int(pe[1]))]=(n,(0,0))
    n+=1
print(pd)
z=0
while True:
    print(z)
    for p in list(pd.keys()):
        #print("P",p)
        n=pd[p][0]
        di=pd[p][1]
        #print("Di",di)
        if n>0:
            pd[p]=(-n,di)
            for r in ri:
                np=(p[0]+r[0],p[1]+r[1])
                if np in pd:
                    nn=pd[np]
                    ndi=pd[np][1]
                    if n!=nn:
                        sdd=abs(di[0])+abs(di[1])-abs(ndi[0])-abs(ndi[1])
                        if sdd<0:
                            pd[np]=(n,(di[0]+r[0],di[1]+r[1]))
                        elif sdd==0:
                            pd[np]=(0,(di[0]+r[0],di[1]+r[1]))
                else:
                    pd[np]=(n,(di[0]+r[0],di[1]+r[1]))
    z+=1
    if z>10:
        break
print(len(pd))
live=set()
cp={}
for p in pd:
    n=pd[p][0]
    if n<0:
        cp[-n]=cp.get(-n,0)+1
    else:
        live.add(n)
print(cp)
print(live)
#print(max([cp[n] for n in cp if not n in live]))
from PIL import Image
import random
col={}
for i in range(51):
    col[i]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
col[0]=(255,0,0)

img = Image.new('RGB', (500, 500), color = (0, 0, 0))
pix=img.load()
for x in range(0,500):
    for y in range(0,500):
        if (x,y) in pd:
            pix[x,y]=col[abs(pd[(x,y)][0])]
img.save('pil_color.png')
