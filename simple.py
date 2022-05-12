import random

"""
Devuelve un lista de 10 diccionarios, donde
los id van de 1 a 10 y las edades son un nº
entero aleatorio entre 1 y 100.
"""
def obtener_id_edades_random():
  return [{"id":i, "edad":random.randint(1,100)} 
          for i in range(1,11)]

"""
Recibe una lista de diccionarios (los cuales deben tener
un id y una edad), ordena dicha lista por edad de mayor
a menor e imprime el id de la persona más joven y el id de
la persona más vieja.
"""
def ordenar_edades_mayor_a_menor(lista_diccionarios):
  """
  >>> random.seed(111)
  >>> ordenar_edades_mayor_a_menor(obtener_id_edades_random())
  El id de la persona más joven es: 8 y el id de la persona más vieja es: 9
  >>> ordenar_edades_mayor_a_menor(obtener_id_edades_random())
  El id de la persona más joven es: 5 y el id de la persona más vieja es: 10
  >>> ordenar_edades_mayor_a_menor(obtener_id_edades_random())
  El id de la persona más joven es: 9 y el id de la persona más vieja es: 6
  """
  resultado = sorted(lista_diccionarios, key= lambda dic: dic["edad"], reverse=True)
  print(f"El id de la persona más joven es: {resultado[-1]['id']} y el id de la persona más vieja es: {resultado[0]['id']}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()