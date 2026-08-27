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

    if "funcionario" in session:
        return redirect("/principal")

    return render_template("index.html")


# =========================
# LOGIN
# =========================

@app.route("/login", methods=["POST"])
def login():

    dados = request.get_json()

    email = dados.get("email")
    senha = dados.get("senha")

    if not email or not senha:

        return jsonify({
            "status": "erro",
            "mensagem": "Preencha o e-mail e a senha."
        }), 400

    try:

        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT id, nome, email
            FROM funcionario
            WHERE email = %s
            AND senha = %s
            """,
            (email, senha)
        )

        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()

        if resultado:

            session["funcionario"] = resultado[2]
            session["nome"] = resultado[1]

            return jsonify({
                "status": "sucesso",
                "mensagem": "Login realizado com sucesso."
            })

        return jsonify({
            "status": "erro",
            "mensagem": "E-mail ou senha incorretos."
        }), 401

    except Exception as erro:

        print("ERRO NO LOGIN:", erro)

        return jsonify({
            "status": "erro",
            "mensagem": "Não foi possível realizar o login."
        }), 500


# =========================
# CADASTRO DE USUÁRIO
# =========================

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro_funcionario():

    if request.method == "GET":
        return render_template("cadastro.html")

    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")

    if not nome or not email or not senha:
        return "Preencha todos os campos.", 400

    try:

        conexao = conectar_banco()
        cursor = conexao.cursor()

        # Verifica se o e-mail já está cadastrado
        cursor.execute(
            """
            SELECT id
            FROM funcionario
            WHERE email = %s
            """,
            (email,)
        )

        funcionario_existente = cursor.fetchone()

        if funcionario_existente:

            cursor.close()
            conexao.close()

            return "Este e-mail já está cadastrado.", 400

        # Insere o novo usuário
        cursor.execute(
            """
            INSERT INTO funcionario (nome, email, senha)
            VALUES (%s, %s, %s)
            """,
            (nome, email, senha)
        )

        conexao.commit()

        cursor.close()
        conexao.close()

        return redirect("/")

    except Exception as erro:

        print("ERRO NO CADASTRO:", erro)

        return "Não foi possível realizar o cadastro.", 500


# =========================
# INTERFACE PRINCIPAL
# =========================

@app.route("/principal")
def principal():

    if "funcionario" not in session:
        return redirect("/")

    return render_template(
        "principal.html",
        funcionario=session["funcionario"]
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