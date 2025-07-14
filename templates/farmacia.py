from typing import Tuple
from haversine import haversine, Unit
class Farmacia:
    def __init__(self, lat:float, lng:float, calle_n:str, calle_a:int, cpa:str):
        ''' requiere: nada
        Inicializa una Farmacia con latitud lat, longitud lng, nombre de calle calle_n, 
        altura de calle calle_a, y código postal argentino cpa'''
        self.latitud:float=lat
        self.longitud:float=lng
        self.calle_nombre:str = calle_n
        self.calle_altura:str = calle_a
        self.cpa:str = cpa 
        self.direccion:str= (calle_n + ' ' + str(calle_a)+ ' ' + '(' + cpa + ')')
    
    def distancia(self, lat:float, long:float) -> float:
        ''' requiere: nada
            devuelve: la distancia que separa la farmacia del punto determinado por 
            la latitud y la longitud ingresadas por el usuario'''
        punto1:Tuple[float, float] = (self.latitud, self.longitud)
        punto2:Tuple[float, float] = (lat, long)
        res:float = haversine(punto1, punto2, unit=Unit.METERS)
        return res

    def __repr__(self)->str:
        '''Requiere:nada
        Devuelve una representación string de Farmacia'''
        return ( 'FARMACIA:' + self. direccion)



