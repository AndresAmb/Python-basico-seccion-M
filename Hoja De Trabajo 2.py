print("--------------------------------------------------------------")
t=int(input("Ingrese un numero entero para generar un triangulo: "))
if t>0:
    for i in range(t+1):
        print("*"*(i))
else:
    print("El numero ingresado no es valido")


print("--------------------------------------------------------------")

ca=int(input("Ingrese un número entero: "))
if ca>0:
    for i in range(ca+1):
        print(ca-i,",", end=(""))
else:
    print("El numero ingresado no es valido")
print()
print("--------------------------------------------------------------")

p=int(input("Introduzca un número entero mayor a 2: "))
if p>=2:
    i=2
    while p %  i != 0:
        i += 1
    if i == p:
        print(str(p)+" es primo")
    else:
        print(str(p)+ " no es primo")
else:
    print("El numero ingresado no es valido")