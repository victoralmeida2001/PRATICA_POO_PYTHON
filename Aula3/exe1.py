class Funcionario:
    def __init__(self, nome, cod, __salario_atual):
        self.nome = nome
        self.cod = cod
        self.salario_atual = __salario_atual

    def aumentar_salario(self, percentual, aumento):
        self.salario_atual += (percentual / 100) * self.salario_atual
        self.percentual = percentual
        self.aumento = aumento
        aumento = []
        aumento.append({"Percentual": self.percentual, "Salario": self.salario_atual}) 

    def exibir_informacoes(self):
        print(f'Funcionario: {self.nome}')
        print(f'Cod.: {self.cod}')
        print(f'Salario atual: {self.salario_atual}')
        print(self.aumento)
    



fun1 = Funcionario('Victor', 1, 10000)

fun1.aumentar_salario(10)
fun1.aumentar_salario(5)
fun1.aumentar_salario(8)
fun1.aumentar_salario(50)
fun1.exibir_informacoes()