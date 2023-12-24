from conexion import Conexion
from persona import Persona
from logger_base import log 

class PersonaDAO:
    '''
    DAO (DATA ACCESS OBJECT)
    CRUD (CREATE, READ, UPDATE, DELETE)
    '''
    
    _SELECCIONAR= "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona (nombre, apellido, email) VALUES (%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre = %s, Apellido = %s, email= %s WHERE id_persona =%s"
    _ELIMINAR= "DELETE FROM persona WHERE id_persona=%s"
    
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)     
                    
                return personas 
        
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:     
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR,valores)
                log.debug(f"Persona insertada: {persona}")
                return cursor.rowcount
            

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug(f"Valores actualizzados para la persona: {persona}")
                return cursor.rowcount
            
    @classmethod
    def eliminar (cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores= (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f"Objeto eliminado: {persona}")
                return cursor.rowcount
             
    
if __name__== "__main__":
    #Insertar un registro.
    
    #persona1=Persona(nombre="JAJAJAJAJA1567",apellido="jajajajajajaj",email="jajajaj.jajaja@jaja.com")
    #personas_insertadas = PersonaDAO.insertar(persona1)
    #log.debug(f"Personas insertadas: {personas_insertadas}")
    
    #Actualizar un registro.
    
    persona2 = Persona(3, "Juan Carlos", "Perez", "jasjasjasjas@jajasj")
    personas_actualizadas = PersonaDAO.actualizar(persona2)
    log.debug(f"Personas actualizadas: {personas_actualizadas}")
    
    
    persona3 = Persona(id_persona=33)
    persona_eliminada= PersonaDAO.eliminar(persona3)
    log.debug(f"Personas eliminadas: {persona_eliminada}")
    
    #seleccionar objeto.
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)  