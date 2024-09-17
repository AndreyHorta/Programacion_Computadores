def AreaTri (b,h):
   y= b*h/2
   return y

h=int (input("Ingrese la altura del triangulo h:"))
b=int (input("Ingrese la base del triangulo b:"))


x=AreaTri(b,h)
print("El Area del triangulo de altura ",h, "y base ",b," es ", x)