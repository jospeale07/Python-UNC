# 1) Crea una clase base llamada Animal que tenga los atributos nombre y edad,
# y un método llamado hacer_sonido() que imprima un mensaje genérico.
# Luego, crea tres clases hijas que hereden de Animal:

#    - Perro -> su sonido es "¡Guau guau!"
#    - Gato -> su sonido es "¡Miau Miau!"
#    - Vaca -> su sonido es "¡Muuuu!"

# Requisitos:

#    - Cada clase hija debe sobreescribir el método hacer_sonido()
#    - Crea una lista con un objeto de cada tipo y recórrela llamando al método hacer_sonido()

#SOLUCION:

class Animal:
  def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad
  hacer_sonido(f"El animal {self.nombre} dice ")  