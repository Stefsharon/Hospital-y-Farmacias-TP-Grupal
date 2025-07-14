import unittest
from dataset import DataSetSanitario
from hospital import Hospital
from farmacia import Farmacia
from typing import List, Dict, Tuple



class TestDataSetSanitario(unittest.TestCase):
    
    def setUp(self):
       self.dataset:DataSetSanitario= DataSetSanitario('prueba_farmacia.csv','prueba_establecimentos_gastronomicos.csv') 
       self.dataset2:DataSetSanitario= DataSetSanitario('prueba_farmacias2.csv','prueba_hospitales2.csv')
       self.dataset3:DataSetSanitario= DataSetSanitario('vacio_farmacias.csv','vacio_hospitales.csv')
   
    def test_nombres_de_hospitales(self):
        res:List[str] = self.dataset.nombres_de_hospitales()
        res_esperada:List[str] = ['HOSP. DE ELIZALDE', 'HOSP. GUTIERREZ', 'HOSP. MOYANO', 'HOSP. ODONTOLOGICO CARRILLO']
        self.assertAlmostEqual(res, res_esperada)
        
    def test_hospital_por_nombre(self):
        nombre:str = 'HOSP. DE ELIZALDE'
        res:Hospital = self.dataset.hospital_por_nombre(nombre)
        res_esperada:Hospital= Hospital('HOSP. DE ELIZALDE','MANUEL A. MONTES DE OCA', 40, 'C1270AAN', -34.6288473603881, -58.3775508488443)
        self.assertAlmostEqual(res.nombre, res_esperada.nombre)
        
    def test_farmacia_por_hospital(self):
        res:Dict[Hospital,Tuple[Farmacia, float]] = self.dataset2.farmacia_por_hospital()
        res_esperada:Dict[Hospital,Tuple[Farmacia, float]] = {}
        h1:Hospital = Hospital('HOSP. DE ELIZALDE', 'MANUEL A. MONTES DE OCA', 40, 'C1270AAN',-34.6288473603881, -58.3775508488443)
        f1:Farmacia = Farmacia(-34.6286014228037, -58.3775895022765, 'AV CASEROS', 1000, 'C1152AAS')
        res_esperada[h1] = (f1,f1.distancia(h1.latitud, h1.longitud))
        h2:Hospital = Hospital('HOSP. PIROVANO','MONROE',3555,'C1430BKC',-34.565051956568, -58.4710781593251)
        f2:Farmacia = Farmacia(-34.565476750226,-58.4710442601769,'AV MONROE',3592,'C1430BKP') 
        res_esperada[h2] = (f2,f2.distancia(h2.latitud, h2.longitud))
        h3:Hospital = Hospital('HOSP. T. DE ALVEAR', 'WARNES',2630,'C1427DPS',-34.5972098729151,-58.4752588459761) #
        f3:Farmacia = Farmacia(-34.5965977331471,-58.4744470215369, 'AV WARNES',2707, 'C1427DPG')
        res_esperada[h3] = (f3,f3.distancia(h3.latitud, h3.longitud))
        h4:Hospital = Hospital('HOSP. ARGERICH', 'CORBETA PI Y MARGAL', 750,'C1155AHD',-34.6283448581677,-58.365985088719)
        f4:Farmacia = Farmacia(-34.6278286788458,-58.3663683680033,'PI Y MARGALL',781,'C1155AHC')
        res_esperada[h4] = (f4,f4.distancia(h4.latitud, h4.longitud))
        self.assertEqual(len(res), len(res_esperada)) 
        hospital1:Hospital = self.dataset2.hospital_por_nombre('HOSP. DE ELIZALDE')
        self.assertEqual(str(res[hospital1][0]), 'FARMACIA:AV CASEROS 1000 (C1152AAS)') 
        
    def test_farmacia_por_hospital2(self): 
        res:Dict[Hospital,Tuple[Farmacia, float]] = self.dataset3.farmacia_por_hospital()
        res_esperada:Dict[Hospital,Tuple[Farmacia, float]] = {}
        self.assertEqual(res, res_esperada)
        
        
    def test_farmacia_mas_cercana(self): 
        h:Hospital = Hospital('HOSP. PIROVANO','MONROE',3555,'C1430BKC',-34.565051956568, -58.4710781593251)
        res:Farmacia = self.dataset2.farmacia_mas_cercana(h)
        res_esperada:Farmacia = Farmacia(-34.565476750226,-58.4710442601769,'AV MONROE',3592,'C1430BKP') 
        self.assertEqual(res.direccion, res_esperada.direccion)
        
    


unittest.main()
