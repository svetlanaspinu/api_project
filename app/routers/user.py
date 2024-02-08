from .. import models, schemas, utils
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter# import the response ca sa ascunda raspinsuri gen 404 la paginile web./ status la linia 80 pt a vedea fiecare http satus codes.
from sqlalchemy.orm import Session
from ..database import get_db


# pentru a connecta decoratorul @
router = APIRouter(
    prefix="/users",
    tags=['Users']
)

#Creating a path operation for a new user 6h
# the line starting with decorator @ it will create a new post request that will be sent to the url user/ when we create something the default status code should be HTTP_201
# we dont have acces to app so we repalce the word app with rputer
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)): # in paranteza-using our database to create a new user

# dupa ce am instalatat CryptoContext si am scris pwd_context linia 2o/ scriu codul de mai jos: hash the password - user.password
    hashed_password = utils.hash(user.password)
# update the pydantic user model/ the password is stored in user.password
    user.password = hashed_password 

# mai jos e cum sa salvam informatie noua in Postman si Postgres
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# retreive an information about an user based on the user id
@router.get('/{id}', response_model=schemas.UserOut)# response_model -este ca sa nu ne apara passwordul in postman
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
# if the user is not found
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with id: {id} does not exist.")

# if the user is found - return the user
    return user