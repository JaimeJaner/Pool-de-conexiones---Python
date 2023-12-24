from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None
        log.debug("Se crea el objeto conexión")
        
    #Cuando se utiliza With, se llama directamente el método enter.
    #Aquí lo estamos sobrecargando para generar funciones adicionales.
    #Una gestión de los recursos diferente.
    
    
    #Iniciamos la conexión y creamos un cursor para ella y retornamos el cursor.
    #Todo dentro del contexto "with"
    
    def __enter__ (self):
        log.debug("Inicio del método with __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        log.debug("Cursor del objeto creado.")
        
        return self._cursor
        
    #Al finalizar el contexto, simplemente verificamos si existió algun error
    #De ser así, eliminamos los cambios realizados. 
    #Si no, efectuamos el commit y liberamos el objeto del pool de conexión,
    #Y cerramos además el cursor asociado al objeto.
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traceback_excepcion):
        log.debug(f"Se ejecuta método __exit__")
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f"Ocurrió una excepción: {valor_excepcion} {tipo_excepcion} {traceback_excepcion}")
        
        else:
            self._conexion.commit()
            log.debug("Commit de la transacción con éxito.")
            
        self._cursor.close()
        log.debug("Cerramos el cursor del objeto.")
        Conexion.liberarConexion(self._conexion)
        

if __name__ == "__main__":
    #con with, se ejecuta el __init__ y luego el __enter__
    with CursorDelPool() as cursor:
        log.debug("Dentro del bloque 'with.'")
        cursor.execute("Select * from Persona")
        log.debug(cursor.fetchall())
        
        