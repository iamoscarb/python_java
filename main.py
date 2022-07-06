#programa principal 
#importamos las funciones del archivo files
from files import read_data, send_data 


#guarda los datos del archivo txt en una lista
data = read_data()
#manda los valores de la lista al localhost
send_data(data)
