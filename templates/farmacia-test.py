import unittest
from haversine import haversine, Unit
from typing import Tuple 
from farmacia import Farmacia



class TestFarmacia(unittest.TestCase):

   
    def test_repr(self):
        f:Farmacia=Farmacia(1234.0,-1234.0,'Monroe',1234,'C1111XYZ')
        res_esperada:str='FARMACIA:Monroe 1234 (C1111XYZ)'
        self.assertAlmostEqual(str(f), res_esperada)
    
    def test_distancia(self):
        f1:Farmacia=Farmacia(-34.6268150764954,-58.5080720511654,	'AV LOPE DE VEGA',1397,'C1407BNM')
        latitud_prueba:float=-34.6268150764954
        longitud_prueba:float=-58.5080720511654      
        res:float=f1.distancia(latitud_prueba,longitud_prueba)
        Tupla1:Tuple[float,float] = (f1.latitud, f1.longitud)
        Tupla2:Tuple[float,float] = (latitud_prueba,longitud_prueba)
        res_esperada:float = haversine(Tupla1, Tupla2, unit=Unit.METERS)
        self.assertAlmostEqual(res, res_esperada,places=6)
        
    def test_distancia2(self):
        f1:Farmacia=Farmacia(-34.626,-58.508,'AV LOPE DE VEGA',1397,'C1407BNM')
        latitud_prueba:float=(-34.631)
        longitud_prueba:float=(-58.511)
        res:float=f1.distancia(latitud_prueba,longitud_prueba)
        Tupla1:Tuple[float,float] = (f1.latitud, f1.longitud)
        Tupla2:Tuple[float,float] = (latitud_prueba,longitud_prueba)
        res_esperada:float = haversine(Tupla1, Tupla2, unit=Unit.METERS)
        self.assertAlmostEqual(res, res_esperada, places=6)
 
  
    def test_longitud(self):
        f1:Farmacia=Farmacia(-34.6268150764954,-58.5080720511654,'AV LOPE DE VEGA',1397,'C1407BNM')
        res:float=f1.longitud
        res_esperada:float=-58.5080720511654
        self.assertEqual(res, res_esperada)
   
        
        
    def test_latitud(self):
        f1:Farmacia=Farmacia(-34.6268150764954,-58.5080720511654,'AV LOPE DE VEGA',1397,'C1407BNM')
        res:float=f1.latitud
        res_esperada:float=-34.6268150764954
        self.assertEqual(res, res_esperada)
        
         
    def test_cpa(self):
         f1:Farmacia=Farmacia(-34.6268150764954,-58.5080720511654,'AV LOPE DE VEGA',1397,'C1407BNM')
         res:str=f1.cpa
         res_esperada:str='C1407BNM'
         self.assertEqual(res, res_esperada)
         
    def test_direccion(self):
        f1:Farmacia=Farmacia(-34.6268150764954,-58.5080720511654,'AV LOPE DE VEGA',1397,'C1407BNM')
        f2:Farmacia = Farmacia(-34.6117065912837,-58.4689759825657, 'AV JUAN B.JUSTO',4995,'C1416DKD')
        res_1:str = f1.direccion
        res_2:str = f2.direccion
        res_esperada_1:str = 'AV LOPE DE VEGA 1397 (C1407BNM)'
        res_esperada_2:str = 'AV JUAN B.JUSTO 4995 (C1416DKD)'
        self.assertEqual(res_1, res_esperada_1)
        self.assertEqual(res_2, res_esperada_2)
        
	



unittest.main()
