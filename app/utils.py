from passlib.context import CryptContext #pentru a crea secure password/ intii am instalat-pip install "passlib[bcrypt]"-in terminal-PassLib is a great Python package to handle password hashes.
# dupa ce am importat passlib si CryptContext linia 7/ next code telling passlib what is the hashing algortihm that we want to use - bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto") # pwd-password context

# define a function that we can call ane will contain the password
def hash(password: str):
    return pwd_context.hash(password) # wil return the password that the users passes in

# this function is response with comparing the two hashes(if the login in auth.py are the same in database)
def verify(plain_password, hashed_password): # plain_password is the password the user will try to attempt, hash_password comes from the database
    return pwd_context.verify(plain_password, hashed_password) # this function will do all teh test of comparision for the passwords