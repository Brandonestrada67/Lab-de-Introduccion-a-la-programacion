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
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    if usuario == "":
        print("Error: Usuario vacío.")
    
    elif chr(32) in usuario:
        print("Error: El usuario no puede tener espacios.")

    elif len(clave) < 8:
        print("Error: La contraseña es muy corta (mínimo 8).")
        continue

    for letra in clave:
        if letra.isdigit():
            print("La contraseña debe contener al menos una letra.")
            break

        elif letra.isalpha():
            print("La contraseña debe contener al menos un numero.")
            break

    else:
        continue
    if usuario == "admin" and clave == "admin2026":
            print("¡Acceso concedido!")
            intentos = 0 
            break 
    else:
        intentos = intentos + 1
        print("Datos incorrectos.")
        print("Te quedan", 3 - intentos, "intentos.")

if intentos == 3:
    print("SISTEMA BLOQUEADO")
```

---

##  Conclusión

Este proyecto de nuestro queridisimo lab demuestra el uso de:

- Ciclos `while`
- Condicionales `if`
- Métodos de cadenas
- Variables booleanas
- Validaciones básicas de seguridad
