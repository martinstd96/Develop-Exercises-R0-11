import math

class Circulo:
  """
  Construye una figura geométrica de tipo Circulo, la cual
  no puede tener un radio menor o igual a cero. En este
  caso, se lanza una excepción de tipo ValueError.
  Radio es un numero entero mayor que cero.
  """
  def __init__(self, radio):
    """
    >>> Circulo(4)
    Circulo(radio=4)
    >>> Circulo(-1)
    Traceback (most recent call last):
        ...
    ValueError: El radio no debe ser menor o igual a cero
    """
    self._es_cero_o_negativo(radio, 'El radio no debe ser menor o igual a cero')
    self.radio = radio
  
  """
  Devuelve una representacion del circulo amigable para
  cuando se imprime el objeto.
  """
  def __str__(self):
    """
    >>> cir = Circulo(4)
    >>> print(cir)
    Círculo de radio: 4
    """
    return f'Círculo de radio: {self.radio}'
  
  """
  Devuelve una representacion del circulo amigable para
  cuando se quiera ver al circulo instanciado.
  """
  def __repr__(self):
    """
    >>> Circulo(4)
    Circulo(radio=4)
    >>> cir = Circulo(4)
    >>> cir
    Circulo(radio=4)
    """
    return f"Circulo(radio={self.radio})"
  
  """
  Multiplica al radio del circulo por un número entero
  mayor a cero. En el caso de que el número sea menor o
  igual a cero, se lanza una excepción de tipo ValueError.
  Devuelve una nueva instancia de la clase Circulo con el
  nuevo radio (el radio anterior multiplicado por n).
  """
  def __mul__(self, n):
    """
    >>> cir = Circulo(3)
    >>> cir * 4
    Circulo(radio=12)
    >>> cir * 0
    Traceback (most recent call last):
        ...
    ValueError: No se puede multiplicar al radio por un número menor o igual a cero
    """
    self._es_cero_o_negativo(n, 'No se puede multiplicar al radio por un número menor o igual a cero')
    return Circulo(self.radio * n)

  """
  Lanza una excepción de tipo ValueError con el mensaje
  que se le pasa como parámetro si el numero es menor
  o igual a cero.
  """
  def _es_cero_o_negativo(self, numero, mensaje):
    if numero <= 0:
        self._lanzar_value_error(mensaje)
  
  """
  Lanza una excepción de tipo ValueError con el mensaje
  que se le pasa por parametro.
  """
  def _lanzar_value_error(self, mensaje):
    raise ValueError(mensaje)

  """
  Modifica el radio del circulo.
  Valor debe ser un número entero mayor que cero.
  En el caso de que el número sea menor o igual a cero,
  se lanza una excepción de tipo ValueError.
  """
  def modificar_radio(self, valor):
    """
    >>> cir = Circulo(2)
    >>> cir.modificar_radio(3)
    >>> cir
    Circulo(radio=3)
    >>> cir.modificar_radio(-2)
    Traceback (most recent call last):
        ...
    ValueError: El radio no debe ser menor o igual a cero
    """
    self._es_cero_o_negativo(valor, 'El radio no debe ser menor o igual a cero')
    self.radio = valor
  
  """
  Devuelve el area del circulo.
  """
  def obtener_area(self):
    """
    >>> cir = Circulo(3)
    >>> cir.obtener_area()
    28.274333882308138
    """
    return (self.radio ** 2) * math.pi
  
  """
  Devuelve el perímetro del circulo.
  """
  def obtener_perimetro(self):
    """
    >>> cir = Circulo(3)
    >>> cir.obtener_perimetro()
    18.84955592153876
    """
    return self.radio * 2 * math.pi

if __name__ == "__main__":
    import doctest
    doctest.testmod()