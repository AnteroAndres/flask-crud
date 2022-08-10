from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/")
def server_info():
    personas = [
        {
            "nombre":"Sergio",
            "apellidos":"Rojas Espino"
        },
        {
            "nombre":"Pedro",
            "apellidos":"Castillo"
        },
         {
            "nombre":"luchito",
            "apellidos":"chupa xd"
        },
    ]
    return jsonify(personas)

if __name__ == "__main__":
    app.run()