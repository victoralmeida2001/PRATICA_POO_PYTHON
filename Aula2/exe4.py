class Produto:
    def __init__(self, nome:str, preco:float, estoque:int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade
        print(f'Adicionado {quantidade}, atualmente estoque igual a {self.estoque}')

    def remover_estoque(self, quantidade):
        self.estoque -= quantidade
        print(f'Removido {quantidade}, atualmente estoque igual a {self.estoque}')

    def exibir_produto(self):
       print(f'O {self.nome} custa R$ {self.preco:.2f} há {self.estoque} no estoque')



medicamento1 = Produto('dipirona', 1.5, 50)
medicamento2 = Produto('paracetamol', 0.45, 60)

medicamento1.exibir_produto()

medicamento1.remover_estoque(40)

medicamento1.exibir_produto()

medicamento1.adicionar_estoque(60)

medicamento1.exibir_produto()