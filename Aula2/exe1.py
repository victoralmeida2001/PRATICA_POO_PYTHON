class Livro:
    def __init__ (self, titulo:str, autor:str):
        self.titulo = titulo
        self.autor = autor
    def exibir_informacoes(self):
        print(f'O livro {self.titulo} foi escrito por {self.autor}')

livro1 = Livro('Dom Casmurro', 'Machado de Assis')
livro2 = Livro('O senhor dos aneis', 'J.K. Rownling')

livro1.exibir_informacoes()
livro2.exibir_informacoes()