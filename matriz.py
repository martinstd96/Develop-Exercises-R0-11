import numpy as np
#python3 -m doctest circulo.py -v

"""
Recibe una lista de tuplas (las cuales contienen un numero
de una fila o columna, un contador, y las posiciones de la
fila y columna en donde se encuentra en la matriz), una
tupla de tuplas (que contienen las posiciones de la lista
de tuplas de la posicion inicial de la fila o columna de
los numeros consecutivos), y una tupla de dos elementos 
(que contiene la ultima posicion de la fila y columna de 
los numeros consecutivos).
"""
def imprimir_fila_columna(lista_memoria, pos_inicial, pos_final):
  fila_inicial, columna_inicial = pos_inicial
  i, j = pos_final
  print(f"Fila inical: {lista_memoria[fila_inicial[0]][fila_inicial[1]]}")
  print(f"Columna inicial: {lista_memoria[columna_inicial[0]][columna_inicial[1]]}")
  print(f"Fila final: {i}")
  print(f"Columna final: {j}")

"""
Recibe una lista de tuplas (las cuales contienen un numero
de una fila o columna, un contador, y las posiciones de la
fila y columna en donde se encuentra en la matriz), una
matriz de numeros enteros donde se quiere buscar numeros
consecutvios, la posicion de una determinada fila y columna
de la matriz.
Devuelve True si el numero anterior al segundo elelemnto
de la fila o columna actual es consecutivo a él. False
en caso contrario.
"""
def segundo_elemento_no_es_consecutivo(lista_memoria, matriz, pos_fila, pos_columna):
  return (lista_memoria[-1][0] != matriz[pos_fila][pos_columna] - 1) and (lista_memoria[-1][1] == 0)

"""
Devuelve una matriz de 5x5 de numeros enteros aleatorios,
salvo en la ultima fila, donde se agrega una fila de
numeros enteros en particular.
"""
def obtener_matriz_con_fila_agregada():
  matriz = obtener_matriz(4, 5)
  return np.append(matriz, [[1, 2, 3, 4, 8]], axis=0)

"""
Devuelve una matriz de 5x5 de numeros enteros aleatorios,
salvo en la primera columna, donde se agrega una columna
de numeros enteros en particular.
"""
def obtener_matriz_con_columna_agregada():
  matriz = obtener_matriz(5, 4)
  return np.insert(matriz, [0],[[8], [2], [3], [4], [5]], axis=1)

"""
Devuelve una matriz de tam_filasXtam_columnas de numeros
enteros aleatorios.
"""
def obtener_matriz(tam_filas, tam_columnas):
  return np.random.randint(1,20, size=(tam_filas, tam_columnas))

"""
Recibe una cadena de caracteres, la cual permite agregar
a la matriz (de donde se quiere obtener una secuencia de 4
numeros consecutivos ya sea en una columna o en una fila)
una fila o una columna de numeros enteros en particular
para poder testear el algoritmo que calcula los numeros
consecutivos.
"""
def obtener_secuencia_4_numeros_consecutivos(agregar="Nada"):
  """
  >>> obtener_secuencia_4_numeros_consecutivos("Fila")
  Fila inical: 4
  Columna inicial: 0
  Fila final: 4
  Columna final: 3
  >>> obtener_secuencia_4_numeros_consecutivos("Columna")
  Fila inical: 1
  Columna inicial: 0
  Fila final: 4
  Columna final: 0
  >>> obtener_secuencia_4_numeros_consecutivos()
  No se han encontrado numeros consecutivos
  """
  matriz = []
  if agregar == "Fila":
    matriz = obtener_matriz_con_fila_agregada()
  
  elif agregar == "Columna":
    matriz = obtener_matriz_con_columna_agregada()
  
  else:
    matriz = obtener_matriz(5, 5)

  #esto es para las filas (horizontal)
  for i in range(len(matriz)):
    contador = 0
    lista_memoria = []
    for j in range(len(matriz[0])):
      if len(lista_memoria) != 0:
        if segundo_elemento_no_es_consecutivo(lista_memoria, matriz, i, j):
          lista_memoria.append((matriz[i][j], contador, i, j))
          contador += 1
          continue
        if lista_memoria[-1][0] != matriz[i][j] - 1:
          break;
        if contador == 3:
          if lista_memoria[0][0] == lista_memoria[1][0] -1:
            imprimir_fila_columna(lista_memoria, ((0, 2), (0, 3)), (i, j))
            return
        if contador == 4:
          imprimir_fila_columna(lista_memoria, ((1, 2), (1, 3)), (i, j))
          return
      
      lista_memoria.append((matriz[i][j], contador, i, j))
      contador += 1
  #esto es para las columnas (vertical)
  for j in range(len(matriz[0])):
    contador = 0
    lista_memoria = []
    for i in range(len(matriz)):
      if len(lista_memoria) != 0:
        if segundo_elemento_no_es_consecutivo(lista_memoria, matriz, i, j):
          lista_memoria.append((matriz[i][j], contador, i, j))
          contador += 1
          continue
        if lista_memoria[-1][0] != matriz[i][j] - 1:
          break;
        if contador == 3:
          if lista_memoria[0][0] == lista_memoria[1][0] -1:
            imprimir_fila_columna(lista_memoria, ((0, 2), (0, 3)), (i, j))
            return
        if contador == 4:
          imprimir_fila_columna(lista_memoria, ((1, 2), (1, 3)), (i, j))
          return
      
      lista_memoria.append((matriz[i][j], contador, i, j))
      contador += 1
  
  print(f"No se han encontrado numeros consecutivos")

if __name__ == "__main__":
    import doctest
    doctest.testmod()