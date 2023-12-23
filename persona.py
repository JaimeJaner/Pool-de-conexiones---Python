from logger_base import log
class Persona: 
    
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None) -> None:
        
        self._id_persona=id_persona
        self._nombre= nombre
        self._apellido= apellido
        self._email=email
        
    def __str__(self) -> str:
        
        return f"""
            Id Persona: {self._id_persona}, Nombre: {self._nombre},
            Apellido: {self._apellido}, Email: {self._email}    
    """
    
    #Métodos get y set para cada una de las propiedades del objeto.
    @property
    def id_persona(self):
        return self._id_persona
    @id_persona.setter
    def id_persona(self, id_persona):
        id_persona=id_persona   
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre       
    @property
    def apellido(self):
        return self._apellido   
    @apellido.setter
    def apellido(self, apellido):
        self._apellido=apellido       
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email):
        self._email= email
        
if __name__ == "__main__":
    
    persona1 = Persona(1,"Jaime","Janer","J.janer292")
    log.debug(persona1)
    
    #Simular un insert.
    persona1 = Persona(nombre="Juan", apellido="Perez", email="jperez")
    log.debug(persona1)