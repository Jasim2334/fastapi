from fastapi import FastAPI,Depends,HTTPException


app = FastAPI()


@app.get('/')
def sample():
    return {'status':True,'msg':'Hello World'}