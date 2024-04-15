class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/horario'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SECRET_KEY = 'HORARIOSSENA'