from sqlalchemy import CHAR, INTEGER, ForeignKey 
from sqlalchemy.orm import  mapped_column, Mapped, relationship
from models.base import Base
from models.pessoa import Pessoa

class Telefone(Base):
    __tablename__= "telefone"
    codigo: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.codigo), primary_key=True)
    telefone_fixo: Mapped[str] = mapped_column(CHAR(10) ,nullable=True)
    celular: Mapped[str] = mapped_column(CHAR(11),nullable=False)
    pessoa = relationship("Pessoa", back_populates="contatos")