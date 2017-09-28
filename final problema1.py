#Sandra Alcaraz Amezcua A01631701
#Problema 1
dic={}
lista=[]
ub=("C:\\Users\\Sandra\\Desktop\\Alumnos.txt")
archivo=open(ub,"r")
lina=archivo.readline()
line=archivo.readline()
while line!="":
    lis=line.split(":")
    v=(int(lis[2])+int(lis[3])+int(lis[4]))/3
    if v<70:
        k="reprobado"
    else:
        k="aprobado"
    m=lis[0].upper()
    v=("%0.2f" %(v))
    lista.append(v)
    v=str(v)
    w=m+":"+lis[1]+":"+v+":"+k
    print(w)
    dic[v]=w
    line=archivo.readline()
lista.sort()
c=0
g=len(lista)
file=open("C:\\Users\\Sandra\\Desktop\\promedioAlumnos.txt","w")
while c<g:
    r=lista[c]
    l=dic.get[r]
    file.write(l)
    c=c+1
print(lista)
print(dic)
