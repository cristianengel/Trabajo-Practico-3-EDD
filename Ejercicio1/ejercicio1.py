import re

# Números válidos
num1 = "3454218963"
num2 = "+5493454213320"
num3 = "(0345) 154219230"

# Números no válidos
num4 = "34542172101"
num5 = "+5493452213210"
num6 = "(0346) 154217230"

patron = "\(0345\)\s154[0-9]{6}|\+5493454[0-9]{6}|3454[0-9]{6}"

# Verifica que el número no sea mas largo de lo debido
def verificacion(num):
    if re.findall(patron, num) and num == re.findall(patron, num)[0]:
        print(f"Número: {num} | Válido")
    else:
        print(f"Número: {num} | Inválido")

verificacion(num1)
verificacion(num2)
verificacion(num3)
verificacion(num4)
verificacion(num5)
verificacion(num6)



