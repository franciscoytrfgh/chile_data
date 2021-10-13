import rut_chile
import sys
from persona import Persona
from patentes import Patente

def rut(r):
    _ = Persona(rut=r)
    _.datos
    return _

def patente(p):
    _ = Patente(p)
    _.datos
    _.datos["propietario"].datos
    return _

def identifica(que):
    if len(que) == 6 and que[0].isalpha() and que[0].isalpha():
        return patente(que)
    elif "-" in que and (len(que) == 9 or len(que) == 10):
        return rut(que)
    
    return "No se identifico " + que


def tojson(v):
    if type(v) == str:
        _ = identifica(v)
    else:
        _ = v
    _ = _.datos.copy()

    if "propietario" in _:
        _["propietario"] = _["propietario"].datos.copy()
    return _

if __name__ == "__main__":
    a =  (identifica(sys.argv[1]))
    print (a)