'''
<<<<<<< HEAD
Created on 26/01/2017
@author: marcosajc, lalezkadu
=======
<<<<<<< HEAD
Created on 26/01/2017
@author: marcosajc, lalezkadu
=======

Created on 26/01/2017

@author: marcosajc, lalezkadu

>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
'''
import unittest
from calcularPrecio import *
from samba.samba3 import passdb

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

<<<<<<< HEAD
	def testNoBisiesto(self):
		inicioDeServicio = datetime.datetime(2017,2,23,3,0,0)
        finDeServicio = datetime.datetime(2017,2,28,3,0,0)
=======
<<<<<<< HEAD
	def testNoBisiesto(self):
		inicioDeServicio = datetime.datetime(2017,2,23,3,0,0)
        finDeServicio = datetime.datetime(2017,2,28,3,0,0)
=======
    def testNoBisiesto(self):
        inicioDeServicio = datetime.datetime(2016,2,23,3,0,0)
        finDeServicio = datetime.datetime(2016,2,28,3,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(10,20)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 1470)

	def testTiempoMin(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2015,10,23,9,45,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2015,10,23,9,45,0)
=======
        inicioDeServicio = datetime.datetime(2015,10,23,9,45,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        finDeServicio = datetime.datetime(2015,10,23,10,0,0)
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(1,2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 1)

<<<<<<< HEAD
	def testTiempoMax(self):
		inicioDeServicio = datetime.datetime(2015,8,23,15,0,0)
=======
<<<<<<< HEAD
	def testTiempoMax(self):
		inicioDeServicio = datetime.datetime(2015,8,23,15,0,0)
=======
    def testTiempoMax(self):
        inicioDeServicio = datetime.datetime(2015,8,23,15,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        finDeServicio = datetime.datetime(2015,8,30,15,0,0)
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(1,2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 216)

<<<<<<< HEAD
	def testMinutosFrontera(self):
		inicioDeServicio = datetime.datetime(2015,2,17,0,0,0)
=======
<<<<<<< HEAD
	def testMinutosFrontera(self):
		inicioDeServicio = datetime.datetime(2015,2,17,0,0,0)
=======
    def testMinutosFrontera(self):
        inicioDeServicio = datetime.datetime(2015,2,17,0,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
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
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,3,12,0,0,0)
        finDeServicio = datetime.datetime(2017,3,13,0,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,3,12,0,0,0)
        finDeServicio = datetime.datetime(2017,3,13,0,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,3,12,0,0,0)
        finDeServicio = datetime.datetime(2015,3,13,0,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(1,2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 48)    

	def testTarifaMinEnSemana(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,13,12,0,0)
        finDeServicio = datetime.datetime(2017,4,13,13,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,13,12,0,0)
        finDeServicio = datetime.datetime(2017,4,13,13,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,4,13,12,0,0)
        finDeServicio = datetime.datetime(2015,4,13,13,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(0,2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 0)

	def testTarifaMinFinSemana(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,16,12,0,0)
        finDeServicio = datetime.datetime(2017,4,16,13,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,16,12,0,0)
        finDeServicio = datetime.datetime(2017,4,16,13,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,4,16,12,0,0)
        finDeServicio = datetime.datetime(2015,4,16,13,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(2,0)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 0)

	def testTarifaDecimalEnSemana(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,6,15,13,0,0)
        finDeServicio = datetime.datetime(2017,6,15,15,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,6,15,13,0,0)
        finDeServicio = datetime.datetime(2017,6,15,15,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,6,15,13,0,0)
        finDeServicio = datetime.datetime(2015,6,15,15,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(2.56,5)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 
                          decimal.Decimal(2)*decimal.Decimal(2.56))

	def testTarifaDecimalFinSemana(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,6,18,13,0,0)
        finDeServicio = datetime.datetime(2017,6,18,15,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,6,18,13,0,0)
        finDeServicio = datetime.datetime(2017,6,18,15,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,6,18,13,0,0)
        finDeServicio = datetime.datetime(2015,6,18,15,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(5,3.78)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 
                          decimal.Decimal(2)*decimal.Decimal(3.78))
        
	def testTarifasDecimalAmbas(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,6,15,13,0,0)
        finDeServicio = datetime.datetime(2017,6,15,15,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,6,15,13,0,0)
        finDeServicio = datetime.datetime(2017,6,15,15,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,6,15,13,0,0)
        finDeServicio = datetime.datetime(2015,6,15,15,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(2.56,3.56)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 
                          decimal.Decimal(2)*decimal.Decimal(2.56))
        
	def testTarfiasDecimalDouble(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,6,15,13,0,0)
        finDeServicio = datetime.datetime(2017,6,15,15,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,6,15,13,0,0)
        finDeServicio = datetime.datetime(2017,6,15,15,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,6,15,13,0,0)
        finDeServicio = datetime.datetime(2015,6,15,15,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(2.123456789,3.987654321)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 
                          decimal.Decimal(2)*decimal.Decimal(2.123456789))
        
	def testEntreSemanas(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,8,6,20,0,0)
        finDeServicio = datetime.datetime(2017,8,7,4,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,8,6,20,0,0)
        finDeServicio = datetime.datetime(2017,8,7,4,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,8,6,20,0,0)
        finDeServicio = datetime.datetime(2015,8,7,4,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(3,4)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 8*4)
        
	def testEntreMeses(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,10,31,15,0,0)
        finDeServicio = datetime.datetime(2017,11,2,15,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,10,31,15,0,0)
        finDeServicio = datetime.datetime(2017,11,2,15,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,10,31,15,0,0)
        finDeServicio = datetime.datetime(2015,11,2,15,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(3,4)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 48*3)
        
	def testEntreAnios(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,12,31,9,0,0)
        finDeServicio = datetime.datetime(2017,1,1,9,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,12,31,9,0,0)
        finDeServicio = datetime.datetime(2017,1,1,9,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,12,31,9,0,0)
        finDeServicio = datetime.datetime(2015,1,1,9,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(3,4)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), 24*4)
        
	def testEntreEnSemanayFinSemana(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,29,23,59,0)
        finDeServicio = datetime.datetime(2017,4,30,0,14,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,29,23,59,0)
        finDeServicio = datetime.datetime(2017,4,30,0,14,0)
=======
		inicioDeServicio = datetime.datetime(2015,4,29,23,59,0)
        finDeServicio = datetime.datetime(2015,4,30,0,14,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(3,4)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), (1*3)+(1*4))
        
	def testViernesALunes(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,5,13,23,45,0)
        finDeServicio = datetime.datetime(2017,5,16,0,15,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,5,13,23,45,0)
        finDeServicio = datetime.datetime(2017,5,16,0,15,0)
=======
		inicioDeServicio = datetime.datetime(2015,5,13,23,45,0)
        finDeServicio = datetime.datetime(2015,5,16,0,15,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(3,4)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), (1*3)+(48*4)+(1*3))
        
	def testTarifaNegativaEnSemana(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,28,8,0,0)
        finDeServicio = datetime.datetime(2017,4,28,10,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,28,8,0,0)
        finDeServicio = datetime.datetime(2017,4,28,10,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,4,28,8,0,0)
        finDeServicio = datetime.datetime(2015,4,28,10,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(-6,9)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), -1)
        
	def testTarifaNegativaFinSemana(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,9,8,0,0)
        finDeServicio = datetime.datetime(2017,4,9,10,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,9,8,0,0)
        finDeServicio = datetime.datetime(2017,4,9,10,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,4,9,8,0,0)
        finDeServicio = datetime.datetime(2015,4,9,10,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(6,-9)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), -1)
        
	def testTarifaCaracterEnSemana(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,28,8,0,0)
        finDeServicio = datetime.datetime(2017,4,28,10,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,28,8,0,0)
        finDeServicio = datetime.datetime(2017,4,28,10,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,4,28,8,0,0)
        finDeServicio = datetime.datetime(2015,4,28,10,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa("a",2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), -1)
        
	def testTarifaCaracterEnFinSemana(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,9,8,0,0)
        finDeServicio = datetime.datetime(2017,4,9,10,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,4,9,8,0,0)
        finDeServicio = datetime.datetime(2017,4,9,10,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,4,9,8,0,0)
        finDeServicio = datetime.datetime(2015,4,9,10,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(2,"a")
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), -1)
        
	def testInicioMayorQueFin(self):
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,7,8,0,0,0)
        finDeServicio = datetime.datetime(2017,7,7,0,0,0)
=======
<<<<<<< HEAD
		inicioDeServicio = datetime.datetime(2017,7,8,0,0,0)
        finDeServicio = datetime.datetime(2017,7,7,0,0,0)
=======
		inicioDeServicio = datetime.datetime(2015,7,8,0,0,0)
        finDeServicio = datetime.datetime(2015,7,7,0,0,0)
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master
        tiempoDeServicio = [inicioDeServicio, finDeServicio]
        tarifaActual = Tarifa(2,"a")
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeServicio), -1)

if __name__ == '__main__':
<<<<<<< HEAD
unittest.main()
=======
<<<<<<< HEAD
unittest.main()
=======
    unittest.main()
>>>>>>> origin/master
>>>>>>> refs/remotes/origin/master

