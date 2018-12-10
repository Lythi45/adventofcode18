ls=open("day8.txt","r").readlines()
input=list(map(int,ls[0].split()))

def smd(po):
    su=0
    nn=input[po]
    nm=input[po+1]
    po+=2
    for n in range(nn):
        no=smd(po)
        su+=no[0]
        po=no[1]
    su+=sum(input[po:po+nm])
    return (su,po+nm)

print (smd(0)[0])

nt=[]
def tree(nt,po):
    nn=input[po]
    nm=input[po+1]
    po+=2
    cl=[]
    for n in range(nn):
        po=tree(cl,po)
    nt.append((cl,input[po:po+nm]))
    return po+nm
tree(nt,0)

def nodev(node):
    if len(node[0])==0:
        return sum(node[1])
    else:
        print(node[1])
        return sum([nodev(node[0][n-1]) for n in node[1] if n>0 and n <=len(node[0])])
print(nodev(nt[0]))
