from sqlalchemy import ForeignKey , Column, Table
from models.base import Base

funcionarios_turma_table = Table(
    "funcionarios_turma",
    Base.metadata,
    Column("codigo_turma", ForeignKey("turma.codigo_turma"), primary_key=True),
    Column("codigo_funcionarios", ForeignKey("funcionarios.codigo_funcionarios"), primary_key=True),
)