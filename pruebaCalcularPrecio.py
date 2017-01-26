'''

Created on 26/01/2017

@author: marcosajc, lalezkadu

'''

import unittest
from calcularPrecio import *

class caseTesterCalcularPrecio(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testBisiesto(self):
		inicioDeServicio = datetime.datetime(2016,2,23,3,0,0)
		finDeServicio = datetime.datetime(2016,2,29,3,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(10,20)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 1920)

	def testNoBisiesto(self):
		inicioDeServicio = datetime.datetime(2016,2,23,3,0,0)
		finDeServicio = datetime.datetime(2016,2,28,3,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(10,20)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 1470)

	def testTiempoMin(self):
		inicioDeServicio = datetime.datetime(2015,10,23,9,45,0)
		finDeServicio = datetime.datetime(2015,10,23,10,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(1,2)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 1)

	def testTiempoMax(self):
		inicioDeServicio = datetime.datetime(2015,8,23,15,0,0)
		finDeServicio = datetime.datetime(2015,8,30,15,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(1,2)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 216)

	def testMinutosFrontera(self):
		inicioDeServicio = datetime.datetime(2015,2,17,0,0,0)
		finDeServicio = datetime.datetime(2015,2,17,0,59,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(1,2)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 1)

	def testHorasFrontera(self):
		inicioDeServicio = datetime.datetime(2015,1,15,0,0,0)
		finDeServicio = datetime.datetime(2015,1,15,23,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(1,2)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 23)

	def testMedianochesEnSemana(self):
		inicioDeServicio = datetime.datetime(2015,3,24,0,0,0)
		finDeServicio = datetime.datetime(2015,3,25,0,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(1,2)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 24)

	def testMedianochesFinSemana(self):
		inicioDeServicio = datetime.datetime(2015,3,12,0,0,0)
		finDeServicio = datetime.datetime(2015,3,13,0,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(1,2)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 48)

	def testTarifaMinEnSemana(self):
		inicioDeServicio = datetime.datetime(2015,4,13,12,0,0)
		finDeServicio = datetime.datetime(2015,4,13,13,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(0,2)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 0)

	def testTarifaMinFinSemana(self):
		inicioDeServicio = datetime.datetime(2015,4,16,12,0,0)
		finDeServicio = datetime.datetime(2015,4,16,13,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(2,0)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 0)

	def testTarifaDecimalEnSemana(self):
		inicioDeServicio = datetime.datetime(2015,6,15,13,0,0)
		finDeServicio = datetime.datetime(2015,6,15,15,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(2.56,5)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), decimal.Decimal(2)*decimal.Decimal(2.56))

	def testTarifaDecimalFinSemana(self):
		inicioDeServicio = datetime.datetime(2015,6,18,13,0,0)
		finDeServicio = datetime.datetime(2015,6,18,15,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(5,3.78)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), decimal.Decimal(2)*decimal.Decimal(3.78))


	def testTarifasDEcimalAmbas(self):
		inicioDeServicio = datetime.datetime(2015,6,15,13,0,0)
		finDeServicio = datetime.datetime(2015,6,15,15,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(2.56,3.56)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), decimal.Decimal(2)*decimal.Decimal(2.56))

	def testTarifasDEcimalDouble(self):
		inicioDeServicio = datetime.datetime(2015,6,15,13,0,0)
		finDeServicio = datetime.datetime(2015,6,15,15,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(2.123456789,3.987654321)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), decimal.Decimal(2)*decimal.Decimal(2.123456789))

	def testEntreSemanas(self):
		inicioDeServicio = datetime.datetime(2015,8,6,20,0,0)
		finDeServicio = datetime.datetime(2015,8,7,4,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(3,4)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 32)

	def testEntreMeses(self):
		inicioDeServicio = datetime.datetime(2015,10,31,15,0,0)
		finDeServicio = datetime.datetime(2015,11,2,15,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(3,4)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 48*3)

	def testEntreAnios(self):
		inicioDeServicio = datetime.datetime(2015,12,31,9,0,0)
		finDeServicio = datetime.datetime(2016,1,1,9,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(3,4)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 7)

	def testEntreEnSemanayFinSemana(self):
		inicioDeServicio = datetime.datetime(2015,4,29,23,59,0)
		finDeServicio = datetime.datetime(2015,4,30,0,14,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(3,4)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 7)

	def testViernesALunes(self):
		inicioDeServicio = datetime.datetime(2015,5,13,23,45,0)
		finDeServicio = datetime.datetime(2015,5,16,0,15,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(3,4)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 3+48*4+3)

	def testTarifaNegativaEnSemana(self):
		inicioDeServicio = datetime.datetime(2015,4,28,8,0,0)
		finDeServicio = datetime.datetime(2015,4,28,10,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(-6,9)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), -1)

	def testTarifaNegativaFinSemana(self):
		inicioDeServicio = datetime.datetime(2015,4,28,8,0,0)
		finDeServicio = datetime.datetime(2015,4,28,10,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(9,-6)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), -1)

	def testTarifaCaracterEnSemana(self):
		inicioDeServicio = datetime.datetime(2015,4,28,8,0,0)
		finDeServicio = datetime.datetime(2015,4,28,10,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa("a",9)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), -1)

	def testTarifaCaracterFinSemana(self):
		inicioDeServicio = datetime.datetime(2015,4,28,8,0,0)
		finDeServicio = datetime.datetime(2015,4,28,10,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(9,"a")
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), -1)

	def testInicioMayorQueFin(self):
		inicioDeServicio = datetime.datetime(2015,7,8,8,0,0)
		finDeServicio = datetime.datetime(2015,7,7,10,0,0)
		tiempoDeServicio = [inicioDeServicio, finDeServicio]
		tarifaActual = Tarifa(3,2)
		self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), -1)

if __name__ == '__main__':
	unittest.main()