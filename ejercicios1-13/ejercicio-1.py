def palabra10():

    x= input("ingresa la palabra que deseas repetir 10 veces: ")
    for i in range  (10):
        print(x)


def edad():
 x=int(input("ingresa la edad que tienes: "))
 for i in range (1, x, 1):
    print(x)


def numerosimpares():
   x=int(input("ingresa el numero entero positivo: "))
   for i in range(1, x + 1, 2):
      print (i, end=",")


def cuenta_regresiva():
   x= int(input("numero para cuenta regresiva: "))
   for i in  range (x, -1 , -1):
      print(i)


def inversion():
   x= int(input("Cantidad a invertir"))
   y= int(input("dame el interes anual"))
   z= int(input("dame el numero de años: "))
   total = 0

   for i in range(z):
      total = total + x  + (x*(y/100))
      print(total)


def triangulo():
   x=int(input("ingresa el numero de filas de ka piramide: "))
   for i in  range (1 , x + 1):
      print("*" *i )

def tablas():
   for i in range (1,11):
      for j in range (1,11):
         resultado = i * j
         print(i, "x", j, "=", resultado)

def piramide_impares():
    n = int(input("Introduce la altura del triángulo: "))
    
    for i in range(1, n + 1):
        for j in range(2 * i - 1, 0, -2):
            print(j, end=" ")
        print()


def contraseña():
   contraseña= "laboratorio"
   intento = ""
   while intento != contraseña:
      intento = input("Ingresa la contraseña: ")
   print("Contraseña correcta. Acceso concedido.")


def num_entero_primo():
   num = int(input("Ingresa un número entero positivo: "))
   if num < 2:
      print(num, "no es primo.")
      return
   for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
         print(num, "no es primo.")
         return
   print(num, "es primo.")


def palabra_al_reves():
   palabra = input("Ingresa una palabra: ")
   for i in range(len(palabra) - 1, -1, -1):
      print(palabra[i])

def frase_letra():
   frase = input("Ingresa una frase: ")
   letra = input("Ingresa una letra: ")
   contador = 0
   for caracter in frase:
      if caracter == letra:
         contador += 1
   print(f"La letra '{letra}' aparece {contador} veces en la frase.")


def eco():
   palabra=" "
   while palabra != "salir":
      palabra= input("ingresa una palabra: ")
      if palabra != "salir":
         print(palabra)

opcion= int(input("dame el numero de opciones: "))
match opcion:
   case 1:
      palabra10()
   case 2:
      edad()
   case 3:
      numerosimpares()
   case 4:
      cuenta_regresiva()
   case 5:
      inversion()
   case 6:
      triangulo()
   case 7:
      tablas()
   case 8:
      piramide_impares()
   case 9:
      contraseña()
   case 10:
      num_entero_primo()
   case 11:
      palabra_al_reves()
   case 12:
      frase_letra()
   case 13:
      eco()
      
    