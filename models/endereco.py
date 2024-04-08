from sqlalchemy import VARCHAR, CHAR,INTEGER, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.base import Base
from models.pessoa import Pessoa

class Endereco(Base):
    __tablename__= "endereco"
    codigo: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.codigo), primary_key=True)
    estado: Mapped[str] = mapped_column(VARCHAR(100),nullable=False)
    cidade: Mapped[str] = mapped_column(VARCHAR(100),nullable=False)
    numero: Mapped[str] = mapped_column(CHAR(3), nullable=False)
    bairro: Mapped[str] = mapped_column(VARCHAR(100),nullable=False)
    cep: Mapped[str] = mapped_column(CHAR(8), nullable=False)
    pessoa = relationship("Pessoa", back_populates="moradias")
