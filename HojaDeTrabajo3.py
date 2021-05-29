print("--------------------------------------------------------------------------------")
contraseña=input("Ingrese una nueva contraseña: ")
vcontraseña=input("Verifique su contraseña: ")
while contraseña!=vcontraseña:
    vcontraseña=input("Las contraseñas no coinciden, vuelva a intentarlo: ")
print("Contraseña verificada")
print("--------------------------------------------------------------------------------")
nEntrad=input("Nueva entrada (Si/No): ").upper()
while nEntrad=="SI":
    nombre=input("Ingrese su nombre: ").upper()
    sexo=input("Ingrse su sexo (hombre/mujer): ").upper()
    pletra=nombre[0]
    while sexo!="MUJER" and sexo!="HOMBRE":
            sexo=input("El genero ingresado no es valido, intente de nuevo: ").upper()
    if sexo=="MUJER":
        if pletra<"M":
            print("Usted pertenece al grupo A")
        else:
            print("Ustes pertenece al grupo B")
    elif sexo=="HOMBRE":
        if pletra>"N":
            print("Usted pertenece al grupo A")
        else:
            print("Usted pertenece al grupo B")
    else:
        print()
    print()
    nEntrad=input("Nueva entrada (Si/No): ").upper()
print("Que tenga un feliz día")
print("--------------------------------------------------------------------------------")
