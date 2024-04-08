from sqlalchemy import VARCHAR, INTEGER, ForeignKey 
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.filial import Filial
from models.base import Base

class Escola(Base):
    __tablename__ = "escola"
    codigo_escola: Mapped[int] = mapped_column(INTEGER, primary_key=True, autoincrement=True)
    codigo_filial: Mapped[int] = mapped_column(INTEGER, ForeignKey(Filial.codigo_filial), nullable=False)
    nome: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)
    filial = relationship("Filial", back_populates="sede")
    curso = relationship("Escola" , back_populates="escola")