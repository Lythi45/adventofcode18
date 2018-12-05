import time
st_ti=time.process_time()

poly=open("day5.txt","r").read().strip()

def l_react(poly):
    i=1
    j=2
    a=poly[i]
    b=poly[j]
    while j < len(poly)-1:
        if a.upper()==b.upper() and a!=b:
            react=True
            i+=2
        else:
            np+=a
            i+=1
    if i==len(poly)-1:
        np+=poly[i]
    poly=np
print(len(poly))
#11476

ppoly=open("day5.txt","r").read().strip()
pset=set(map(lambda x:x.upper(),ppoly))
print(pset)
minl=len(ppoly)
for delc in pset:
    poly=[c for c in ppoly if c.upper()!=delc]
    print(delc,len(poly))
    react=True
    while react:
        react=False
        np=""
        i=0
        while i < len(poly)-1:
            a=poly[i]
            b=poly[i+1]
            if a.upper()==b.upper() and a!=b:
                react=True
                i+=2
            else:
                np+=a
                i+=1
        if i==len(poly)-1:
            np+=poly[i]
        poly=np
    if len(poly)<minl:
        minl=len(poly)
print(minl)
print(time.process_time()-st_ti)
