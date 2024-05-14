from flask import Flask
from controllers.book_controller import book_bp
from flask_swagger_ui import get_swaggerui_blueprint
from database import db

app = Flask(__name__)
# Cofigura la URL de la documentacion OpenAPI
SWAGGER_URL = "/api/docs"

# Ruta de tu archivo OpenAPI/Swagger
API_URL="/static/swagger.json"

# Inicialicza el Blueprint de Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,API_URL,config={"app_name":"Biblioteca API"}
)
app.register_blueprint(swagger_ui_blueprint,url_prefix=SWAGGER_URL)

# Configuracion de la base de datos 
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

# Inicializa la base de datos
db.init_app(app)

# Registra el blueprint de animales en la aplicacion
app.register_blueprint(book_bp, url_prefix="/api")

# Crea las tablas si no existen
with app.app_context():
    db.create_all()

#ejecuta la aplicacion
if __name__ == "__main__":
    app.run(debug=True)