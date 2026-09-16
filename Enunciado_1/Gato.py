from Animal import Animal
from Perro import Perro

class Gato(Animal):  
  def hacer_sonido(self):
    print(f"{self.nombre} dice: ¡Miau Miau!")
      