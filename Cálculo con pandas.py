import pandas as pd

datos = pd.Series([10, 20, 30, 40, 50])

desviacion = datos.std()
print("Desviación estándar: ", desviacion) 

varianza = datos.var()
print("Varianza:", varianza)

cantidad = datos.count()
suma = datos.sum()
print("Cantidad de datos:", cantidad)
print("Suma total:", suma)

elementos = datos.size
print("Cantidad total de elementos:", elementos)
