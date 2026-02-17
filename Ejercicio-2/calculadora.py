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
