programa_activo = True
while programa_activo:
    intentos = 0
    
    while intentos < 3:
        usuario = input("Usuario: ")
        clave = input("Contraseña: ")

        if usuario == "":
            print("Error: Usuario vacío.")
        elif " " in usuario:
            print("Error: El usuario no puede tener espacios.")
        elif len(clave) < 8:
            print("Error: La contraseña es muy corta (mínimo 8).")
        else:
            if usuario == "admin" and clave == "Admin2026":
                print("¡Acceso concedido!")
               
                sesion_activa = True
                while sesion_activa:
                    print("1. Clasificar numero")
                    print("2. Categoria de edad y permisos")
                    print("3. Calcular tarifa final")
                    print("4. Cerrar sesion")
                    print("5. Salir")

                    opcion = input("Selecciona una opcion: ")
                    if opcion == "1":
                        print("Opcion 1 seleccionada")
                    elif opcion == "2":
                        print("Opcion 2 seleccionada")
                    elif opcion == "3":
                        print("Opcion 3 seleccionada")
                    elif opcion == "4":
                        print("Cerro sesion correctamente")
                        sesion_activa = False
                    elif opcion == "5":
                        print("Salio del programa")
                        programa_activo = False
                        sesion_activa = False
                    else:
                        print("Opcion invalida")
                break
            else:
                intentos += 1
                print("Datos incorrectos.")
                print("Te quedan", 3 - intentos, "intentos.")
    if intentos == 3:
        print("SISTEMA BLOQUEADO")
        programa_activo = False