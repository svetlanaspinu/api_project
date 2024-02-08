from .. import models, schemas, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Optional# import the response ca sa ascunda raspinsuri gen 404 la paginile web./ status la linia 80 pt a vedea fiecare http satus codes.
from sqlalchemy.orm import Session
from ..database import get_db       
from typing import List   
from sqlalchemy import func # give access to function count la join tabels on python               

router = APIRouter(
    prefix="/posts",
    tags='Posts'    
) # every single route in this file , always start with /posts. so we dint need to write it on every single function                                    
   #the tags will group the requets in categories, asta pot sa ved daca accese link din terminal + /docs         
   #                            
                                        # GETting all Posts 
# creating a new path operations
# get is the HTTP method, am importat List sus din typing pt ca ne dadea eroare in Postman, pt ca datele care le da la output sunt in forma de List
#@router.get("/", response_model=List[schemas.Post]) 
@router.get("/", response_model=List[schemas.PostOut])    
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # ....Continuarea dupa while True ....try;   Trebuie sa fac Send in Postman - Get Posts ca sa apara informatia din PgAdmin in Postma si aiic in terminal
# retrieving posts: after creating dtabase in PgAdmin/ making a query (a connection) calling cursor from the try part passing the sql statements in .execute("""")- comande din PgAdmin 
    #cursor.execute("""SELECT * FROM posts """)
    #posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    #am scris my posts de la linia 21 si in Postman imi arata informaria notata/  ca sa imi arate in web browser dupa ipsdresa scriu the path to the url..aici /posts.

        # Join using sqlalchemy in python
# db.query(models.Post - o sa ne dea in terminal si in Postman toate column din Post-table/ .join-perform the join with sqlalchemy/ dupa .join(models.Vote-the table we want to join, models.Vote.post_id == models.Post.id-the colum we perform a join on )/ 
# getting the count - func.count / .label("votes") - numele pe care vrem sa ii dam coloanei ce am creat-o
# by defaul with sqalchemy this is an left inner join-isouter=True - make it a leftouter join/ .group_by(models.Post.id).all() - group by post.id using .group_by/ specifying the specific colum moldels.Post.id
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    return posts

 # Creating an Post
#@app.post("/createposts") - 1h 13min in video
# to extract the information that i have wrote in the body of Postman i have to assign a a variable within the path operation, to store the Body data
# in this case i assigned the 'payLoad' variable, i wrote the 'dict' because i have stored the information in dictionaries{}, and the body to import the Body from Postman
# i imported the body from the api libraries -from fastapi.params import Body-
# to extract all of the fileds from the Body from Postman, convert it to a Python dictionary, and store it inside a variable named payLoad
#def post_item(payLoad: dict = Body(...)):
# print the payLoad information. at the end i press send in the Postman
    #print(payLoad)
    #return{"message": "succesfully created posts"}                                        

# creating the Posts. i have edited the @app.post("/posts"), dar o mai scriu odata pt a salva si varianta originala
# to change the default status code(as a http status codes), in Create Posts in Postman, inside the decorator add status_code=status. and select the http status that we need.
# by default every time when someone send a will send a request to create a post will sent a 201-Created
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post) # the response model l-am introdys dupa ce am creat response schema in schems.py/ sche,as.-e numele fileului, .Post e numele class-ei
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db),  current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
# limit = 10 - limit query parameters, aici 10 posts, Optional pt search l-am importat sus
# functia de mai sus din paranteza- user_id: int = Depends(oauth2.get_current_user) - forces the user to be loged in before to create a post si cheam functia get_current_user din oauth2 file and passing the token that is used by the user
   # print(post) # daca aici scriu post.title in terminal o sa imi apara numele titlui ce l-am scris in Postma-body
    #print(post.dict()) # convert in dictionare by doing .dict 
    #post_dict = post.dict() # postp pydante model converted to a dictionary, min 4h12
    #post_dict['id'] = randrange(0, 1000000) # every entrance is going to be a unique number starting from 0 to 1000000
    #my_posts.append(post_dict)
# dupa 4h de curs; inserting new post in database; scrie exact ca in pgAdmim comenzile- SQL comenzi, in paranteza sunt la ce sectiuni adaugam informatie noua
# we dont want to insert strings and having errors in the db so we are going to sanitize all the data that we put in sql using %s-that represent a variable, and insert the actuali information in braces after the strings
    #cursor.execute("""INSERT INTO post (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published)) # the %s-method - is sanitize, make sure that there is no weird sql commands, and we are not vulnerable to sql injections; %s-are place holders
# pt informatia de sus RETURNING * -to return all the db
    #new_post = curosor.fetchone() # storing the RETURNING * in new post using fetchone()-method

    #conn.commit() # to save the information from pgAdmin in postgrase app

# informatia cu models.Post este inserata cind deja lucram cu DB, chem tabelul din fileul models pt a crea tabel.
#explicatia pt title=post.title - titlul nou va fi titlul pe care userul il va trimite prin intermediul post.title..si asa pt fiecare
# dupa ce am scris informatia la new_post verific in Postman daca este conexiunea/ la Create Posts - sa fie la Body + raw, scriu ceva nou la conent si title, apas send si ar trebuie sa imi apara informatia noua plus si publisehd.
# sa verific daca imi apare si in tabelul sau daca sa facut query in Postgres/ click stinga pe post + query tool - introduc select * from posts;
    #new_post = models.Post(title=post.title, content=post.content, published=post.published)
# dupa ce am scris new_post de sus si totul a functionat am modificat prin commanda de jos/ Explicatia: daca in fileul models sunt 50 de columns ex: date/yerar, etc, o sa dureze prea mult
# sa scrim pt fiecare date=posts.date .. si tot asa pt 50 sau mai mult/ titlte=post.title este stockat in pyrhon dictionary si trebuie sa unpact the dictionary prin **, formula e print(**post.dict())
# dupa verific in Postman si Postgres.
    #print(current_user.id)
    new_post = models.Post(owner_id=current_user.id, **post.dict())
#pentru a pushed ce am creat now in Postgres DB scriu urmatoarea commanda
    db.add(new_post)
#pentru a commit to save the information from pgAdmin in postgrase app/ dupa aceasta verifi incaodata - CreatePost-Send -in Postman si si execute(the play button) in Postgres
    db.commit()
# retrieve(ca un fel de return) noua query pe care am creat-o si store in tha variable new_post
    db.refresh(new_post)
    return new_post # dupa asta verific in postman la create post - scriu altceva la title sa vad ce modificari sunt; apoi in pg-admin la query tool scriu select*from posts s avad daca sunt cave modificri.
 # TO START THE WEBSERVER: in Terminal i wrote: uvicorn main:app --reload (main-is name of the file, app is the instance i have created above)to start the web server, the code iS on the fastapi.com
 # the --reload command is to save and to restart the server.  - this line its called dash

 # the schema(is a pydentic model)




                                     # Getting(retrieving) an individual post

 # retrieving one individual posts
@router.get("/{id}", response_model=schemas.PostOut) # the user is going to provide the id of the post that is intresting in
 # the id is called a path parameter 
def get_post(id: int, db: Session = Depends(get_db),  current_user: int = Depends(oauth2.get_current_user)): # define as an interger pt a accepta si litere
    #cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    #post = cursor.fetchone() #to take out - 1 post, first ia have checkd in getonepost - Postman
    # post = find_post(id) # call the function that find the post by an ID, convert manally as an int.

# deja cind creez tabelul cu query
# .filter(model.Post.id == id) un filtru(where) o sa se uite prin models si o sa verifice id-urile care o sa fie egal cu id pe care userl il request
# am folosit .first() - doar un singur id poate avea id care il cauta userul o sa caute primul instance cu acel id si o sa il returneze, nu o sa mai caute mai departe(daca ar fi sa pun .all)
# verific in Postam si Postgres id
    #post = db.query(models.Post).filter(models.Post.id == id).first()
# updating the get posts to join the columns
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post: # ca sa avem outputul 404
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
    return {"post_detail": post}



                                    # Deleting a Post
# to delete a post it startet with the decorator @ that is require a .delete http request., the same url/posts and the id to know wich post to delete
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db),  current_user: int = Depends(oauth2.get_current_user)): # define the function, pass the id and the type int- if not i will have a Internal Server Error in Postman
# the logic of deleting an post: to figure out which specific dictionary within this array has the specific id of whatever id we give it, and remove it from teh array
    # 1. find the indexin the array that has required ID .../ am creat o functie mai sus pt def_find_index ..pt a gasi index
    # le-am facut ca comment cind am inceput sa lucrez cu db:session..
    #cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(id)))
    #deleted_post = cursor.fetchone()
    #conn.commit()
# grabbimg the post model and filter using the id/ looking for the ud that we want to delete
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

# to check if an user is only his own post(till here 08:21 if we loggen in we can delete anyone posts)
# the next code have to match for a user to delete a post
    if post.owner_id != current_user.id:
# if it dosen't match raise http exce
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")


# calling the function that i have created above for the index
    #index = find_index_post(id)
   
    #return {'message': 'post was succesfully deleted'}
# daca schimb nr index de la url http://127.0.0.1:8000/posts/5 --in loc de 5 sa fie alt nr o sa am eroare pentru ca nu este post cu alt nr de id, scriu ca mai jos
    if post == None: # return None if it dosent exist, and raise an exception and write a message
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")
# if the post exist delete it
    post_query.delete(synchronize_session=False)
# to make changes in postman and postgres
    db.commit()
# dupa ce am scris toate aceste comzi ma duc in postman la delete post dupa url scriu ce id vreu sa sterg din posgres ex: /3, press send, dupa refresh in postgres sa vad daca a mers

    #my_posts.pop(index) # .pop() method removes the element at a specific position
# dupa mesajul cu post was succefully created pt a avea no data back scriu ca mai jos.
    return Response(status_code=status.HTTP_204_NO_CONTENT)
# dupa ce am verificat in Postman ca am mesajul post was succefully deleted, mai fac un send la Get Posts sa verific daca Postul a fost sters, acolo trebuie sa am un singur post
# tot la Delete post trebuie sa verifc status la pt HTTP status code, pt delete trebuie sa fie 204
# sa verific terminalul de la output ce greseli imi arata



                                        # Update Post (Put)
# dupa ce am creat Update Post cu Put method in Postman, creez functia
@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int,updated_post: schemas.PostCreate, db: Session = Depends(get_db),  current_user: int = Depends(current_user.id)):
# after creating the function above, next we have to find the index of the post with the specific id

    #cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %sRETURNING *""", (post.title, post.content, post.published, (str(id)))) 
    #updated_post = cursor.fetchone()
    #conn.commit() #  trebuie sa facem asta defiecare data cind facem modificari la db
# am copiat partea aceasta din Deleting a Post
    #index = find_index_post(id)
# verificam prin tabel dupa id
    post_query = db.query(models.Post).filter(models.Post.id == id)


# selectam prima iesire cu id care il dorim
    post = post_query.first()
# daca post nu exista send 404
    if post== None: 
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")

# to check if an user is only his own post(till here 08:21 if we loggen in we can delete anyone posts)
# the next code have to match for a user to delete a post
    if post.owner_id != oauth2.get_current_user.id:
# if it dosen't match raise http exce
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")

# daca exista, inseram ce o sa update, ce sectiuni din tabel
   #pentru test #post_query.update({'title': ' hey the title is update', 'content': 'the content is update'}, synchronize_session=False)
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

# this will take the data that we receive from front end wich is stored in Post, and it will converted in dictionari
    #post_dict = post.dict()
# set the id inside the dictionary created above, to be the id
    #post_dict['id'] = id
# calling my_posts and passing an index of the specific id that we want to update 
    #my_posts[index] = post_dict

# grab teh exact query from post_query=db.query... select the first one with the specific id, and it will return the upadate query
    return post_query.first()

    #return {'message': "updated post"}
                                # Overall - the logic of Update the post that i have made above
#the user is going to send a Put request to the specific id of the post he want to update-@app.put, we will do a quick check to find what is the index of that specific post
# within my_posts array, if the index dosen't exist we will show a 404, if it does exist first we'll take all the data receve from the front end, which is stored in Post- post: Post
# we'll converted to a regulat Python dictionary post.dict(), then we'll add the ID, that is built in - my_posts ['id'], and then we're going to say for the post within index - my post[index]
# to replace it with our new post_post