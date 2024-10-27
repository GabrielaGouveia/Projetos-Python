class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_informacoes(self):
        return f'Produto: {self.nome} | Preço: R${self.preco:.2f}'


class Pedidos:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def calcular_total(self):
        total = sum(produto.preco for produto in self.itens)
        return total

    def mostrar_informacoes(self):
        info = 'Itens do Pedido:\n'
        for produto in self.itens:
            info += f'- {produto.mostrar_informacoes()}\n'
        info += f'Total: R${self.calcular_total():.2f}'
        return info


class Restaurante:
    def __init__(self):
        self.menu = []

    def adicionar_produto_ao_menu(self, produto):
        self.menu.append(produto)

    def listar_menu(self):
        for produto in self.menu:
            print(produto.mostrar_informacoes())

    def criar_pedido(self):
        return Pedidos()


def main():
    restaurante = Restaurante()

    # Adicionar produtos ao menu
    restaurante.adicionar_produto_ao_menu(Produto("Hambúrguer", 15.50))
    restaurante.adicionar_produto_ao_menu(Produto("Pizza", 25.00))
    restaurante.adicionar_produto_ao_menu(Produto("Refrigerante", 5.00))
    restaurante.adicionar_produto_ao_menu(Produto("Suco", 7.00))

    pedido = restaurante.criar_pedido()

    while True:
        print("\n1. Mostrar Menu")
        print("2. Adicionar produto ao pedido")
        print("3. Mostrar pedido e Total")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("\nMenu:")
            restaurante.listar_menu()
        elif escolha == '2':
            nome_produto = input("Digite o nome do produto que deseja adicionar ao pedido: ")
            for produto in restaurante.menu:
                if produto.nome.lower() == nome_produto.lower():
                    pedido.adicionar_produto(produto)
                    print(f"{produto.nome} adicionado ao pedido.")
                    break
            else:
                print("Produto não encontrado no menu.")
        elif escolha == '3':
            print("\nResumo do Pedido:")
            print(pedido.mostrar_informacoes())
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
