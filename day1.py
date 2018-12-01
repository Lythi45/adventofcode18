print (sum(map(int,open("day1.txt","r").readlines())))

li=list(map(int,open("day1.txt","r").readlines()))

fr=0
frs=set()
cont=True
while cont:
    for offset in li:
        fr+=offset
        if fr in frs:
            print(fr)
            cont=False
            break
        frs.add(fr)
