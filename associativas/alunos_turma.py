from sqlalchemy import ForeignKey , Column, Table
from models.base import Base

alunos_turma_table = Table(
    "alunos_turma",
    Base.metadata,
    Column("codigo_turma", ForeignKey("turma.codigo_turma"), primary_key=True),
    Column("matricula", ForeignKey("alunos.matricula"), primary_key=True),
)