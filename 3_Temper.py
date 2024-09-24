#Convertir una temperatura de grados Celsius C a Fahrenheit F . F ́ormula:F = 9/5 C + 32

def Temperatura(C):
   F= 9*C/5 + 32
   return F

C=float (input("Ingrese la temperatura en Celsius:"))


x=Temperatura(C)
print("La temperatura en Celsius",C, "es equivalente a",x,"Fahrenheit.")