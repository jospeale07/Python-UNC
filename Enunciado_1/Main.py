from Animal import Animal
from Perro import Perro
from Gato import Gato
from Vaca import Vaca 

animales = [
  Perro("Inu", 3)
  Gato("Neko", 2)
  Vaca("Ushi", 5)
]

for animal in animales:
  animal.hacer_sonido()