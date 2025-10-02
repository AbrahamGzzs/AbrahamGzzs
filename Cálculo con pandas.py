import pandas as pd

datos = pd.Series([10, 20, 30, 40, 50])

desviacion = datos.std()
print("Desviación estándar: ", desviacion) 