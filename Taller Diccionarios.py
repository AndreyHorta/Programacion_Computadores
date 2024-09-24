diccionario = {
    "Alondra": {"Regresion": 3.4, "InteligenciaArtificial": 2.8},
    "Baltasar": {"Calculo": 2.0, "Probabilidad": 4.0},
    "Celestino": {"Bioestadistica": 1.0},
    "Doroteo": {"Programacion": 1.5, "Probabilidad": 2.5, "Bayesiana": 3.0},
    "Esperancita": {"Programacion": 1.0},
    "Fabiola": {"Multivariante": 3.2, "Probabilidad": 4.1, "HistoriaEst": 2.9}
}

##1. ¿Cómo accederías al valor asociado con la clave 'Calculo'
##en el diccionario anidado para 'Baltasar'?

print(diccionario["Baltasar"]["Calculo"])

##2. Escribe un bucle `for` en Python para iterar a través de todos los nombres
##en el diccionario e imprimir solo aquellos que tienen una clave 'Programación'
##en su diccionario anidado.

##Sirve para los Values
#for k in diccionario:
 #   for j in diccionario[k]:
  #      if diccionario[k][j]==3.4:
   #         print(k)
 
 
#print(diccionario["Alondra"].keys()) 
 
for k in diccionario:
    if "Programacion" in diccionario[k].keys():
            print(k)
            
##3. ¿Qué línea de código usarías para añadir un nuevo par clave-valor
##`'MineríaDatos': 3.5` al diccionario anidado de 'Alondra'?

diccionario["Alondra"]["MineríaDatos"]=3.5
print(diccionario["Alondra"])

##4. Si intentas acceder a una clave que no existe en el diccionario, como
##`diccionario['Alondra']['Estadística']`, ¿Qué ocurre y cómo puedes manejarlo?

##Sale un error: KeyError: 'Estadística'. Se podria crear la clave Estadistica e
## indagar por el valor asociado (nota)

b=(input("Ingrese la nota de Alondra en la case de Estadística:"))
diccionario["Alondra"]["Estadística"]=b
print(diccionario["Alondra"])

##5. Proporciona un ejemplo de cómo usar el método `get()` para obtener el valor
##de 'Bioestadística' en el diccionario de 'Celestino', con un valor
##predeterminado de `0` si la clave no existe.

print(diccionario["Celestino"].get("Calculo",0))

##6. ¿Qué comando usarías para eliminar la materia 'HistoriaEst'
##del diccionario de 'Fabiola'?

del diccionario["Fabiola"]["HistoriaEst"]
print (diccionario["Fabiola"])

## 7. Crea una función en Python que calcule y devuelva el promedio de todas las
##notas de un estudiante dado, tomando como argumento el nombre del estudiante.







def PromEstu(k):    
    contador=0
    suma=0
    for i in diccionario[k],values:
        contador +=1
        suma +=i
    return 

y=PromEstu("Celestino")

print ("El Promedio es ", suma/contador)