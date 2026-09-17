# 3) Crea una clase base Empleado con los atributos nombre y salario_base, 
# y un método calcular_salario() que devuelva el salario base.

# Crea dos clases hijas:
 
#   - Gerente -> su salario es el base + un bono del 30%.
#   - Vendedor -> su salario es el base + una comisión del 10% sobre las ventas realizadas (atributo adicional ventas).

# Requisitos:

#   - Usa super.__init__() en las clases hijas.
#   - Crea una lista con varios empleados y muestra cuánto gana cada uno.

#SOLUCION:

class Empleado:
  def __init__(self, nombre, salario_base):
      self.nombre = nombre
      self.salario_base = salario_base
    
  def calcular_salario(self):
    return self.salario_base