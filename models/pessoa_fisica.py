from sqlalchemy import DATE, VARCHAR, CHAR, INTEGER, ForeignKey 
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import date
from models.pessoa import Pessoa
from models.base import Base

class PessoaFisica(Base):
    __tablename__ = "pessoa_fisica"
    codigo: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.codigo), primary_key=True)
    data_nasc: Mapped[date] = mapped_column(DATE,nullable=False, unique=True)
    email_pessoal: Mapped[str] = mapped_column(VARCHAR(45), nullable=False, unique=True)
    altura: Mapped[str] = mapped_column(CHAR(10), nullable=False)
    nome: Mapped[str] = mapped_column(VARCHAR(100),nullable=False,unique=True)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    pessoa = relationship("Pessoa", back_populates="cliente")