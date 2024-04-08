from sqlalchemy import DATETIME,INTEGER, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.base import Base
from models.pessoa import Pessoa
from associativas.funcionarios_cursos import funcionarios_cursos_table
from associativas.funcionarios_turma import funcionarios_turma_table


class Funcionarios(Base):
    __tablename__ = "funcionarios"
    codigo_funcionarios: Mapped[int]= mapped_column(INTEGER, primary_key=True, autoincrement=True)
    codigo_pessoa: Mapped[int]= mapped_column(INTEGER,ForeignKey(Pessoa.codigo), nullable=False) 
    carga_horaria: Mapped[DATETIME]= mapped_column(DATETIME, nullable=False) 
    turmas = relationship("Turma", secondary=funcionarios_turma_table, back_populates="funcionarios")
    cursos = relationship("Cursos", secondary=funcionarios_cursos_table, back_populates="funcionarios")
    relacao_contratual = relationship("Contrato", back_populates="funcionarios")
    pessoa = relationship("Pessoa", back_populates="docentes")