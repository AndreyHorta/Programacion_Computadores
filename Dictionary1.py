Nombres=["Aiden", "Britney", "Christina", "David", "Elvis", "Feid"]
Discos=[3,20,12,8,30,3]
Estado=["WA", "PA", "NM", "NY", "IA","CO"]



def indicador(Lista: list, Artist: str):
    contador=0
    for i in Lista:
        if i== Artist:
            return contador
        contador +=1
    return "Not found"

def Ubi(Lista: list,indice: int):
    y=Lista[indice]
    return y


b=(input("Ingrese el nombre del artista:"))


#print(x)

z=indicador(Nombres, b)
x=Ubi(Discos,z)
y=Ubi(Estado,z)
print("La cantidad de discos de",b, "son", x,\
      "y fueron publicados en el estado",y)
#print(z)
