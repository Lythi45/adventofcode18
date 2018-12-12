gs=9424
gs=42
d={}
dx={}
dxy=[]
for y in range(1,301):
    for x in range(1,301):
        rid=(x+10)
        n=(rid*y+gs)*rid
        d[(x,y)]=(n%1000)//100-5
for y in range(1,301):
    for x in range(1,299):
        dx[(x,y)]=d[(x,y)]+d[(x+1,y)]+d[(x+2,y)]

for y in range(1,299):
    for x in range(1,299):
        dxy.append([(x,y),dx[(x,y)]+dx[(x,y+1)]+dx[(x,y+2)]])


print(max(dxy,key=lambda x:x[1]))

dxy=[]
for s in range(1,30):
    dx={}
    print(s)
    for y in range(1,301):
        for x in range(1,302-s):
            dx[(x,y)]=sum([d[(x+xx,y)] for xx in range(s)])

    for y in range(1,302-s):
        for x in range(1,302-s):
            dxy.append([(x,y),s,sum([dx[(x,y+yy)] for yy in range(s)])])

print(max(dxy,key=lambda x:x[2]))
