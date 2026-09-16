from Figura import Figura
from Rectangulo import Rectangulo  
from Circulo import Circulo  

class Triangulo(Figura):
  def __init__(self, base, altura):
      self.base = base
      self.altura = altura

  def area(self):
      return (self.base * self.altura) / 2