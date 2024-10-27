class Membro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.treinos = []

    def adicionar_treino(self, treino):
        self.treinos.append(treino)

    def mostrar_informacoes(self):
        info = f'Nome: {self.nome}, idade: {self.idade}\nTreinos:'
        for treino in self.treinos:
            info += f'\n- {treino.descricao}'
        return info


class Treino:
    def __init__(self, descricao, duracao, data):
        self.descricao = descricao
        self.duracao = duracao
        self.data = data

    def mostrar_informacoes(self):
        return f'Descrição: {self.descricao}, Duração: {self.duracao}, Data: {self.data}'


class Academia:
    def __init__(self):
        self.membros = []

    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def listar_membros(self):
        for membro in self.membros:
            print(membro.mostrar_informacoes())

    def salvar_membros_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            for membro in self.membros:
                arquivo.write(f'{membro.nome}, {membro.idade}\n')
                for treino in membro.treinos:
                    arquivo.write(f'{treino.descricao}, {treino.duracao}, {treino.data}\n')
        print(f'Membros e treinos salvos no arquivo {nome_arquivo} com sucesso!')


def main():
    academia = Academia()
    
    while True:
        print("\n1. Adicionar Membro")
        print("2. Adicionar Treino ao Membro")
        print("3. Listar Membros e Treinos")
        print("4. Salvar Membros e Treinos")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do membro: ")
            idade = input("Digite a idade do membro: ")
            membro = Membro(nome, idade)
            academia.adicionar_membro(membro)
            print("Membro adicionado com sucesso!")

        elif escolha == '2':
            nome = input("Digite o nome do membro para adicionar o treino: ")

            for membro in academia.membros:
                if membro.nome == nome:
                    descricao = input("Digite a descrição do treino: ")
                    duracao = input("Digite a duração do treino: ")
                    data = input("Digite a data do treino: ")
                    treino = Treino(descricao, duracao, data)
                    membro.adicionar_treino(treino)
                    print("Treino adicionado com sucesso!")
                    break
            else:
                print("Membro não encontrado")

        elif escolha == '3':
            print("\nLista de Membros e Treinos: ")
            academia.listar_membros()

        elif escolha == '4':
            nome_arquivo = input("Digite o nome do arquivo para salvar membros e treinos: ")
            academia.salvar_membros_em_arquivo(nome_arquivo)

        elif escolha == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
