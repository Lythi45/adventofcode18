li = open("day12.txt","r").readlines()
s='....'+li[0].split()[2]+'....'
ru={}
for i in range(2,len(li)):
    r=li[i].split(' => ')
    ru[r[0]]=r[1].rstrip()

i=0
pl={}
ss={}
while True:
    ns=""
    for p in range(0,len(s)-4):
        ns+=ru[s[p:p+5]]
    #print(ns[i*2:])
    s='....'+ns+'....'
    i+=1
    pl[i]=sum([p-(i+2)*2 for p in range(len(s)) if s[p]=='#'])
    sts=s.strip('.')
    if sts in ss:
        #print(i,ss[sts])
        diff_i=i-ss[sts]
        diff_v=pl[i]-pl[ss[sts]]
        #print(pl[i],pl[ss[sts]])
        ii=50000000000
        print(pl[ss[sts]]+(ii-ss[sts])*diff_v//diff_i)
        break
    else:
        ss[sts]=i
    if i==20:
        print(pl[i])
