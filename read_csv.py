import csv

def read_csv(path): #Con esta función abrimos el archivo, definimos el delimitador y los permisos
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader) #Con esto obtenemos la primera fila de forma manual al ser reader un iterable
    data = []
    for row in reader:
      iterable = zip(header, row) #Une el header con el dato y para luego convertir la lista en diccionario
      country_dict = {key: value for key, value in iterable} #Se convierte a diccionario
      data.append(country_dict)
    return data

if __name__ == "__main__":
  data = read_csv("./app/data.csv")
  print(data[0])#vemos como nos queda el diccionaio, para el ejemplo tomamos solo la información de la posición 0