class Funcionario:
    def __init__(self, cod, nome, salario):
        self.cod = cod
        self.nome = nome
        self.__salario = salario  # Salário é um atributo privado
        self.historico_aumentos = []  # Inicializa a lista de histórico de aumentos

    @property
    def salario(self):
        return self.__salario

    def alterar_salario(self, novo_salario):
        if novo_salario < self.__salario:
            raise ValueError("Não é possível reduzir o salário.")
        self.__salario = novo_salario

    def aumentar_salario(self, percentual):
        if percentual < 0:
            raise ValueError("O percentual deve ser positivo.")
        aumento = self.__salario * (percentual / 100)
        novo_salario = self.__salario + aumento
        self.__salario = novo_salario
        # Adiciona ao histórico de aumentos
        self.historico_aumentos.append({
            'percentual': percentual,
            'novo_salario': novo_salario
        })

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Código: {self.cod}")
        print(f"Salário Atual: {self.__salario:.2f}")
        print("Histórico de Aumentos:")
        for aumento in self.historico_aumentos:
            print(f"- Aumento de {aumento['percentual']}%: Novo Salário: {aumento['novo_salario']:.2f}")

# Exemplo de uso da classe
funcionario = Funcionario(1, "João da Silva", 3000)
funcionario.aumentar_salario(10)  # Aumento de 10%
funcionario.aumentar_salario(5)    # Aumento de 5%
funcionario.exibir_informacoes()

# Tentativa de alterar o salário para um valor menor
try:
    funcionario.alterar_salario(2900)  # Isso deve lançar uma exceção
except ValueError as e:
    print(e)

# Alterando o salário para um valor maior
funcionario.alterar_salario(3500)
funcionario.exibir_informacoes()