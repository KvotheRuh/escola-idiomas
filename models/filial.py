from sqlalchemy import INTEGER, ForeignKey 
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.pessoa import Pessoa
from models.base import Base


class Filial(Base):
    __tablename__ = "filial"
    codigo_filial: Mapped[int] = mapped_column(INTEGER,autoincrement=True, primary_key=True)
    codigo_pessoa: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.codigo), nullable=False)
    pessoa = relationship("Pessoa", back_populates="filiais")
    sede = relationship("Filial", back_populates="filial")