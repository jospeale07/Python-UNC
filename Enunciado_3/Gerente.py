from Empleado import Empleado  

class Gerente(Empleado):
  def __init__(self, nombre, salario_base):
    super().__init__(nombre, salario_base)

  def calcular_salario(self):
    return self.salario_base * 1.30  
      