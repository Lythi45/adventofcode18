bl=open("day3.txt","r").readlines()
f={}
for b in bl:
  s=b.split(':')
  px,py=map(int,s[0].split('@')[1].split(','))
  sx,sy=map(int,s[1].split('x'))
  for x in range(sx):
      for y in range(sy):
          f[(px+x,py+y)]=f.get((px+x,py+y),0)+1
print(sum([1 for x in f if f[x]>1 ]))

for b in bl:
  s=b.split(':')
  id = int(b.split('@')[0][1:])
  px,py=map(int,s[0].split('@')[1].split(','))
  sx,sy=map(int,s[1].split('x'))
  for x in range(sx):
    br=False
    for y in range(sy):
      if f[(px+x,py+y)]>1:
        br=True
        break
    if br:
        break
  else:
      print(id)
      break
