from sqlalchemy import INTEGER, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.base import Base
from models.alunos import Alunos
from models.funcionarios import Funcionarios
from models.alunos import Alunos


class Contrato(Base):
    __tablename__ = "contrato"
    codigo_contrato: Mapped[int]= mapped_column(INTEGER, primary_key=True, autoincrement=True)
    contrato_alunos: Mapped[int]= mapped_column(INTEGER, ForeignKey(Alunos.matricula), nullable=False) 
    codigo_funcionarios: Mapped[int]= mapped_column(INTEGER, ForeignKey(Funcionarios.codigo_funcionarios), nullable=False)
    alunos = relationship("Alunos", back_populates="contratos")
    funcionarios = relationship("Funcionarios", back_populates="ralacao_contratual")