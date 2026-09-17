from Empleado import Empleado 
from Gerente import Gerente 
from Vendedor import Vendedor

empleados = [Gerente("Ana", 3000), Vendedor("Carlos", 1200, 5000), Empleado("Pedro", 1000)]

for emp in empleados:
  print(f"Empleado: {emp.nombre} | Salario Total: ${emp.calcular_salario():.2f}")