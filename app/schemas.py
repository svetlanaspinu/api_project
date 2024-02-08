# the pydantic module is in Lib folder, that means that is already installed in the python library, Pydantic is used for data validation in python
# to validate the schema of a information
# email str-to be sure that this is a email validator, not just an usual string
from pydantic import BaseModel, EmailStr
from datetime import datetime # ca sa pot pune dta la created_at in class PostCreate
from typing import Optional # optional de la TokenData
from pydantic.types import conint # coint allows the negative numbers

            # THIS IS THE PYDANTINC MODEL HOW TO CREATE A POST INHERITING FROM POSTBASE THAT INHERIT FROM BASEMODEL
# creating a class that is going to extend the basemodel from pydantic library
class PostBase(BaseModel): # sa ma informez despre Schema Models din caiet
    #writing the contenet that we want for our posts and set up to be a string
    title: str
    content: str
    published: bool = True # =True default value un tabel
# ceea ce am scris in paranteze la class extinde informatia ce se afla la acea clasa chiar daca e in alta pagina, de ex: class PostCreate(PostBase)-extinde informatia de la PostBase
# iar PostBase rxtinde informatia de la BaseModel
class PostCreate(PostBase):
    pass # it will accept whatever the PostBase will be

# this will send the user inform to the client that required
class UserOut(BaseModel):
    id: int
    email: EmailStr 
    created_at: datetime 
# nu scriem passwordul aici, asa ca nu o sa apara in postman
    
# the output is an sqlalchemy model but we need an pydantic model so i am using the below Config to transform.
    class Config:
        from_attributes = True

    
                # THE PYDANTIC MODEL FOR THE RESPONSE /  is reponaive for sending the post out

class Post(PostBase):
# this are all the fileds that we want in the response
    id: int
    created_at: datetime
    owner_id: int 
# dupa ce am scris in models.py  owner = relationship("User")...scriu codul de mai hos pentru a avea output de la user
    owner: UserOut

# the output is an sqlalchemy model but we need an pydantic model so i am using the below Config to transform.
    class Config:
        from_attributes = True

# schemas ca sa trec de errorile pydantic.error_wrappers.ValidationError: 8 validation errors for Settings database_hostname field required din Terminal
class PostOut(BaseModel):
# toate filedurile de la class Post vor fi sub denumirea de Post
    Post: Post
    votes: int

    class Config:
        from_attributes = True

# dupa ce am creat Creating a path operation for a new user in main.py aici cream schema pt user/ to check pip freeze - daca email-validator e instalat pt validarea emailului
class UserCreate(BaseModel):
    email: EmailStr  #importat sus din pydantic
    password: str
  



# pentru @router.post('/login') din auth.py file
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# the schema for the token
class Token(BaseModel):
    access_token: str
    token_type: str

# the schema for the embedded the data for token, 
class TokenData(BaseModel):
    id: Optional[str] = None  # aici id este setat ca sa fie Optional, am importat si Optional din typing library - sus.

# schemas for voting
class Vote(BaseModel):
    post_id: int
#dir-direction/ coint e importat si sus pentru a permite raspuns mai putin de cifra 1, de ex. -1 numere negative/ (le=1)-anything less than 1 it will be allowed
    dir: conint(le=1)
