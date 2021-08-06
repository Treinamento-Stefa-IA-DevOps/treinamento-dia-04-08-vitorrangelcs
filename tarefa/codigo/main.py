#vitor rangel
import pickle
from fastapi import FastAPI

app = FastAPI(
    title = 'Api Titanic',
    description = ''
)
@app.post('/model')
## Coloque seu codigo na função abaixo

async def titanic(Sex:int,Age:float, Lifeboat:int, Pclass:int):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)    
    
    predi = titanic.predict([[Sex, Age, Lifeboat, Pclass]]).tolist()

    try:
        return {
            'survived': bool(predi[0]),
            'status': 200,
            'message': 'Deu tudo certo \o' if bool(predi[0]) else 'Não sobreviveu',
        }
    except Exception:
        return {
            'message': 'Estou com algum problema :('
        }

@app.get('/model')
def get():
    return {'hello':'test'}
