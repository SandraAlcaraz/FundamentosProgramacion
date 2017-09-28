#Sandra Alcaraz Amezcua A01631701
import codecs
achAb=("C:\\calificacionesAlumnos.txt")
archivo=open(achAb,"r")
lina=archivo.readline()
line=archivo.readline()
file=open("C:\\Users\\Sandra\\Desktop\\promedioAlumnos.txt","w")
while line!="":
    lis=line.split(":")
    v=(int(lis[2])+int(lis[3])+int(lis[4]))/3
    if v<70:
        k="reprobado"
    else:
        k="aprobado"
    
    v=("%0.2f" %(v))
    v=str(v)
    cap=lis[1]+":"+ v+":"+k
    print(cap)
    print(lis[1]+":"+ v+":"+k+"\n")
    file.write(lis[1]+":"+ v+":"+k+"\n")
    line=archivo.readline()
    
