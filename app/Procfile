# a procfile - a text file in the root directory of your application to explicity what command should be executed to start your app.

web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}

# web - declaring the app as a web process/ is the only process that can receive external HHTP traffic from heroku's routers.
# uvicorn app.main:app - passing the name of the app(the same as in vs)
# --host=0.0.0.0 - providing a host ip/ os empty because ni matter what host we provide, heroku is going to accept it.
# --port - if we dont provide the port is going to default to 8000/ heroku is going to provide a port and we have to accept it regardless of what it is
# to accept a environment variable or to reference one - ${} - we want to take whatever value heroku give us with the environment varialbe of port -PORT, and assigned here/ it gives a default value of 5000 if it didnt provide one.
# Heroku will always provide a PORT nr so we dont need -5000
