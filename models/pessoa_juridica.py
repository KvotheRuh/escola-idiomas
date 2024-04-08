from sqlalchemy import DATE, VARCHAR, CHAR, INTEGER, ForeignKey 
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import date
from models.pessoa import Pessoa
from models.base import Base


class PessoaJuridica(Base):
    __tablename__ = "pessoa_juridica"
    codigo: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.codigo), primary_key=True)
    email_institucional : Mapped[str] = mapped_column(VARCHAR(50),nullable=False, unique=True)
    cnpj : Mapped[str] = mapped_column(CHAR(14), nullable=False, unique=True)
    data_abertura : Mapped[date] = mapped_column(DATE,nullable=False)
    nome_fantasia : Mapped[str] = mapped_column(VARCHAR(50), nullable=False, unique=True)
    razao_social : Mapped[str] = mapped_column(VARCHAR(150), nullable=False, unique=True)
    pessoa = relationship("Pessoa", back_populates="empresa")