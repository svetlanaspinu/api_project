from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm    #import autorizatia de a crea password
from sqlalchemy.orm import Session # import the database
#import the db function
from ..database import get_db
from .. import schemas, models, utils, oauth2

router = APIRouter(tags='Authentication')

# creating a post request
@router.post('/login', response_model=schemas.Token)
# dupa ce am importat Oauth2PaawordRequestForm..provide a dependencie that required to retriev the credentials and fastapi will store the inform in user_credentials
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
# OAuth2PasswordRequestForm - dupa ce am instalat si am scris in comanda de mai sus, in Postman selectez form-data din Body pentru a testa/ scriu username si password pentru testare/ 7h 13'
# cu user_credentials we can accesee all the user information

#making a request to the database to our user table to retrieve the user based on his email(filtru din comanda de jos)
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

# no user with that specific name, return error
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')

# dupa ce am importat file utils, il run pentru a face functia def verify aici
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials' )

    # create token /  import the token created in oauth2 file/  i decide wat information i want in dict / to encode{..aici user_id}
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    # return token
    return {"access_token": access_token, "token_type": "bearer"} 
# dupa aceasta am creat un nou request in postman - Login User - sa testez.
