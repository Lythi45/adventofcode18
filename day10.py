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
while True:
    np=[]
    for n in range(len(pp)):
        np.append((pp[n][0]+pv[n][0],pp[n][1]+pv[n][1]))
    miny=min([p[1] for p in np])
    maxy=max([p[1] for p in np])
    if maxy-miny<dy:
        dy=maxy-miny
    else:
        minx=min([p[0] for p in pp])
        maxx=max([p[0] for p in pp])
        mess=""
        for y in range(aminy,amaxy+1):
            for x in range(minx,maxx+1):
                mess+=['.','#'][(x,y) in pp]
            mess+='\n'
        print (mess,se)
        break

    pp=np
    amaxy=maxy
    aminy=miny
    se+=1
