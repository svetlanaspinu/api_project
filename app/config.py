#                                           CODUL PENTRU VIRTUAL ENVIRONMENT

# pentru virtual environment
from pydantic import BaseSettings

from dotenv import load_dotenv

load_dotenv()  # am luat-o din online ca aveam erroare la /.env

# virtual environment/ ar trebui sa fie capital letter dar pydantic will read all the variables and it will look from an case-sensitive prospective so we dint need to capitalize them
# and its going to perform all the validation and it will store in the variable settings, de mai jos/ and we can access just using settings.database_password - sau orice informatie dorim
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
#secret key for token
    secret_key: str
#algorithm for sign in a token
    algorithm: str
    access_token_expire_minutes: int
# pentru informatia de sus/ none of this at the begginig are set, that's a lot of work to set everything on the machine, so i create .env(este ca un standard convention) tha contain all the environment variables file sa lucrez acolo..

#importing the .env file
    class Config:
        env_file ='/.env'
        
# creating an instance of the settings class
settings = Settings()

