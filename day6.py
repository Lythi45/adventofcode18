li= open("day6.txt","r").readlines()
ri=[(0,1),(1,0),(0,-1),(-1,0)]
n=1
pd={}
pp={}
for p in li:
    pe=p.split(',')
    x=int(pe[0])
    y=int(pe[1])
    pd[(x,y)]=n
    pp[n]=(x,y)
    n+=1
print(pd)
z=0

def md(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

while True:
    print(z)
    for p in list(pd.keys()):
        #print("P",p)
        n=pd[p]
        #print("Di",di)
        if n>0:
            pd[p]=-n
            for r in ri:
                np=(p[0]+r[0],p[1]+r[1])
                if np in pd:
                    nn=pd[np]
                    if n!=abs(nn) and nn!=0:
                        sdd=md(np,pp[n])-md(np,pp[abs(nn)])
                        if sdd<0:
                            pd[np]=n
                        elif sdd==0:
                            #pass
                            pd[np]=0
                else:
                    pd[np]=n
    z+=1
    if z>200:
        break
print(len(pd))
live=set()
cp={}
for p in pd:
    n=pd[p]
    if n<0:
        cp[-n]=cp.get(-n,0)+1
    else:
        live.add(n)
print(cp)
print(live)
print(max([cp[n] for n in cp if not n in live]))
from PIL import Image
import random
import math
img = Image.new('RGB', (600, 600), color = (0, 0, 0))
pix=img.load()
col={}
for i in range(51):
    wi=math.pi*2/50*i
    #col[i]=(random.randint(100,255),random.randint(100,255),random.randint(100,255))
    col[i]=(int((math.sin(wi)+1)*127),
            int((math.sin(wi+2*math.pi/3)+1)*127),
            int((math.sin(wi+4*math.pi/3)+1)*127))
    col[-i]=(col[i][0]//2,col[i][1]//2,col[i][2]//2)
    pix[i,0]=col[i]
    pix[i,1]=col[-i]
col[0]=(255,0,0)

for x in range(0,600):
    for y in range(0,600):
        if (x-100,y-100) in pd:
            pix[x,y]=col[pd[(x-100,y-100)]]
img.save('pil_color.png')
