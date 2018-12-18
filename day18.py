from PIL import Image
li= open("day18.txt","r").readlines()
wi=len(li[0])+1
f=['.'*wi]+['.'+l.strip()+'.' for l in li]+['.'*wi]
r=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
print(f)
fd={}
fnd={}
n=0


def out(n):
    tn=0
    ln=0
    for c in fnd[n]:
        tn+=c=='|'
        ln+=c=='#'
    print(tn*ln)
def viz(n,lo):
    img = Image.new('RGB', (wi,len(f)), color = (0, 0, 0))
    pix=img.load()
    for i in range(1,800):
        nn=[i,(i-n)%lo+n][i>n]
        for p,c in enumerate(fnd[nn]):
            if c=='#':
                pix[p%wi,p//wi]=(120,60,0)
            elif c=='|':
                pix[p%wi,p//wi]=(0,170,0)
            else:
                pix[p%wi,p//wi]=(0,0,0)
        img.save('day18pngs/'+('000000'+str(i))[-6:]+'.png')


cont=True
while cont:
    nf=['.'*wi]
    tl=''
    for y in range(1,len(f)-1):
        nl='.'
        for x in range(1,len(f[0])-1):
            u={'.':0,'#':0,'|':0}
            c=f[y][x]
            for ri in r:
                ff=f[y+ri[1]][x+ri[0]]
                u[ff]+=1
            if c=='.':
                if u['|']>=3:
                    nl+='|'
                else:
                    nl+='.'
            elif c=='|':
                if u['#']>=3:
                    nl+='#'
                else:
                    nl+='|'
            else:
                if u['#']>=1 and u['|']>=1:
                    nl+='#'
                else:
                    nl+='.'
        nl+='.'
        nf+=[nl]
        tl+=nl
    f=nf+['.'*wi]
    n+=1
    if tl in fd:
        print('Loop detected',n,fd[tl])
        lst=fd[tl]
        lole=n-lst
        nn=(1000000000-lst)%lole+lst
        print(nn)
        out(10)
        out(nn)
        viz(lst,lole)
        break
    else:
        fd[tl]=n
        fnd[n]=tl
