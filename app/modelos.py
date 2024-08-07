from abc import ABC, abstractmethod
import sqlite3

class Model(ABC):
    @classmethod
    @abstractmethod
    def create_from_dict(cls, diccionario):
        pass

class Product(Model):
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(int(diccionario["id"]), diccionario["nombre"], float(diccionario["precio_unitario"]) )

    def __init__(self, nombre: str, id: int = -1, precio_unitario: float = 0.0):
        self.nombre = nombre
        self.id = id
        self.precio_unitario = precio_unitario

    def __repr__(self) -> str:
        return f"Product({self.id}):{self.nombre}:{self.precio_unitario}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.id == other.id and self.nombre == other.nombre and self.precio_unitario == other.precio_unitario
        return False
        
    def __hash__(self) -> int:
        return hash((self.id, self.nombre, self.precio_unitario))
    
""" class Pelicula:
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(diccionario["titulo"], diccionario["sinopsis"], int(diccionario["director_id"]), int(diccionario["id"]))

    def __init__(self, titulo: str, sinopsis: str, director: object, id: int = -1):
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.id = id
        self.director = director
 
    @property
    def director(self):
        return self._director
    
    @director.setter
    def director(self, value):
        if isinstance(value, Director):
            self._director = value
            self._id_director = value.id
        elif isinstance(value, int):
            self._director = None
            self._id_director = value
        else:
            raise TypeError(f"{value} debe ser un entero o instancia de Director")

    def __repr__(self) -> str:
        return f"Pelicula({self.id}):{self.titulo}, {self.director}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.titulo == other.titulo and self.sinopsis == other.sinopsis and self.director == other.director and self.id == other.id    
        return False
        
    def __hash__(self) -> int:
        return hash((self.id, self.titulo, self.sinopsis, self.director))
    
class Genero(Model):
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(diccionario["genero"], int(diccionario["id"]))

    def __init__(self, genero: str, id: int = -1):
        self.genero = genero
        self.id = id

    def __repr__(self) -> str:
        return f"Genero({self.id}):{self.genero}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.id == other.id and self.genero == other.genero 
        return False
        
    def __hash__(self) -> int:
        return hash((self.id, self.genero)) """
    
class DAO(ABC):
    """ 
    @abstractmethod
    def guardar(self, instancia):
        pass
        # raise NotImplementedError("No se debe usar DAO, es una interfaz")
    
    @abstractmethod
    def actualizar(self, instancia):
        pass
        # raise NotImplementedError("No se debe usar DAO, es una interfaz")
    
    @abstractmethod
    def borrar(self, id: int):
        pass
        # raise NotImplementedError("No se debe usar DAO, es una interfaz")
    
    @abstractmethod
    def consultar(self, id: int):
        pass
        # raise NotImplementedError("No se debe usar DAO, es una interfaz")
    """

    @abstractmethod
    def todos(self):
        pass
        # raise NotImplementedError("No se debe usar DAO, es una interfaz")
    

class DAO_Sqlite(DAO):
    model = None
    tabla = None

    def __init__(self, path) -> None:
        self.path = path

    def todos(self):
        """
        acceder a sqlite y traer todos los registros de la tabla del modelo
        con la funccion rows_to_dictlist traerlos en forma diccionario
        devolverlos como instancias de Model
        """
        conexion = sqlite3.connect(self.path)
        cursor = conexion.cursor()

        
        cursor.execute(f"select * from {self.tabla}")

        nombres = list(map(lambda item: item[0], cursor.description))

        resultado = self.__rows_to_dictlist(cursor.fetchall(), nombres)
        
        conexion.close

        return resultado
    
    def __rows_to_dictlist(self,filas,nombres):
        registros = []
        for fila in filas:
            registro = {}
            for i, nombre in enumerate(nombres):
                registro[nombre] = fila[i]

            registros.append(self.model.create_from_dict(registro))
        return registros
    

class DAO_Sqlite_Product(DAO_Sqlite):
    model = Product
    tabla = "productos"

""" class DAO_Sqlite_Pelicula(DAO_Sqlite):
    model = Pelicula
    tabla = "peliculas" """
    
