from logger_base import log
import psycopg2 as bd
import sys

class Conexion: 
    
    _DATABASE= "test_db"
    _USERNAME= "postgres"
    _PASSWORD= "123456"
    _DB_PORT= "5432"
    _HOST = "127.0.0.1"
    
    @classmethod
    def obtenerConexion(cls):
       pass
        
    
    
if __name__=="__main__":
    pass