class Estudante:
    def __init__ (self, nome:str, nota1:float, nota2:float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    
    def media(self):
        return (self.nota1 + self.nota2)/2
    
    def situacao(self):
        if self.media() >= 7.0:
            print(f'Média igual a {self.media()}, desse modo {self.nome} está aprovado(a)')
        else:
            print(f'Média igual a {self.media()},logo o(a) aluno(a) {self.nome} está reprovado(a)')


aluno1 = Estudante('Victor', 7.5, 8.5)
aluno2 = Estudante('Thaise', 5.5, 6.5)

print(aluno1.situacao())
print(aluno2.situacao())
