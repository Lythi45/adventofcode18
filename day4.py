bl=sorted(open("day4.txt","r").readlines())
print(bl)
id=0
asleep=False
slmi=0
gst={}
gsmid={}
for b in bl:
    mi=int(b.split(']')[0].split(':')[1])
    if b.split()[2]=='Guard':
        gid=int(b.split()[3][1:])
    else:
        if asleep:
            gst[gid]=gst.get(gid,0)+mi-slmi
            asleep=False
            smid=gsmid.get(gid,{})
            for m in range(slmi,mi):
                smid[m]=smid.get(m,0)+1
            gsmid[gid]=smid
        else:
            slmi=mi
            asleep=True
sleepiest_guard=max(gst, key=lambda key: gst[key])
smid=gsmid[sleepiest_guard]
sleepiest_minute=max(smid,key=lambda key: smid[key])
print(sleepiest_guard*sleepiest_minute)

sleepiest_guard=max(gst,key=lambda gid:gsmid[gid][max(gsmid[gid],key=lambda mi:gsmid[gid][mi])])
smid=gsmid[sleepiest_guard]
sleepiest_minute=max(smid,key=lambda key: smid[key])
#print(sleepiest_guard,sleepiest_minute)
print(sleepiest_guard*sleepiest_minute)
