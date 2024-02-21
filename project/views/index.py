import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controllers.pessoa import PessoaController
from models.pessoa import Pessoa


while True:

    decisao = int(input('Digite 1 para cadastrar e 2 para listar: '))

    if decisao == 1:

        nome = input('Nome: ')
        sobrenome = input('Sobrenome: ')
        idade = input('Idade: ')
        cpf = input('CPF: ')

        p = Pessoa(nome=nome, sobrenome=sobrenome, idade=idade, cpf=cpf)
        PessoaController.salvar_pessoa(p)

    elif decisao == 2:

        for pessoa in PessoaController.listar_pessoas():
            print(f'Nome: {pessoa.nome}\nSobrenome: {pessoa.sobrenome}\nIdade: {pessoa.idade}\nCPF: {pessoa.cpf}')
            print('##########')