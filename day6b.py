li= open("day6.txt","r").readlines()
ri=[(0,1),(1,0),(0,-1),(-1,0)]
n=1
pd={}
pp={}
for p in li:
    pe=p.split(',')
    x=int(pe[0])
    y=int(pe[1])
    pp[n]=(x,y)
    n+=1

sudi=0

def md(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

for x in range(0,400):
    print(x)
    for y in range(0,400):
        li=sorted([(p,md((x,y),pp[p])) for p in pp], key=lambda x:x[1])
        if li[0][1]==li[1][1]:
            pd[(x,y)]=0
        else:
            pd[(x,y)]=li[0][0]
        sdi=sum([md((x,y),pp[p]) for p in pp])
        if sdi<10000:
            sudi+=1

print(len(pd))
live=set()
cp={}
for p in pd:
    n=pd[p]
    cp[n]=cp.get(n,0)+1
    if p[0]==0 or p[0]==399 or p[1]==0 or p[1]==399:
        live.add(n)
print(cp)
print(live)
print(max([cp[n] for n in cp if not n in live]))
from PIL import Image
import random
import math
img = Image.new('RGB', (400, 400), color = (0, 0, 0))
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

for x in range(0,400):
    for y in range(0,400):
        if (x,y) in pd:
            pix[x,y]=col[pd[(x,y)]]
img.save('pil_color.png')
print(sudi)
