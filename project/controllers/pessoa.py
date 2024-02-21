import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from models.pessoa import Pessoa
from typing import List

class PessoaController:

    pessoa = []

    @classmethod
    def salvar_pessoa(cls, pessoa: Pessoa):
        cls.pessoa.append(pessoa)

    @classmethod
    def listar_pessoas(cls) -> List[Pessoa]:
        return cls.pessoa