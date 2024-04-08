from sqlalchemy import DATETIME,INTEGER, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.base import Base
from models.cursos import Cursos
from associativas.alunos_turma import alunos_turma_table

class Turma(Base):
    __tablename__ = "turma"
    codigo_turma: Mapped[int] = mapped_column(INTEGER, primary_key=True, autoincrement=True) 
    codigo_cursos: Mapped[int] = mapped_column(INTEGER, ForeignKey(Cursos.codigo_cursos), nullable=False) 
    carga_horaria: Mapped[DATETIME] = mapped_column(DATETIME, nullable=False)
    cursos =  relationship("Cursos", back_populates="salas")
    alunos = relationship("Alunos", secondary=alunos_turma_table, back_populates="turma")
    funcionarios = relationship("Funcionarios", secondary=alunos_turma_table, back_populates="turma")