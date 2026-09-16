# 2) Crea una clase base llamada Figura con un método area() que devuelva 0.
#    Después crea las clases hijas:

#    - Rectángulo -> recibe base y altura, y calcula su área.
#    - Círculo -> recibe radio y calcula su área (usa math.pi). 
#    - Triángulo -> recibe base y altura, y calcula su área.

# Requisitos:

#    - Cada figura debe heredar de "Figura".
#    - Guarda las figuras en una lista y muestra el área de cada una.

#SOLUCION:

import math

class Figura:
  def area(self):
    return 0