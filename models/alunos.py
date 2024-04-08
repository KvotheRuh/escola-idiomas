from sqlalchemy import CHAR, DATETIME,INTEGER, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.base import Base
from models.pessoa import Pessoa
from associativas.alunos_turma import alunos_turma_table

class Alunos(Base):
    __tablename__ = "alunos"
    matricula: Mapped[int] = mapped_column(INTEGER, primary_key=True, autoincrement=True) 
    codigo_pessoa: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.codigo), nullable=False) 
    notas: Mapped[str] = mapped_column(CHAR(5), nullable=True) 
    carga_horaria: Mapped[DATETIME] = mapped_column(DATETIME, nullable=False)
    turmas = relationship("Turma", secondary=alunos_turma_table, back_populates="alunos")
    pessoa = relationship("Pessoa", back_populates="aluno")
    contratos = relationship("Contrato", back_populates="alunos")