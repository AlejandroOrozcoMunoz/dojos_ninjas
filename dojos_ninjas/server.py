from flask_app import app

#FALTA controladores -> Archivos con rutas
from flask_app.controllers import dojos_ninjas_controller

if __name__=="__main__":
    app.run(debug=True)
