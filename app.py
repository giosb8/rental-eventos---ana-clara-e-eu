from flask import Flask, render_template, request, jsonify, session, redirect
import pg8000
from config import DB_CONFIG

app = Flask(__name__)

app.secret_key = "rental-eventos-chave"


def conectar_banco():
    return pg8000.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )

# =========================
# TELA DE LOGIN
# =========================

@app.route("/")
def home():

    if "usuario" in session:
        return redirect("/principal")

    return render_template("index.html")


# =========================
# LOGIN
# =========================

@app.route("/login", methods=["POST"])
def login():

    dados = request.get_json()

    usuario = dados.get("usuario")
    senha = dados.get("senha")

    if not usuario or not senha:
        return jsonify({
            "status": "erro",
            "mensagem": "Preencha o usuário e a senha."
        }), 400

    try:

        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT *
            FROM usuario
            WHERE usuario = %s
            AND senha = %s
            """,
            (usuario, senha)
        )

        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()

        if resultado:

            session["usuario"] = usuario

            return jsonify({
                "status": "sucesso",
                "mensagem": "Login realizado com sucesso."
            })

        return jsonify({
            "status": "erro",
            "mensagem": "Usuário ou senha incorretos."
        }), 401

    except Exception as erro:

        print("ERRO NO LOGIN:", erro)

        return jsonify({
            "status": "erro",
            "mensagem": "Não foi possível realizar o login."
        }), 500


# =========================
# INTERFACE PRINCIPAL
# =========================

@app.route("/principal")
def principal():

    if "usuario" not in session:
        return redirect("/")

    return render_template(
        "principal.html",
        usuario=session["usuario"]
    )


# =========================
# LOGOUT
# =========================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# =========================
# EXECUTAR SISTEMA
# =========================

if __name__ == "__main__":
    app.run(debug=True)