Artist={"Aiden":3, "Britney":20, "Christina":12, "David":8, "Elvis":30, "Feid":3}
Artist.keys() ##imprime la lista con las Keys
Artist.values()

#Para imprimir Keys
for k in Artist:
    print(k)

for k in Artist.keys():
    print(k)

#Para imprimir Values
for k in Artist.values():
    print(k)
    
for k in Artist:
    print(Artist[k])
    
for k in Artist:
    print("El artista", k, "tiene", Artist[k],"discos.")
    
Artist2={"Aiden":[3,"WA"], "Britney":[20, "PA"], "Christina":[12,"NM"],
         "David":[8,"NY"], "Elvis":[30, "IA"], "Feid":[3,"CO"]}

for k in Artist2:
    print("El artista", k, "tiene", Artist2[k][0],
          "discos y vive en",Artist2[k][1])
print("David" in Artist2.keys())        