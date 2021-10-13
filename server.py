from flask import Flask,jsonify,request
from patentes import Patente
import full


api = Flask(__name__)

@api.route('/api/patentes/<p>/', methods=['GET'])
def get_patente(p):
    
    if len(p) == 6:
        return jsonify(full.tojson(str(p)))

    return "['error']"

@api.route("/buscar", methods=["GET"])
def buscar():
    p = request.args.get("patente")
    t = request.args.get("tipo")
    return jsonify(full.tojson(str(p)))

@api.route("/")
def index():
    return """
    <form action="/buscar" method="GET" style="width: 100px; margin: 50px auto;">
    <fieldset>
        <legend>Rut o Patente</legend>
        <input name="patente" type="text" placeholder="AABBCC"><br>

        <input type="radio" id="vehiculo" name="tipo" value="vehiculo">
        <label for="vehiculo">Auto</label><br>

        <input type="radio" id="moto" name="tipo" value="moto">
        <label for="moto">Moto</label><br>
        <input type="submit" value="buscar">
    </fieldset>
    
    
    
    </form>
    """

if __name__ == '__main__':
    api.run() 