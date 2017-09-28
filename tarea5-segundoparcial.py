#Tarea 5
#Sandra Gpe. Alcaraz Amezcua A01631701
def main():
    x=str(input("Ingrese la fecha en este formato dd/mm/yyyy "))
    y=x.count("/")
    m=traduceFecha(x,y)
def traduceFecha(x,y):
    if  len(x)==10 and y==2:
        a,b,c=x.split('/')
        a=int(a)
        b=int(b)
        c=int(c)
        if a<32 and a>0 and c>999 and c<10000:
            if b>0 and b<13:
                 if b==1:
                     b="Enero"
                 elif b==2:
                     b="Febrero"
                 if b==3:
                     b="Marzo"
                 if b==4:
                     b="Abril"
                 if b==5:
                     b="Mayo"
                 if b==6:
                     b="Junio"
                 if b==7:
                     b="Julio"
                 if b==8:
                     b="Agosto"
                 if b==9:
                     b="Septiembre"
                 if b==10:
                     b="Octubre"
                 if b==11:
                     b="Noviembre"
                 if b==12:
                     b="Diciembre"
                 print(a,b,c)
            else:
                 print("la fecha está fuera del rango")    
    else:
        print("no tiene el formato correcto")
main()

