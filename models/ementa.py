from sqlalchemy import VARCHAR,TIME, INTEGER, ForeignKey 
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.cursos import Cursos
from models.base import Base

class Ementa(Base):
    __tablename__ = "ementa"
    codigo_ementa: Mapped[int] = mapped_column(INTEGER, primary_key=True, autoincrement=True)
    codigo_cursos: Mapped[int] = mapped_column(INTEGER, ForeignKey(Cursos.codigo_cursos), nullable=False)
    metodologia: Mapped[str] = mapped_column(VARCHAR(300), nullable=False)
    duracao: Mapped[TIME] = mapped_column(TIME, nullable=False)
    cursos = relationship("Cursos" , back_populates="ementas")