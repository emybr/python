from enum import Enum

class Antiguedad(Enum):
    MENOS_DE_2_AÑOS = 1
    DE_2_A_5_AÑOS = 2
    MAS_DE_5_AÑOS = 3

class TipoEmpleado(Enum):
    SALARIO_FIJO = 1
    COMISION = 2

class Empleado:
    def __init__(self, dni, nombre, apellido, año_ingreso, tipo, antiguedad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.año_ingreso = año_ingreso
        self.tipo = tipo
        self.antiguedad = antiguedad

    def obtener_salario(self):
        pass

class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, año_ingreso, salario_minimo, clientes_captados, monto_por_cliente, antiguedad):
        super().__init__(dni, nombre, apellido, año_ingreso, TipoEmpleado.COMISION, antiguedad)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def obtener_salario(self):
        salario = self.clientes_captados * self.monto_por_cliente
        return max(salario, self.salario_minimo)

class EmpleadoSalarioFijo(Empleado):
    def __init__(self, dni, nombre, apellido, año_ingreso, sueldo_basico, porcentaje_adicional, antiguedad):
        super().__init__(dni, nombre, apellido, año_ingreso, TipoEmpleado.SALARIO_FIJO, antiguedad)
        self.sueldo_basico = sueldo_basico
        self.porcentaje_adicional = porcentaje_adicional

    def obtener_salario(self):
        if self.antiguedad == Antiguedad.MAS_DE_5_AÑOS:
            return self.sueldo_basico * 1.1
        elif self.antiguedad == Antiguedad.DE_2_A_5_AÑOS:
            return self.sueldo_basico * 1.05
        else:
            return self.sueldo_basico

def mostrarSalarios(empleados):
    for empleado in empleados:
        salario = empleado.obtener_salario()
        print(f"Empreado: {empleado.nombre} {empleado.apellido}: Salario: ${salario:.2f}")


empleados = [
    EmpleadoComision(12345678, "Juan", "Perez", 2019, 1000, 20, 50, Antiguedad.MENOS_DE_2_AÑOS),
    EmpleadoComision(23456789, "Maria", "Gomez", 2018, 1200, 15, 60, Antiguedad.MAS_DE_5_AÑOS),
    EmpleadoComision(34567890, "Pedro", "Lopez", 2020, 1100, 25, 45, Antiguedad.DE_2_A_5_AÑOS),
    EmpleadoComision(45678901, "Laura", "Martinez", 2017, 1500, 30, 55, Antiguedad.MAS_DE_5_AÑOS),
    EmpleadoSalarioFijo(56789012, "Ana", "Rodriguez", 2016, 2000, 0.05, Antiguedad.MAS_DE_5_AÑOS),
    EmpleadoSalarioFijo(67890123, "Carlos", "Sanchez", 2015, 1800, 0.1, Antiguedad.MAS_DE_5_AÑOS),
    EmpleadoSalarioFijo(78901234, "Sofia", "Diaz", 2014, 2200, 0.05, Antiguedad.MAS_DE_5_AÑOS),
    EmpleadoSalarioFijo(89012345, "Diego", "Garcia", 2013, 2500, 0.1, Antiguedad.MAS_DE_5_AÑOS),
    EmpleadoSalarioFijo(90123456, "Julia", "Fernandez", 2012, 2300, 0.05, Antiguedad.MAS_DE_5_AÑOS),
    EmpleadoSalarioFijo(12345670, "Lucas", "Lopez", 2011, 2400, 0.1, Antiguedad.MAS_DE_5_AÑOS)
]


mostrarSalarios(empleados)
