from Figura import Figura
from Rectangulo import Rectangulo
import math

class Circulo(Figura):
  def __init__(self, radio):
      self.radio = radio

  def area(self):
      return math.pi * (self.radio ** 2)