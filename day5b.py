import time
st_ti=time.process_time()

poly=open("day5.txt","r").read().strip()
#poly="abcCBAefgdD"
def l_react(poly):
    i=1
    j=2
    while j < len(poly)-1:
        a=poly[i]
        b=poly[j]
        if a.upper()==b.upper() and a!=b:
            poly=poly[:i]+poly[j+1:]
            i-=1
            j-=1
        else:
            i+=1
            j+=1
    return len(poly)-1

print(l_react('#'+poly))
#11476

ppoly=open("day5.txt","r").read().strip()
pset=set(map(lambda x:x.upper(),ppoly))
minl=len(ppoly)
for delc in pset:
    poly=[c for c in ppoly if c.upper()!=delc]
    minl=min(minl,l_react('#'+''.join(poly)))
print(minl)
print("Seconds used: ",time.process_time()-st_ti)
