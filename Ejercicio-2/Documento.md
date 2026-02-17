#  Calculadora de Decimal a Binario, Octal y Hexadecimal :)
##  Explicación del código  

### Echo por: Brandon Estrada

---

##  1. Objetivo del Programa  

Este programa permite:

- Ingresar un número decimal.
- Convertirlo manualmente a:
  - Binario (base 2)
  - Octal (base 8)
  - Hexadecimal (base 16)
- Mostrar cada resultado en pantalla.

El procedimiento se realiza usando divisiones sucesivas y residuos.

---

##  2. Código Completo del Programa  

```python
numero_original = int(float(input("Ingresa el numero que deseas convertir: ")))

numero = numero_original
resultado_binario = ""

while numero > 0:
    residuo = numero % 2
    resultado_binario = str(residuo) + resultado_binario
    numero = numero // 2

numero = numero_original
resultado_octal = ""

while numero > 0:
    residuo = numero % 8
    resultado_octal = str(residuo) + resultado_octal
    numero = numero // 8

numero = numero_original
resultado_hex = ""
tabla_hex = "0123456789ABCDEF"

while numero > 0:
    residuo = numero % 16
    caracter = tabla_hex[residuo] 
    resultado_hex = caracter + resultado_hex 
    numero = numero // 16

print(f"Decimal: {numero_original}")
print(f"Octal: {resultado_octal}")
print(f"Hexadecimal: {resultado_hex}")
print(f"Binario: {resultado_binario}")
```

---

##  3. Explicación General del Funcionamiento  

### 🔹 Entrada del número

```python
numero_original = int(float(input("Ingresa el numero que deseas convertir: ")))
```

- `input()` permite al usuario ingresar el número.
- `float()` acepta números con decimales.
- `int()` convierte el valor a entero.
- Se guarda en `numero_original` para reutilizarlo.

---

### 🔹 Conversión a Binario (Base 2)

```python
numero = numero_original
resultado_binario = ""

while numero > 0:
    residuo = numero % 2
    resultado_binario = str(residuo) + resultado_binario
    numero = numero // 2
```

Proceso:
- Se divide entre 2.
- Se guarda el residuo.
- Se repite hasta que el número sea 0.
- Los residuos se agregan al inicio.

---

### 🔹 Conversión a Octal (Base 8)

```python
numero = numero_original
resultado_octal = ""

while numero > 0:
    residuo = numero % 8
    resultado_octal = str(residuo) + resultado_octal
    numero = numero // 8
```

Proceso:
- Se divide entre 8.
- Se guarda el residuo.
- Se forma el número octal agregando residuos al inicio.

---

### 🔹 Conversión a Hexadecimal (Base 16)

```python
numero = numero_original
resultado_hex = ""
tabla_hex = "0123456789ABCDEF"

while numero > 0:
    residuo = numero % 16
    caracter = tabla_hex[residuo] 
    resultado_hex = caracter + resultado_hex 
    numero = numero // 16
```

Proceso:
- Se divide entre 16.
- Se usa la tabla `"0123456789ABCDEF"` para representar valores mayores a 9.
- Se construye el resultado agregando caracteres al inicio.

---

### 🔹 Impresión de Resultados

```python
print(f"Decimal: {numero_original}")
print(f"Octal: {resultado_octal}")
print(f"Hexadecimal: {resultado_hex}")
print(f"Binario: {resultado_binario}")
```

Se muestran todos los valores convertidos usando f-strings.

---

##  4. Ejemplo de Ejecución  

```
Ingresa el numero que deseas convertir: 25
Decimal: 25
Octal: 31
Hexadecimal: 19
Binario: 11001
```

---

##  5. Conclusión  

Este programa demuestra cómo funcionan los sistemas de numeración:

- Base 2 → Computadoras  
- Base 8 → Sistemas antiguos  
- Base 16 → Programación  

Se utilizan:

- División entera `//`
- Residuo `%`
- Ciclos `while`
- Manejo de cadenas
- Tabla de conversión para hexadecimal
