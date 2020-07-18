
# modulo de fecha
import datetime

# fecha actualcon hora minutos y segundos
fecha_actual = datetime.datetime.today()
print(fecha_actual)

# fecha actual hora minutos y segundos
fecha_actual2 = datetime.datetime.now()
print(fecha_actual2)

# obtener año
ano = fecha_actual2.year
print(ano)

# obtener mes
mes = fecha_actual2.month
print(mes)

# obtener dia
dia = fecha_actual2.day
print(dia)

# strftime(param) se le pasa un parametro (ver documentacion) y arroja un resultado
# ver nombre del dia completo ejemplo
dia_completo = fecha_actual2.strftime("%A") 
print(dia_completo)

# importando modulo
from mi_modulo import Suma, saludo_cordial

Suma(10, 19)
saludo_cordial("Diana Laura")