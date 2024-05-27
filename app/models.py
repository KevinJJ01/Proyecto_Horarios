from app import db, login 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

#Modulo 
class Administrador(db.Model, UserMixin):
    __tablename__="Administrador"
    id_administrador=db.Column(db.Integer, primary_key = True)
    Nombres_admin =db.Column(db.String(40))
    Apellidos_admin =db.Column(db.String(40))
    Tel_admin =db.Column(db.String(12))
    Tipo_admin =db.Column(db.String(15))
    username = db.Column(db.String(120), unique = True)
    password =db.Column(db.String(120))

    def get_id(self):
        return str(self.id_administrador)

##autentication for user  
@login.user_loader
def load_user(id):
    return Administrador.query.get(id)

#Modulo
class Regional(db.Model):
    __tablename__="Regional"
    id_Regional=db.Column(db.Integer, primary_key = True)
    Nombre=db.Column(db.String(40))
    Departamento=db.Column(db.String(40))

#Modulo
class Transversal(db.Model):
    __tablename__ ="Transversal"
    id_Transversal =db.Column(db.Integer, primary_key = True)
    Nombre_Tran =db.Column(db.String(40))
    Horas_Min_Sem =db.Column(db.Integer)
    Horas_Max_Sem =db.Column(db.Integer)
    Hora_Dia =db.Column(db.Integer)

#Modulo
class Centro(db.Model):
    __tablename__="Centro"
    id_Centro =db.Column(db.Integer, primary_key = True)
    Nombre =db.Column(db.String(40))
    Areas =db.Column(db.String(40))
    Descripcion =db.Column(db.String(40))
    Id_Regional= db.Column(db.Integer, db.ForeignKey('Regional.id_Regional'))
    Regional = relationship('Regional')
    

class Instructor(db.Model):
    __tablename__="Instructor"
    id_instructor=db.Column(db.Integer, primary_key = True)
    Nombre=db.Column(db.String(40))
    Apellido=db.Column(db.String(40))
    Num_identificacion =db.Column(db.String(12))
    Tipo_Contrato =db.Column(db.String(20))
    Horas_Semanales =db.Column(db.Integer)
    Horas_Diarias =db.Column(db.Integer)
    Id_Centro= db.Column(db.Integer, db.ForeignKey('Centro.id_Centro'))
    Centro = relationship('Centro')

class Ambiente(db.Model):
    __tablename__="Ambiente"
    id_Ambiente =db.Column(db.Integer, primary_key = True)
    Nombre =db.Column(db.String(40))
    Disponibilidad =db.Column(db.String(40))
    tipo =db.Column(db.String(40))
    Horas_Disp =db.Column(db.Integer)
    Horas_Ocup =db.Column(db.Integer)
    Id_Centro= db.Column(db.Integer, db.ForeignKey('id_Centro'))
    
#Modulo
class Coordinacion(db.Model):
    __tablename__="Coordinacion"
    id_Coordinacion =db.Column(db.Integer, primary_key = True)
    Nombre_coordinacion =db.Column(db.String(40))
    descripcion_coordinacion =db.Column(db.String(40))
    Id_Centro= db.Column(db.Integer, db.ForeignKey('Centro.id_Centro'))
    Centro = relationship('Centro')
    
class Programa (db.Model):
    __tablename__="Programa"
    id_Programa =db.Column(db.Integer, primary_key = True)
    Nombre_progr =db.Column(db.String(40))
    Id_Coordinacion= db.Column(db.Integer, db.ForeignKey('Coordinacion.id_Coordinacion'))
    Coordinacion = relationship('Coordinacion')
    
class Ficha(db.Model):
    __tablename__="Ficha"
    id_Ficha =db.Column(db.Integer, primary_key = True)
    Id_Programa= db.Column(db.Integer, db.ForeignKey('id_Programa'))
    
class Tematica (db.Model):
    __tablename__="Tematica"
    id_Tematica =db.Column(db.Integer, primary_key = True)
    Nombre =db.Column(db.String(40))
    Duracion_Semana =db.Column(db.Integer)
    Duracion_Trimestre =db.Column(db.Integer)
    Desripcion =db.Column(db.String(40)) 
    Id_Programa= db.Column(db.Integer, db.ForeignKey('id_Programa'))
    
class Resultado_de_aprendizaje(db.Model):
    __tablename__="Resultado_de_aprendizaje"
    id_Resul_apr =db.Column(db.Integer, primary_key = True)
    Nombre =db.Column(db.String(40))
    Estado =db.Column(db.String(20))
    Id_Tematica= db.Column(db.Integer, db.ForeignKey('id_Tematica'))


class Horario(db.Model):
    __tablename__ ="Horario"
    id_Horario =db.Column(db.Integer, primary_key= True)
    Nombre_iden =db.Column(db.String(30))
    NumeroDias =db.Column(db.Integer)
    NumeroBloquesxDia =db.Column(db.Integer)
    Id_Programa= db.Column(db.Integer, db.ForeignKey('id_programa'))
    

class Bloque(db.Model):
    __tablename__="Bloque"
    id_Bloque =db.Column(db.Integer, primary_key = True)
    Dia =db.Column(db.String(40))
    Id_Horario= db.Column(db.Integer, db.ForeignKey('id_Horario'))
    Id_Tematica= db.Column(db.Integer, db.ForeignKey('id_Tematica'))
    Id_Ficha= db.Column(db.Integer, db.ForeignKey('id_Ficha'))
    Id_Tranversal= db.Column(db.Integer, db.ForeignKey('id_Transversal'))
    Id_Ambiente= db.Column(db.Integer, db.ForeignKey('id_Ambiente'))
    Id_Instructor= db.Column(db.Integer,db.ForeignKey('id_Instructor'))
    
