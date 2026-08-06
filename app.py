from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():

    dados = request.get_json()

    usuario = dados["usuario"]
    senha = dados["senha"]

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario=? AND senha=?",
        (usuario, senha)
    )

    resultado = cursor.fetchone()

    conexao.close()

    if resultado:
        return jsonify({"status":"sucesso"})
    else:
        return jsonify({"status":"erro"})

if __name__ == "__main__":
    app.run(debug=True)