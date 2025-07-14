class Hospital:
    def __init__(self, n:str, calle:str, altura:int, cpa:str, lat:float, long:float):
        ''' requiere:Nada
            Inicializa un Hospital con nombre n, nombre de calle calle, altura de 
            calle altura, código postal argentino cpa, latitud lat y longitud long '''
        self.nombre:str = n 
        self.calle_nombre:str = calle
        self.calle_altura:int = altura
        self.cpa:str = cpa
        self.longitud:float = long
        self.latitud:float = lat 
        self.direccion:str = (calle + ' ' + str(altura) + ' ' + '(' + cpa + ')')

    def __repr__(self) -> str:
        '''Requiere:nada
           Devuelve: una representación str de Hospital'''
        return(self.nombre + '--' + self.direccion)