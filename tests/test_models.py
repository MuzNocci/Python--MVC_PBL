import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from project.models import pessoa

def test_contcatecacao_nome_completo():
    p = pessoa.Pessoa('Lucky', 'Nocciolli', 5, '8654654654')
    assert p.nome_completo() == 'Lucky Nocciolli'
