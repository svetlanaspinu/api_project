#   Pentru a crea tokens
# informatie de pe https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/?h=oauth2 / am instalat in terminal si am importat mai jos 
from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings
#tokenurl is the end point of our login endpoint/ login din paranteza vine din auth.py - @router.post('/login')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# provide the SECRET_KEY / numarul e de pe site fastapi.
#SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7" # it's not ok to store the secret key within the actual code
SECRET_KEY = settings.secret_key
# provide the ALGORITHM that we want to use
#ALGORITHM = "HS256"
Algorithm = settings.algorithm
# provide the EXPIRATION TIME OF THE TOKEN (how long a user should be logged in after perfomring a login operation, here 60 min)
#ACCESS_TOKEN_EXPIRE_MINUTES = 60
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
#       migrating the variables in venv. pentru informatia de sus..cind variabilele sunt importate in mai multe file-uri

def create_access_token(data: dict):
# making a copy of the data from the parantese to store new variables/ 
    to_encode = data.copy() # holds all the data that we are going to encode in JWT TOKEN
# create the expiration field/ first import the datetime libraray
    expire = datetime.utcnow() + to_encode(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

# creating the jwt token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# creating a function to verify the access token 
# jos in paranteza: passing a token(it will be a string), passing teh specific credentilas_exception(what our exception should be, if the credentials it will match or if there's aany problem with the toke)
def verify_access_token(token: str, credentials_exception):
# we can have error in running the code so we have to taste using try_except block
    try: 
# prin jwt-acces the jwt library, having the funtion(sus am folosit encode pt a crea token aici pt a verifica folosim decode)/ in paranteza dupa edecode inseram token-ul
# passing the secret key(so we can decoded), and passing the Algorithm that we use/ secret_key si algorithm sun tinserate de sus - linia 9/10
        payload =  jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
# to extract the data/ dupa get(we need to put the specific field that we put in)/in auth.py users_id will take the id of the user so we are using it here
# this is store in a variable called id - type - string   
        id : payload.get("user_id")
# if no id raise a credentials_exception(whatever exception provide in the credentials_exception it will shows that)
        if id is None:
            raise credentials_exception 
# validate that is matches our specific schema
        token_data = schemas.TokenData(id=id)
# using the except JWT- is coming from jose library importat sus
    except JWTError:
        raise credentials_exception
   
    
    return token_data

# create a function that will take the token token from the requesrt automaticly extract the id for us/ verify if the token is correct by calling verify_access_token
# it will fetch the user automatically from the database and adeed as parameter into the path operations function
# oauth2_scheme - am creat-o sus - toata informatia este notata sus
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
# define the credentials excetions that will pass in verify_access_toke/ when the credentilas are wring ot any issue with JWToken what exceptio should we raise
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
  
# we have the get_current_user function to only call the verify_access_toke - that is already noted above. The idea behind the get_current_user function once the verify_access_token return the token_data which is the id
# the get_current_user fn fetch the user from the database, so we can attach the user to any path operations so we can perfom any neccesary logic
#   how to fetch an user (the data back is just an id)/ am importat database sus si am introdus-o in paranteza la get_current_user, am instalat si Session din sqlalchemy pt aceasta, tot sus
    token = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first() # filtrat dupa token id si sa fie primul
    
    return user

 
