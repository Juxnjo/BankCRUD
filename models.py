from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Cuenta(Base):
    __tablename__ = 'cuentas'
    id = Column(Integer, primary_key=True)
    numero_cuenta = Column(Integer)
    tipo_cuenta = Column(String(50))
    nombre = Column(String(50))
    saldo = Column(Float(50))
    
    movimientos = relationship("Movimientos", back_populates="cuenta")
    
    def __repr__(self):
        return '<Cuenta %r>' % (self.id)   
    
class Movimientos(Base):
    __tablename__ = 'movimientos'
    id = Column(Integer, primary_key=True)
    valor_transaccion = Column(Float)
    numero_cuenta = Column(Integer, ForeignKey('cuentas.numero_cuenta'))
    fecha = Column(String(50))
    tipo_transaccion_id = Column(Integer, ForeignKey('tipo_transaccion.id'))

    cuenta = relationship("Cuenta", back_populates="movimientos")
    tipo_transaccion = relationship("TipoTransaccion", back_populates="movimientos")

    def __repr__(self):
        return '<Movimientos %r>' % (self.id)

class TipoTransaccion(Base):
    __tablename__ = 'tipo_transaccion'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(50))

    movimientos = relationship("Movimientos", back_populates="tipo_transaccion")

    def __repr__(self):
        return '<TipoTransaccion %r>' % (self.id)