import pandas

Artist3={"Nombres":["Aiden", "Britney", "Christina", "David", "Elvis", "Feid"],
"Discos":[3,20,12,8,30,3], "Estado":["WA", "PA", "NM", "NY", "IA","CO"]}

#print(Artist3)

df=pandas.DataFrame(Artist3)
print(df)
print(df.Nombres)
print(df.loc[3])




