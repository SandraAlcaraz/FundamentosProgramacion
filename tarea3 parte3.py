#Tarea3 parte3
#Sandra Guadalupe Alcaraz Amezcua
def escribe():
    v=True
    archivo=open("Datospy.txt","w")
    while v:
        nom=input("Capture el nombre")
        if nom!="":
            ap=input("Capture el apellido paterno")
            am=input("Capture el apellido materno")
            fec=input("Capture la fecha de nacimiento en fotmato dd/mm/aa")
            ecv=input("Capture el estado civil")
            dat=nom+":"+ap+":"+am+":"+fec+":"+ecv
            #print(dat)
            archivo.write(dat+"\n")
        else:
            break
    archivo.close()
    
def leeInfo():
    archivo=open("Datospy.txt","r")
    line=archivo.readline()
    while line != "":
        li=line.split(":")
        print("Nombre:"+li[0]+" "+li[1]+" "+li[2])
        print("Fecha de nacimiento "+li[3])
        print("Estado civil "+li[4])
        line=archivo.readline()
    archivo.close()
    
escribe()
leeInfo()
