from src.app import app
import src.controllers.apicontroller
from config import PORT
import src.controllers.apilabcontroller


app.run("0.0.0.0", PORT, debug=True)