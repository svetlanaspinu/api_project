# tot codul acesta este din fastapi-sqlalchemy. mai intii am instalat sqlalchemy in python(pip install sqlalchemy), supa am creat file database.py pentru a importa 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# database adapter for python - first insatllation in terminal: pip intall psycopg - all information in caiet, in documentation-basic module usage- gasesc toate codurile cu explicatii
import psycopg2
#pentru a chema column name si values din pgAdmin database care am facut-o trebuie sa importez de mai jos si sa o chem la cursor_factory la try
from psycopg2.extras import RealDictCursor 
import time # legat de while True de la Database, dupa break sa fie o pauza de citeva secunde
#omport for settings SQLALCHEMY_DATABASE_URL
from .config import settings

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# all this commans are in sqlalchemy fastapi documentation
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base = declarative_base()

#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password456@localhost/fastapi' #postgresql://<username>:<password>@<ip-address/hostname(localhost)>/<database_name>' # the format of connection string that we have to pass in sql alchemy to connect with our db
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# create an engine that is responsible to sqlalchemy connect with postman
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# to make a connection with DB we make a session
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)



# this function is create a session towards our database, for every request to that specific API endpoint, and then its going to close it out once is done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#                   Codul acesta se pote si de sters pentru ca este doar un test de conectare cu database folosind postgres driver/ folosim sqalchemy to connect cu database
   # Demostration how to connect vs code with PgAdmin database
#de aici pina la time.sleep este doar o demonstartie sa vedem cum merge conectarea database cu codul din VS in mod normal nu se face asa pentru ca se vede informatia ca - numele localhosyului, passwordul, - informatii ce sunt secrete
#while True:
# am installat psycopg si am importat, 
# connection to database can fail, because the DB is unreacheable or down so firts we use try to check the connection;
    #try:
    # connect function passing the host-ip address(localhost-our ip address), database-we want to connect to(fastapi-database din pgAdmin), user name we want to connect to, and password
        #conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='password456', cursor_factory=RealDictCursor, port=5432)
        #cursor = conn.cursor() #calling the cursor method and savin in variable cursor, we eill use cursor to execute SQL statemets
        #print("Database connection was succesfull!")
        #break
#if unablle to connect
   # except Exception as error:  # storing the error in variable error
        #print("Connection to database failed!")
        #print("Error: ", error)
    # dupa ce am importat time-ul sus il setez la 2 sec
       # time.sleep(2)