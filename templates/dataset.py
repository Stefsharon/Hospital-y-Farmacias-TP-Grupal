from typing import List, Dict, TextIO, Tuple
from farmacia import Farmacia
from hospital import Hospital
import csv
class DataSetSanitario:
    def __init__(self, 
                 filename_farmacias:str, 
                 filename_hospitales:str):
        '''       
        Requiere: filename_farmacias y filename_hospitales son nombres de dos archivos de tipo csv 
        Devuelve: Inicializa un DataSetSanitario, cargando las farmacias y hospitales contenidas en filename_farmacias y filename_hospitales en los atributos lista_f
        (una lista de Farmacias) y lista_h(lista de Hospitales)'''
        self.lista_f:List[Farmacia]=[]
        self.lista_h:List[Hospital] = []
        
        file_farmacias: TextIO = open(filename_farmacias, 'r', encoding='utf-8')
        linea: Dict[str, str]
        for linea in csv.DictReader(file_farmacias):
            lng:float=float(linea['long']) 
            lat:float=float(linea['lat'])
            calle_n:str=linea['calle_nombre']
            calle_a:str=linea['calle_altura']
            cpa:str=linea['codigo_postal_argentino']
            
            f1:Farmacia=Farmacia(lat,lng,calle_n,calle_a,cpa)
            self.lista_f.append(f1)

        file_hospitales: TextIO = open(filename_hospitales, 'r', encoding='utf-8')
        linea: Dict[str, str]
        for linea in csv.DictReader(file_hospitales):
            coordenadas:List[str] = linea['WKT'].split(' ')
            long:float=float(coordenadas[1][1:])
            lat:float=float(coordenadas[2][:-1])
            nombre:str = linea['NOM_MAP']
            calle:str=linea['CALLE']
            altura:str=linea['ALTURA']
            cpa:str=linea['COD_POSTAL']
            h:Hospital=Hospital(nombre, calle, altura, cpa, lat, long)
            self.lista_h.append(h)
        
        file_farmacias.close()
        file_hospitales.close()

    def nombres_de_hospitales(self) -> List[str]:
        '''Requiere:nada
            Devuelve: una lista con los nombres de todos los hospitales en el DataSetSanitario, en orden alfabético '''
        nombres_hospitales:List[str] = []
        for hospital in self.lista_h: 
            nombres_hospitales.append(hospital.nombre)
        return sorted(nombres_hospitales)
        
    def hospital_por_nombre(self, nombre:str) -> Hospital:
        ''' Requiere: que el nombre ingresado sea el nombre de un Hospital existente en el DataSetSanitario 
            Devuelve: el objeto Hospital correspondiente al nombre ingresado por el usuario '''
        for hospital in self.lista_h: 
            if hospital.nombre == nombre: 
                return hospital


    def farmacia_por_hospital(self) -> Dict[Hospital, Tuple[Farmacia, float]]:
        '''Requiere:Nada
           Devuelve: un diccionario que asocia a cada Hospital del dataset 
           un par (o sea, una tupla) con la Farmacia más cercana y la 
           distancia misma (en metros) '''
        farmacia:Farmacia = ()
        farmacia_distancia:Tuple[Farmacia,float]
        farmacia_hospital:Dict[Hospital, Tuple[Farmacia,float]] = dict()
        for hospital in self.lista_h:
            farmacia = self.farmacia_mas_cercana(hospital)
            farmacia_distancia = (farmacia, farmacia.distancia(hospital.latitud, hospital.longitud))
            farmacia_hospital[hospital] = farmacia_distancia
        return farmacia_hospital

    def farmacia_mas_cercana(self, hosp:Hospital)  -> Farmacia:
        ''' Requiere: que hosp sea un Hospital existente en el DataSetSanitario.
           Devuelve: La Farmacia del DatasetSanitario que está más cercana
           al Hospital hosp.'''
        distancia_res:float = 0.0
        distancia:float = 0.0
        res:Farmacia 
        for farmacia in self.lista_f: 
            distancia = farmacia.distancia(hosp.latitud, hosp.longitud)
            if distancia_res == 0.0 or distancia_res > distancia: 
                distancia_res = distancia
                res = farmacia
        return res

