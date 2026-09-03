
from flask import Flask
from flask_smorest import Api, Blueprint
from marshmallow import Schema, fields
from flask_sqlalchemy import SQLAlchemy

from config import DB_CONFIG


app = Flask(__name__)


# =========================
# CONFIGURAÇÃO DO BANCO
# =========================

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql+pg8000://"
    f"{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}"
    f"/{DB_CONFIG['database']}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# =========================
# CONFIGURAÇÃO FLASK-SMOREST
# =========================

app.config["API_TITLE"] = "Rental Eventos API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"

app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = (
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
)


# =========================
# BANCO
# =========================

db = SQLAlchemy(app)


# =========================
# API
# =========================

api = Api(app)


# =========================
# MODEL FUNCIONÁRIO
# =========================

class Funcionario(db.Model):

    __tablename__ = "funcionario"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    senha = db.Column(
        db.String(255),
        nullable=False
    )


# =========================
# SCHEMA DE LOGIN
# =========================

class LoginSchema(Schema):

    email = fields.Email(
        required=True
    )

    senha = fields.String(
        required=True
    )


# =========================
# SCHEMA DE RESPOSTA
# =========================

class FuncionarioResponseSchema(Schema):

    id = fields.Integer()

    nome = fields.String()

    email = fields.Email()


# =========================
# BLUEPRINT
# =========================

blp = Blueprint(
    "funcionario",
    "funcionario",
    url_prefix="/funcionario",
    description="Operações relacionadas ao funcionário"
)


# =========================
# LOGIN
# =========================

@blp.route("/login")
class Login:

    @blp.arguments(LoginSchema)
    @blp.response(200, FuncionarioResponseSchema)
    def post(self, dados):

        funcionario = Funcionario.query.filter_by(
            email=dados["email"],
            senha=dados["senha"]
        ).first()

        if not funcionario:

            return {
                "mensagem": "E-mail ou senha incorretos."
            }, 401

        return funcionario


# =========================
# REGISTRAR BLUEPRINT
# =========================

api.register_blueprint(blp)


# =========================
# EXECUTAR API
# =========================

if __name__ == "__main__":

    app.run(
        debug=True
    )

