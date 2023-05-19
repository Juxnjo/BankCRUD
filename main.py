from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
import models
from database import engine, sessionlocal
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse 
from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory='templates')

app = FastAPI()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def raiz(request: Request, db: Session = Depends(get_db)):
    cuentas = db.query(models.Cuenta).order_by(models.Cuenta.id.desc())
    return templates.TemplateResponse('index.html', {'request': request, 'cuentas': cuentas})

@app.get ('/registrar')
async def registrar(request: Request):
    return templates.TemplateResponse('registrar.html', {'request': request})

@app.get('/transacciones')
async def transacciones(request: Request):
    return templates.TemplateResponse('transacciones.html', {'request': request})

@app.post('/agregar')
async def agregar(request: Request, numero_cuenta: int = Form(...), tipo_cuenta: str = Form(...), nombre: str = Form(...), saldo: float = Form(...) ,db: Session = Depends(get_db)):
    print(numero_cuenta)
    print(tipo_cuenta)
    print(nombre)
    print(saldo)
    cuentas = models.Cuenta(numero_cuenta=numero_cuenta, tipo_cuenta=tipo_cuenta, nombre=nombre, saldo=saldo)
    db.add(cuentas)
    db.commit()
    return RedirectResponse(url=app.url_path_for('raiz'), status_code=status.HTTP_303_SEE_OTHER)

@app.get('/editar/{cuenta_id}')
async def editar(request: Request, cuenta_id: int, db: Session = Depends(get_db)):
    cuenta = db.query(models.Cuenta).filter(models.Cuenta.id == cuenta_id).first()
    return templates.TemplateResponse('editar.html', {'request': request, 'cuenta': cuenta})

@app.post('/actualizar/{cuenta_id}')
async def actualizar(request: Request, cuenta_id: int, numero_cuenta: int = Form(), tipo_cuenta: str = Form(), nombre: str = Form(), saldo: float = Form() ,db: Session = Depends(get_db)):
    cuenta = db.query(models.Cuenta).filter(models.Cuenta.id == cuenta_id).first()
    cuenta.numero_cuenta = numero_cuenta
    cuenta.tipo_cuenta = tipo_cuenta
    cuenta.nombre = nombre
    cuenta.saldo = saldo
    db.commit()
    return RedirectResponse(url=app.url_path_for('raiz'), status_code=status.HTTP_303_SEE_OTHER)

@app.get('/retirarse/{cuenta_id}')
async def retirarse(request: Request, cuenta_id: int, db: Session = Depends(get_db)):
    cuenta = db.query(models.Cuenta).filter(models.Cuenta.id == cuenta_id).first()
    cuenta.saldo = 0
    db.commit()
    return RedirectResponse(url=app.url_path_for('raiz'), status_code=status.HTTP_302_FOUND)

@app.get('/borrar/{cuenta_id}')
async def borrar(request: Request, cuenta_id: int, db: Session = Depends(get_db)):
    cuenta = db.query(models.Cuenta).filter(models.Cuenta.id == cuenta_id).first()
    db.delete(cuenta)
    db.commit()
    return RedirectResponse(url=app.url_path_for('raiz'), status_code=status.HTTP_302_FOUND)