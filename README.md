- 👋 Hi, I’m @JosRmrz
- 👀 Soy estudiante de Ing. electrica electronica...
- 🌱 I’m currently learning muchas cosas geniales entre ellas programacion y estos son mis codigos
JosRmrz/JosRmrz
SEGUNDO PARCIAL EJERCICIO 1 Y 2
import pandas as pd
datos =        [["TUTO",20],
                ["JUAN",27],
                ["GABRIEL",39],
                ["ALISSON",17],
                ["EBERTO", 55],
                ["ROSA", 34],
                ["JESUS", 45],
                ["JOSE", 18],
                ["MARIO", 33],
                ["CARMEN",29]]
columnas =['Alumno','Edad']
df = pd.DataFrame(datos,columns=columnas,)
porprom = df.sort_values('Edad',ascending=False)                                                                       
porprom.head()
arx = porprom.iloc[0,:]
print ("La lista ingresada es la siguiente:")
print (df)
print()
print("El familiar con mayor edad es:")
print(arx)
