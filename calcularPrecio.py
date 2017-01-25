'''
Created on 24/1/2017

Autores: Lalezka Duque, Marcos Jota
'''

import decimal
import math
import datetime
import sys

class Tarifa():
	def __init__(self,ds,fs):
		if((type(ds) is int or type(ds) is float) 
			and (type(fs) is int or type(fs) is float)):
			self.diasemana = decimal.Decimal(ds)
			self.finsemana = decimal.Decimal(fs)
		else:
			self.diasemana = -1
			self.finsemana = -1

# Intervalo en horas: [1,168]
# tiempoDeServicio = [inicio_servicio,fin_servicio]
def calcularPrecio(tarifa, tiempoDeServicio):
	if(tarifa.diasemana < 0 or tarifa.finsemana < 0):
		return -1

	precio = 0
	inicio = tiempoDeServicio[0]
	fin = tiempoDeServicio[1]
	tiempo_total = fin - inicio
	dias_servicio = tiempo_total.days()
	horas_servicio = tiempo_total.days()*24 + tiempo_total.seconds()//3600
	segundos_servicio = tiempo_total.seconds()
	dia_inicio = inicio.weekday()
	dia_fin = fin.weekday()

	# Redondeamos las horas de servicio
	if(segundos_servicio % 3600 > 0):
		horas_servicio += 1
	if(dia_inicio == 4 and dia_fin == 0):
		horas_servicio += 1

	if(dias_servicio == 0 and segundos_servicio < 900):
		print("El tiempo de servicio fue menor a 15 minutos.")
		return -1
	elif(dias_servicio > 7):
		print("El tiempo de servicio fue mayor a 7 dias")
		return -1
	elif(((dia_inicio == 4 and dia_fin == 5) or
		(dia_inicio == 6 and dia_fin == 0)) and horas_servicio == 1):
		
		if(dia_inicio == 5 or dia_inicio == 6):
			precio += tarifa.finsemana
		else:
			precio += tarifa.diasemana
		
		if(dia_fin == 5 or dia_fin == 6):
			precio += tarifa.finsemana
		else:
			precio += tarifa.diasemana
	else:
		
		if(inicio.day == fin.day):
			
			if(dia_inicio == 5 or dia_inicio == 6):
				precio += decimal.Decimal(horas_servicio*tarifa.finsemana)
			else:
				precio += decimal.Decimal(horas_servicio*tarifa.diasemana)
		else:
			
			if(dia_inicio == 5 or dia_inicio == 6):
				precio += decimal.Decimal((24-inicio.hour())*tarifa.finsemana)
			else:
				precio += decimal.Decimal((24-inicio.hour())*tarifa.diasemana)
			
			horas_restantes = horas_servicio
			horas_restantes -= (24-inicio.hour())
    
			if(dia_inicio == 6):
				dia_actual = 0
			else:
				dia_actual = dia_inicio + 1
			if(horas_restantes < 24 and horas_restantes > 0):
				dias_restantes = 1
			else:
				dias_restantes = math.ceil(horas_restantes/24)
                
			while(dias_restantes > 0):

				if(dias_restantes == 1):
				
					if(dia_actual == 5 or dia_actual == 6):
						precio += decimal.Decimal(horas_restantes*tarifa.finsemana)
					else:
						precio += decimal.Decimal(horas_restantes*tarifa.diasemana)
				else:
					horas_restantes -= 24
				
					if(dia_actual == 5 or dia_actual == 6):
						precio += decimal.Decimal(24*tarifa.finsemana)
					else:
						precio += decimal.Decimal(24*tarifa.diasemana)
                        
				if(dia_actual == 6):
					dia_actual = 0
				else:
					dia_actual += 1
                                
				dias_restantes -= 1

	return precio