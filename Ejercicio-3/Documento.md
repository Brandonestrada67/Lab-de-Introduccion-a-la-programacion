#  Sistema de Login en Python
## Echo por Brandon Estrada
### :)

Este programa simula un inicio de sesión con validaciones básicas de usuario y contraseña.

Permite hasta 3 intentos antes de bloquear la cuenta.

---

##  Características

El programa valida:

-  Usuario no vacío  
-  Usuario sin espacios (usando `chr(32)`)  
-  Usuario solo alfanumérico  
-  Contraseña mínimo 8 caracteres  
-  Contraseña con al menos una letra  
-  Contraseña con al menos un número  
-  Máximo 3 intentos  

---

##  Lógica del Programa
El sistema funciona con un ciclo `while`:

```python
while intentos < 3:
```

El usuario tiene hasta 3 oportunidades para ingresar correctamente sus credenciales.

---

##  Validaciones del Usuario

### 1️ No puede estar vacío

```python
if usuario == "":
```

Se verifica que el usuario no esté vacío.

---

### 2️ No debe contener espacios

```python
if chr(32) in usuario:
```

`chr(32)` representa el carácter espacio en ASCII.

---

### 3️ Solo letras y números

```python
usuario.isalnum()
```

Este método devuelve `True` si el texto contiene únicamente letras y números.

---

##  Validaciones de la Contraseña

### 1️ Mínimo 8 caracteres

```python
if len(contraseña) < 8:
```

Se usa `len()` para contar los caracteres.

---

### 2️ Debe contener al menos una letra y un número

Se recorre la contraseña:

```python
for c in contraseña:
```

Se utilizan:

```python
c.isalpha()   # Detecta letras
c.isdigit()   # Detecta números
```

Si falta alguno de los dos, la contraseña es inválida.

---

##  Comparación Final

Solo si el usuario y la contraseña son válidos:

```python
if usuario == "admin" and contraseña == "Admin2026":
```

Si coinciden:
- ✔ Acceso concedido

Si no:
- ❌ Acceso denegado
- Se suma un intento

---

##  Bloqueo

Si se alcanzan 3 intentos fallidos:

```python
if intentos == 3:
```

La cuenta se bloquea.

---

##  Código Completo

```python
intentos = 0

while intentos < 3:

    print("usuario")
    usuario = input("ingrese su usuario: ")

    usuario_valido = True

    if usuario == "":
        print("El usuario no puede estar vacío")
        usuario_valido = False

    if chr(32) in usuario:
        print("El usuario no debe contener espacios")
        usuario_valido = False

    if usuario.isalnum() == False:
        print("El usuario solo debe contener letras y números")
        usuario_valido = False


    print("contraseña")
    contraseña = input("ingrese su contraseña: ")

    contraseña_valida = True

    if len(contraseña) < 8:
        print("La contraseña debe tener mínimo 8 caracteres")
        contraseña_valida = False

    tiene_letra = False
    tiene_numero = False

    for c in contraseña:
        if c.isalpha():
            tiene_letra = True
        if c.isdigit():
            tiene_numero = True

    if tiene_letra == False or tiene_numero == False:
        print("La contraseña debe tener al menos una letra y un número")
        contraseña_valida = False


    if usuario_valido == True and contraseña_valida == True:
        if usuario == "admin" and contraseña == "Admin2026":
            print("Acceso concedido")
            break
        else:
            print("Acceso denegado")
            intentos += 1
    else:
        print("Datos inválidos")

if intentos == 3:
    print("Cuenta bloqueada")
```

---

##  Conclusión

Este proyecto de nuestro queridisimo lab demuestra el uso de:

- Ciclos `while`
- Condicionales `if`
- Métodos de cadenas
- Variables booleanas
- Validaciones básicas de seguridad
