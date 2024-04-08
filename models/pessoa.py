from sqlalchemy import INTEGER
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.base import Base

class Pessoa(Base):
    __tablename__= "pessoa"
    codigo: Mapped[int] = mapped_column(INTEGER, autoincrement=True , primary_key=True)
    moradias = relationship("Endereco", back_populates="pessoa")
    contatos = relationship("Telefone", back_populates="pessoa")
    cliente = relationship("PessoaFisica", back_populates="pessoa")
    empresa = relationship("PessoaJuridica", back_populates="pessoa")
    filiais = relationship("Filial", back_populates="pessoa")
    aluno = relationship("Alunos", back_populates="pessoa")
    docentes = relationship("Funcionarios", back_populates="pessoa")