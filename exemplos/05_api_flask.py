from flask import Flask, jsonify

app = Flask(__name__)
alunos = [{"id": 1, "nome": "Ana"}, {"id": 2, "nome": "Bruno"}]


@app.get("/alunos")
def listar():
    return jsonify(alunos)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
