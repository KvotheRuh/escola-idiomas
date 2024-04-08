from service.db  import engine
from models.base import Base
from models.pessoa import Pessoa
from models.endereco import Endereco
from models.telefone import Telefone
from models.pessoa_fisica import PessoaFisica
from models.pessoa_juridica import PessoaJuridica
from models.filial import Filial
from models.escola import Escola
from associativas.funcionarios_cursos import funcionarios_cursos_table
from models.cursos import Cursos
from models.ementa import Ementa
from associativas.alunos_turma import alunos_turma_table
from associativas.funcionarios_turma import funcionarios_turma_table
from models.turma import Turma
from models.alunos import Alunos
from models.funcionarios import Funcionarios
from models.contrato import Contrato

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)