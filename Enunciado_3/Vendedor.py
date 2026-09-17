from Empleado import Empleado 
from Gerente import Gerente  

class Vendedor(Empleado):
  def __init__(self, nombre, salario_base, ventas):
      super().__init__(nombre, salario_base)
      self.ventas = ventas

  def calcular_salario(self):
    return self.salario_base + (self.ventas * 0.10)