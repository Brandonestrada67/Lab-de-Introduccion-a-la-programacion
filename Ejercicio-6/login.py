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
                    print("\n MENÚ PRINCIPAL ")
                    print("1. Clasificar numero")
                    print("2. Categoria de edad y permisos")
                    print("3. Calcular tarifa final")
                    print("4. Cerrar sesion")
                    print("5. Salir")

                    opcion = input("Selecciona una opcion: ")
                    
                    if opcion == "1":
                        print("Ingresa el número que quieres clasificar:")
                        numero = int(input("Numero: "))
                        if numero > 0:
                            print("El número es positivo.")
                        elif numero < 0:
                            print("El número es negativo.")
                        else:   
                            print("El número es cero.")
                        if numero != 0:
                            if numero % 2 == 0:
                                print("El número es par.")
                            else:
                                print("El número es impar.")

                    elif opcion == "2":
                        print("Ingresa tu edad:")
                        edad = int(input("Edad: "))
                        
                        if edad < 0 or edad > 120:
                            print("Error: Edad inválida.")
                        else:
                            if edad <= 12:
                                categoria = "Niñez"
                            elif edad <= 17:
                                categoria = "Adolescencia"
                            elif edad <= 64:
                                categoria = "Adultez"
                            else:
                                categoria = "Persona Mayor"
                            
                            print(f"Categoría: {categoria}")
                            identificacion = input("¿Tienes identificación? (S/N): ")
                            licencia = input("¿Tienes licencia de conducir? (S/N): ")
                            if edad >= 13:
                                print(" Puede registrarse.")
                            else:
                                print("No puede registrarse.")
                            if edad >= 18:
                                print(" Puede comprar sin tutor.")
                            else:
                                print(" Requiere tutor para comprar.")
                            if edad >= 18 and licencia == "S":
                                print("Puede conducir.")
                            if edad >= 21 and identificacion == "S":
                                print(" Tiene acceso al servicio premium.")

                    elif opcion == "3":
                        print("Opción 3 seleccionada (Cálculo de tarifa)")
                        precio_final = 200
                        precio_base = 200
                        edad = int(input("Ingresa tu edad para calcular la tarifa: "))
                        if edad < 0 or edad > 120:
                            print("Error: Edad inválida.")
                        dia_semana = int(input("Dia de la semana (1-7): "))
                        print("Es estudiante? (S/N): ")
                        print("Es miembro? (S/N): ")
                        metodo_pago = input("Metodo de pago Efectivo o Tarjeta (E/T): ")
                        if dia_semana == 1 or dia_semana ==5:
                            precio_final= 200
                            precio_base = 200
                        if dia_semana == 6 or dia_semana == 7:
                            precio_base = precio_base * 1.10
                        
                        if edad < 12:
                            precio_base += 50
                        elif edad >= 13 and edad <= 17:
                            precio_base += 20
                        elif edad >= 65:
                            precio_base += 30
                        else: 
                            print("Edad invalida.")

                        if edad >=13:
                            descuento_estudiante = input("¿Eres estudiante? (S/N): ")
                        if descuento_estudiante == "S":
                            precio_base += 15

                        descuento_miembro = input("¿Eres miembro? (S/N): ")
                        if descuento_miembro == "S":
                            precio_base += 10

                        if metodo_pago == "E":
                            descuento_total_porcentaje += 5
                            print("Descuento por pago en efectivo aplicado.")
                        

                        
                        limite_descuento = precio_base * 0.60
                        if precio_base > limite_descuento:
                            precio_base = limite_descuento  

                        print(f"Precio base: {precio_final}")
                        print(f"Recargo: {precio_base - 200}")
                        print(f"Descuento: {200 - precio_base}")
                        print(f"Total: {precio_base}")
                    
                    elif opcion == "4":
                        print("Cerró sesión correctamente.")
                        sesion_activa = False
                        
                    elif opcion == "5":
                        print("Salió del programa.")
                        programa_activo = False
                        sesion_activa = False
                    else:
                        print("Opción inválida.")
                break
            else:
                intentos += 1
                print("Datos incorrectos.")
                print("Te quedan", 3 - intentos, "intentos.")
                
    if intentos == 3:
        print("SISTEMA BLOQUEADO")
        programa_activo = False