from PIL import Image
img = Image.new('RGB', (140,70), color = (0, 0, 0))
pix=img.load()

def bild(bn,pp):
    for y in range(0,70):
        for x in range(0,140):
            pix[x,y]=[(255,255,255),(0,0,0)][(x+100,y+80) in pp]
    img.save('pngs/'+('000000'+str(bn))[-6:]+'.png')

import re
li= open("day10.txt","r").readlines()
print(len(li))
pp=[]
pv=[]
for l in li:
    p=re.split('[<>,]', l)
    pp.append((int(p[1]),int(p[2])))
    pv.append((int(p[4]),int(p[5])))

dy=9999999
amaxy=0
amaxy=0
se=0
bo=0
while True:
    np=[]
    for n in range(len(pp)):
        np.append((pp[n][0]+pv[n][0],pp[n][1]+pv[n][1]))
    miny=min([p[1] for p in np])
    maxy=max([p[1] for p in np])
    if se>10050:
        if se==10117:
            for i in range(10):
                bild(se-10050+bo,pp)
                bo+=1
            bo-=1
        else:
            bild(se-10050+bo,pp)
    if se>10200:
        break

    pp=np
    amaxy=maxy
    aminy=miny
    se+=1
