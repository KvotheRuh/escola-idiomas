from sqlalchemy import ForeignKey , Column, Table
from models.base import Base


funcionarios_cursos_table = Table(
    "funcionarios_cursos",
    Base.metadata,
    Column("codigo_cursos", ForeignKey("cursos.codigo_cursos"), primary_key=True),
    Column("codigo_funcionarios", ForeignKey("funcionarios.codigo_funcionarios"), primary_key=True),
)