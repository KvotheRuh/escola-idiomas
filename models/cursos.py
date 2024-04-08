from sqlalchemy import VARCHAR, INTEGER, ForeignKey 
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.escola import Escola
from associativas.funcionarios_cursos import funcionarios_cursos_table
from models.base import Base


class Cursos(Base):
    __tablename__ = "cursos"
    codigo_cursos: Mapped[int] = mapped_column(INTEGER, primary_key=True, autoincrement=True)
    codigo_escola: Mapped[int] = mapped_column(INTEGER, ForeignKey(Escola.codigo_escola), nullable=False)
    nome: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)
    escola = relationship("Escola" , back_populates="curso")
    ementas = relationship("Cursos" , back_populates="cursos")
    salas = relationship("Cursos", back_populates="cursos")
    funcionarios = relationship("Funcionarios", secondary=funcionarios_cursos_table, back_populates="cursos")