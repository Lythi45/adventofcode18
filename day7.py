import copy
rels=open("day7.txt","r").readlines()
rd={}
ls=set()
for r in rels:
    rs=r.split()
    print(r,rs)
    rv=rs[1]
    ra=rs[7]
    ls.add(rv)
    ls.add(ra)
    rs=rd.get(ra,set())
    rs.add(rv)
    rd[ra]=rs
print(rd)
srd=copy.deepcopy(rd)
ll=sorted(list(ls))
print(ll)
wl=[]
while True:
    for l in ll:
        if l not in wl and l not in rd:
            print('Independent:',l)
            wl.append(l)
            for i in list(rd.keys()):
                if l in rd[i]:
                    rd[i].remove(l)
                    if len(rd[i])==0:
                        print("Freeing:", i)
                        del rd[i]
            break
    else:
        break
print(''.join(wl))

wl=[]
rd=srd
worker={}
t=0
notfree=True
while len(wl)<len(ll) or len(worker)>0:
    for l in ll:
        if l not in wl and l not in rd and len(worker)<5:
            print('Independent:',l)
            wl.append(l)
            worker[l]=60+ord(l)-ord('A')+1


    for w in list(worker.keys()):
        worker[w]-=1
        if worker[w]==0:
            del worker[w]
            print("Done:",w)
            for i in list(rd.keys()):
                if w in rd[i]:
                    rd[i].remove(w)
                    if len(rd[i])==0:
                        print("Freeing:", i)
                        del rd[i]
    t+=1
    print(t,worker)

print(t)
