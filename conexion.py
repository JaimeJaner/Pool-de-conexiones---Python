#Un pool de conexiones, en el contexto de la programación y el manejo de bases de datos, es un conjunto gestionado de conexiones a una fuente de datos,
#como una base de datos. En lugar de abrir y cerrar conexiones individualmente cada 
#vez que se necesita interactuar con la base de datos, un pool de conexiones
#mantiene un grupo de conexiones preestablecido que pueden ser reutilizadas de manera eficiente.
#Esto ayuda a mejorar el rendimiento y la eficiencia al evitar
#el costo de abrir y cerrar conexiones constantemente, 
#especialmente en entornos donde se realizan muchas operaciones de base de datos.

from logger_base import log
from psycopg2 import pool
import sys

class Conexion: 
    
    _DATABASE= "test_db"
    _USERNAME= "postgres"
    _PASSWORD= "123456"
    _DB_PORT= "5432"
    _HOST = "127.0.0.1"
    #Numero mínimo y máximo de conexiones. Todas las basses de datos tienen
    #Un límite. Cuidado con la elección, puede resultar pesado. Todo depende
    #De las necesidades del proyecto.
    _MIN_CON = 1
    _MAX_CON = 5 
    _pool = None
    
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, 
                                                      cls._MAX_CON,
                                                      host = cls._HOST, 
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f"Creación del pool exitoso. {cls._pool}")
                
                return cls._pool
                
            except Exception as e:
                log.error(f"Ocurrió un error al tratar de obtener el pool. {e}")
                sys.exit()
        else:
            return cls._pool


    @classmethod
    def obtenerConexion(cls):
       conexion = cls.obtenerPool().getconn()
       log.debug(f"Conexion obtenida del pool: {conexion}")
       return conexion
        
    
if __name__=="__main__":
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
