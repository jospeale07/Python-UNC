from Figura import Figura
from Rectangulo import Rectangulo  
from Circulo import Circulo  
from Triangulo import Triangulo  

figuras = [Rectangulo(10, 5), Circulo(4), Triangulo(6, 3)]

for figura in figuras:
  print(f"Area: {figura.area(): .2f}")