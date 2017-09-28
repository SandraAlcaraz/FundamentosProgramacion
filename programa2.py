#Programa 2
#Sandra Alcaraz Amezcua
x=int(input("Ingrese el número"))
for y in range (1,x+1):
    u=(((1+5**.5)**y)-((1-5**.5)**y))/((2**y)*5**.5)
    print("%d" %u)
