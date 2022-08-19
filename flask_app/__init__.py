#inicializa nuestra aplicacion 
from flask import Flask

app = Flask(__name__)

#establecemos una secret key
app.secret_key="mi llave super secreta"