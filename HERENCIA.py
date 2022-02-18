class Persona(object):
    def __init__(self,vdni,vapellidos,vnombres,vedad,vsexo):
        self.dni=vdni
        self.apellidos=vapellidos
        self.nombres=vnombres
        self.edad=vedad
        self.sexo=vsexo
    
    def __str__(self):
        return "%s, %s, %s, %s, %s"% (str(self.dni),self.apellidos,self.nombres,str(self.edad),self.obtebersexo(self.sexo))
    
    def obtebersexo(self,sexo):
        genero=('MASCULLINO','FEMENINO')
        if sexo=='M':
            return genero[0]
        elif sexo=='F':
            return genero[1]
        else:
            return 'DESCONOCIDO'

class Supervisor(Persona):
    def __init__(self, vdni, vapellidos, vnombres, vedad, vsexo,vturno):
        super().__init__(vdni, vapellidos, vnombres, vedad, vsexo)
        self.turno=vturno
        self.tareas=['Supervisor obras','Visto Bueno','Objetivos en las Obras']
    
    def __str__(self):
        return "DNI: %s, APELLIDOS Y NOMBRES: %s %s, ES SUPERVISOR DE OBRAS Y SUS TAREAS SON: %s, SU EDAD ES: %s, SEXO %s,TURNO: %s"%(
            str(self.dni),self.apellidos,self.nombres,self.mostrartareas(),str(self.edad),self.sexo,self.turno)

    def mostrartareas(self):
        return ', '.join(self.tareas)

class 

Supervisor1=Supervisor(45090133, "MASCCO LUQUE ", "MICHAEL RONALD", 33, "M", "MAÑANA")
print(Supervisor1)