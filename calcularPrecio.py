'''
Created on 24/1/2017

Autores: Lalezka Duque, Marcos Jota
'''

import decimal
import math
import datetime
import sys

# Clase Tarifa
# Almacena las tarifas correspondientes a la hora de servicio en los días de
# la semana
# Atributos:
# ds: tarifa de los dias entre semana
# fs: tarfia de los fines de semana
class Tarifa():
	def __init__(self, ds, fs):
		if ((type(ds) is int or type(ds) is float) 
			and (type(fs) is int or type(fs) is float)):
			self.diasemana = decimal.Decimal(ds)
			self.finsemana = decimal.Decimal(fs)
		else:
			self.diasemana = -1
			self.finsemana = -1

# Determina el precio de un servicio
# Parametros:
# tarifa: instancia de la clase Tarifa que contiene las tarifas por hora de 
# servicio
# tiempoDeServicio: Lista que contiene el tiempo de inicio del servicio y
# el tiempo en el cual termino el servicio
# Retorna el precio total por el tiempo de servicio.
def calcularPrecio(tarifa, tiempoDeServicio):
	# Las tarifas son numeros enteros positivos
	if (tarifa.diasemana < 0 or tarifa.finsemana < 0):
		return -1

	precio = 0																# Precio total inicial
	inicio = tiempoDeServicio[0]											# Inicio del servicio
	fin = tiempoDeServicio[1]												# Fin del servicio

	tiempo_total = fin - inicio 											# Tiempo total de servicio
	dias_servicio = tiempo_total.days										# Tiempo de servicio en dias
	horas_servicio = tiempo_total.days*24+tiempo_total.seconds//3600		# Tiempo de servicio en horas
	segundos_servicio = tiempo_total.seconds								# Tiempo de servicio en segundos
	dia_inicio = inicio.weekday()											# Dia en el cual inicio el servicio
	dia_fin = fin.weekday()													# Dia en el cual finalizo el servicio

	# Redondeamos las horas de servicio
	if (segundos_servicio % 3600 > 0):
		horas_servicio += 1
	if (dia_inicio == 4 and dia_fin == 0):
		horas_servicio += 1

	if (dias_servicio == 0 and segundos_servicio < 900):	# Verificamos que el tiempo de servicio se encuentra en el dominio
		print("El tiempo de servicio fue menor a 15 minutos.")
		return -1
	elif (dias_servicio > 7):
		print("El tiempo de servicio fue mayor a 7 dias")
		return -1
	elif (((dia_inicio == 4 and dia_fin == 5) 				# Calculo del precio
		or (dia_inicio == 6 and dia_fin == 0)
		or (dia_inicio == 5 and dia_fin == 6)) 				# Servicio de una hora en fin de semana
		and horas_servicio == 1):
		if (dia_inicio == 5 or dia_inicio == 6):			# Fin de semana
			precio += tarifa.finsemana
		else:												# Entre semana
			precio += tarifa.diasemana
		
		if (dia_fin == 5 or dia_fin == 6):					# Fin de semana
			precio += tarifa.finsemana
		else:												# Entre semana
			precio += tarifa.diasemana
	else:
		if (inicio.day == fin.day):							# Servicio de un dia
			if (dia_inicio == 5 or dia_inicio == 6):		# Fin de semana
				precio += decimal.Decimal(horas_servicio*tarifa.finsemana)
			else:											# Entre semana
				precio += decimal.Decimal(horas_servicio*tarifa.diasemana)
		else:												# Servicio de varios dias de duracion
			if (dia_inicio == 5 or dia_inicio == 6):		# Servicio comienza fin de semana
				precio += decimal.Decimal((24-inicio.hour)*tarifa.finsemana)
			else:											# Servicio comienza entre semana
				precio += decimal.Decimal((24-inicio.hour)*tarifa.diasemana)
			
			horas_restantes = horas_servicio		
			horas_restantes -= (24-inicio.hour)			# Quitamos las horas ya calculadas
    		
    		# Actualizamos el dia siguiente
    		# Si comenzamos en Domingo, seguimos calculando desde el Lunes
			if (dia_inicio == 6):
				dia_actual = 0
			else:
				dia_actual = dia_inicio+1

			# Redondeo de los dias restantes de servicio
			if (horas_restantes < 24 and horas_restantes > 0):
				dias_restantes = 1
			else:
				dias_restantes = math.ceil(horas_restantes/24)
			# Iterando sobre los dias en los cuales se hizo servicio calculamos
            # el resto del precio hasta agotar los dias restantes por calcular
			while (dias_restantes > 0):

				if (dias_restantes == 1):			
					if (dia_actual == 5 or dia_actual == 6):
						precio += decimal.Decimal(horas_restantes*tarifa.finsemana)
					else:
						precio += decimal.Decimal(horas_restantes*tarifa.diasemana)
				else:
					horas_restantes -= 24
				
					if (dia_actual == 5 or dia_actual == 6):
						precio += decimal.Decimal(24*tarifa.finsemana)
					else:
						precio += decimal.Decimal(24*tarifa.diasemana)
                        
				if (dia_actual == 6):
					dia_actual = 0
				else:
					dia_actual += 1
                                
				dias_restantes -= 1

	return precio
