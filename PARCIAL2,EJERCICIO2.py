import pandas as pd
n = int(input("Ingrese el numero de familiares: "))
df = pd.DataFrame(columns=['Nombre', 'Edad'],
                  index=range(n))
for i in range(n):
    t = str(i)
    for k in range (2):
        q = str(k)
        x = input("Ingrese el valor de x"+ t + "," + q + ": ")
        df.iloc[i,k] = (x)

porprom = df.sort_values('Edad',ascending=False)
porprom.head()
arx = porprom.iloc[0,:]
print ("La lista ingresada es la siguiente:")
print (df)
print("El familiar con mayor edad es:")
print(arx)