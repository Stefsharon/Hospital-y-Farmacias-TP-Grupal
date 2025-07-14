import unittest

# Importamos el codigo a testear.
from hospital import Hospital

####################################################################

class TestHospital(unittest.TestCase):
    def test_repr(self):
        h1:Hospital = Hospital('HOSP. GUTIERREZ', 'GALLO', 1330,'C1425EFD', 1234.0, 1234.0)
        res:str = str(h1)
        res_esperada:str = 'HOSP. GUTIERREZ--GALLO 1330 (C1425EFD)'
        self.assertAlmostEqual(res, res_esperada)      
        
    def test_longitud(self):
        h1:Hospital=Hospital('HOSP. DE ELIZALDE','MANUEL A. MONTES DE OCA',40,'C1270AAN', -34.6288473603881,-58.3775508488443)
        res:float=h1.longitud
        res_esperada:float=-58.3775508488443
        self.assertEqual(res, res_esperada)
        
    def test_nombre(self):
        h1:Hospital=Hospital('HOSP. DE ELIZALDE','MANUEL A. MONTES DE OCA',40,'C1270AAN',-34.6288473603881,-58.3775508488443)
        res:str=h1.nombre
        res_esperada:str='HOSP. DE ELIZALDE'
        self.assertEqual(res, res_esperada)
        
    def test_latitud(self):
        h1:Hospital=Hospital('HOSP. DE ELIZALDE','MANUEL A. MONTES DE OCA',40,'C1270AAN', -34.6288473603881,-58.3775508488443)
        res:float=h1.latitud
        res_esperada:float=-34.6288473603881
        self.assertEqual(res, res_esperada)
        
    
    def test_cpa(self):
         h1:Hospital=Hospital('HOSP. DE ELIZALDE','MANUEL A. MONTES DE OCA',40,'C1270AAN', -34.6288473603881,-58.3775508488443)
         res:str=h1.cpa
         res_esperada:str='C1270AAN'
         self.assertEqual(res, res_esperada)
        
        
    def test_direccion(self):
        h1:Hospital = Hospital('HOSP. GUTIERREZ', 'GALLO', 1330,'C1425EFD', 1234.0, 1234.0)
        h2:Hospital = Hospital('HOSP. DE ELIZALDE','MANUEL A. MONTES DE OCA',40, 'C1270AAN' ,-34.6288473603881, -58.3775508488443)
        res_1:str = h1.direccion
        res_2:str = h2.direccion
        res_esperada_1:str = 'GALLO 1330 (C1425EFD)'
        res_esperada_2:str = 'MANUEL A. MONTES DE OCA 40 (C1270AAN)'
        self.assertEqual(res_1, res_esperada_1)
        self.assertEqual(res_2, res_esperada_2)
        
        			
        

unittest.main()
