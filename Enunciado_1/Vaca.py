from Animal import Animal
from Perro import Perro
from Gato import Gato

class Vaca(Animal):  
  def hacer_sonido(self):
    print(f"{self.nombre} dice: ¡Muuuu!")
      