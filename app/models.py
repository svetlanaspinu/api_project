# this file contains the tables. we do not create the tabels in pgAdmin but in python using  model, every model represent a table in database.
from .database import Base
# to create the colums/ intenger we have to specialize what type of data is the id, here intenger/ 
# aici am inserat tot ce am inserat in class post/ ex intenger, timestamp, boolea,..etc
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from pydantic_settings import BaseSettings


class Post(Base):
    # name of the table
    __tablename__ = "posts"
    # define the columns
    id = Column(Integer, primary_key=True, nullable=False) # primarykey si nullable am scris dupa ce am verificat cum sunt in pgAdmin/
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False) #nullable faulse - not allow for the column to be empty
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))  #server_def=text(now)-exact cum scrim in posgres sa aratte data si ora, text-lam importat sus

# creating a foreign_key through code using sqlalchemy/ create a specific class within the 'post' table, / foreignkey e imortat din sqlalchemy
# in foreign key we have to insert the exact table and column that we want to refference/ the ondelete is the policy for when we delete the foreignkey or the parent table
# with the CASCADE if the parent is deleted then the child is deleted as well/ nullable=False - nu poate ramine empty - must be fiiled in
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE", nullable=False))

# this tells sqalchemy to automatic fetch some piece of information based up the relationship - am importat relationship sus
# ce este in paranteza it will gonna to return the class of another model(in this case User - ce este mentionat mai jos)/ this create another propertie -owner- for our post
# so when we retrieve a post it's gonna to retrieve a owner propertie and its gonna to figure out the relationship to User/ its gonna to fetch the user based on the owner id
# and return that for us/ dupa asta update schemas.py in class Post
    owner = relationship("User")


                # Creating User functionality - having users being able to create an account within the app, login, creating posts associates with their acoount
# creating a table that it will hold user information
class User(Base): # Base - ectend that is required for sqlalchemy model
    __tablename__ = "users" # asa va aparea in Postgress
# creating the columns:
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True) # unique - sa nu fie 2 emailuri pt acelasi acount
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) 
     #server_def=text(now)-exact cum scrim in posgres sa aratte data si ora, text-lam importat sus
# Alembic - database migration tool/ it allow to automatic update the columns based on the model that we defined here, when we add a new colum here it's going to update the Postgres database
# ALEMBIC - it allow us to create incremented changes to database and truck it

# creating the tables for the votes tables/ nu mi-a aparut in postman min 09:32
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = ColumnColumn(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)




    