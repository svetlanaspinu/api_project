from fastapi import FastAPI #Response, status, HTTPException, Depends# import the response ca sa ascunda raspinsuri gen 404 la paginile web./ status la linia 80 pt a vedea fiecare http satus codes.
#from typing import Optional, Union, List #  a variable or parameter could be multiple different types
#from fastapi.params import Body
# the pydantic module is in Lib folder, that means that is already installed in the python library, Pydantic is used for data validation in python
# to validate the schema of a information
#from pydantic import BaseModel
#from random import randrange # is used to create a random number or a random intenger
#from sqlalchemy.orm import Session
# import the models, base for the below command - model.Base.metadaa.../ # models - import the class Post(Base)- unde se afla tabelul din fileul models
from . import models    # schemas, utils
from .database import engine #get_db
# connectez folderul routers cu fileul main
from .routers import post, user, auth, vote
from .config import settings
# de pe fastapi.tiangolo -- CORS
from fastapi.middleware.cors import CORSMiddleware



# accessing the database
print(settings.database_username)

# from fastapi sqlalchemy import to create all the tables/ we dond needed after installing the alembic
#models.Base.metadata.create_all(bind=engine)


#continuarea la notitiile din caiet
app =FastAPI() # creating an instance of fastapi, this code is from api.com website
#all the domains that can talk to api, stored in list, in this case google/ we just have to provide all the website that can access our api
# if is public/ for everyone using a wildcard ["*"]
origins = ["https://www.google.com"]
# de pe fastapi - CORS
app.add_middleware(
    CORSMiddleware,     # if someone send a request to our app, before to go to the routers below, it goes to CORSMiddleware and perform some sorts of operations
    allow_origins=origins,  #what domains should our api talk to
    allow_credentials=True, #
    allow_methods=["*"],    # allwos all http methods and headers to 
    allow_headers=["*"],
)




# save the post in memory by creating a variable that's going to store all the Posts, it's an array[] that content all the posts subjects.
# each post will be a dictionary{} that will have a couple propierties like title, ...
#my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "i like pizza", "id": 2}]  # everytime we save a piece of information with databases, teh databases will create a unique identifier(id)

# create the function to find the post by an id
#def find_post(id):
# iterate over my_posts, p is the post that we are iterate over
    #for p in my_posts:
        #if p["id"] == id: # the post has an id wich equals the ID that was passed into the function
            #return p # return that specific posts

                        # --- continuarea la Delete a Post...
# defind a function to delete a post. Urmatoarea dupa ce am creat functia la Delete a Post section
 # 1. find the index in the array that has required ID
#def find_index_post(id): # (id) - passing the id we are interesting in 
# iterate over the array "i(index), p(post)" and grabbing the specifinc index that we are iterate over - using enumerate(my_posts), using my_post - to get the acces to the post(p) that we are iterating over and index(i)
    #for i, p in enumerate(my_posts):
# it will give us the index of the dictionary with the specific id / ... dupa aceasta ma duc inapoi jos la Delete a Post section
        #if p['id'] == id:
           # return i
                        # --- aici se termina functia pt Delete Post



# the @ is a decorator that make a function to act as an API/ the @- decorator; app- reference the fastAPI instance; get-the HTTP method the user should use
# ("/") - is the route path; the path after the specific name of the API; the url of the website is this slash /
@app.get("/")    #this code is from fastapi.com
def read_root(): # a plain function that holds the data that its going to be sent back to the user
    return {"message": "Hello World, new worlld"} # this is a python dictionary and fastAPI will convert this to JSON wich is the main language of API.
# the JSONs is used to send data back and forth between APIs/  it convert the message to JSON and it sends it back to the user/ that's why we see on the web browser
 

 # codul de mai jos: face trimitere mai intii sa verifice filele post si user iar dupa sa aplice comnzile din de la decorator @router.get, prin -app.include_router
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
                                    #TEST CODE
 # cod test sa sa vad daca merge:
#@app.get("/sqlalchemy")
# test_post is our path operation function and we pas the db as a parameter. the db is the get_db function from database file, saved as db here, after importing the Session object and Dependenccy
# we are calling the get_db with Dependence so it makes it a dependency/ 
#def test_posts(db: Session = Depends(get_db)):
# to make a query which is getting passed into our function-db, and we tap it into the query method-.query, then we have to pass in the specific model for the
#tabel we want to query/ (models.-cheama tabelul din fileul models .Posts-the information from post class)/ .all()- methods to query the entry -here all
    #posts = db.query(models.Post).all()
    #return {"data": "succefully"}
# testatrea de mai sus, dupa ce scriu codul-verific in postman - creez un nou request cu acelasi url si dupa / scriu /sqalchemy cum e scriss in paranteza
# si dupa in postgres clic stinga pe query tool + in tabelul cela scriu SELECT * FROM posts si ar treebui sa arate daca avem vreun post
                                #TEST CODE FINISH


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
    #return {"item_id": item_id, "q": q}



                                       

#                                      

