class Biblioteca:
    def __init__(self):
        self.banco_de_livros = []

    def adicionar_livro(self, titulo, autor, ano):
        livro = {"titulo": titulo, "autor": autor, "ano": ano}
        self.banco_de_livros.append(livro)
        print(f'Livro "{titulo}" adicionado com sucesso!')

    def listar_livros(self):
        if self.banco_de_livros:
            print("Lista de livros na biblioteca:")
            for idx, livro in enumerate(self.banco_de_livros, start=1):
                print(f"{idx}. Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
        else:
            print("Nenhum livro encontrado na biblioteca.")

    def buscar_livro_por_titulo(self, titulo):
        resultados = [livro for livro in self.banco_de_livros if titulo.lower() in livro['titulo'].lower()]
        if resultados:
            print(f"Livros encontrados com o título '{titulo}':")
            for idx, livro in enumerate(resultados, start=1):
                print(f"{idx}. Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
        else:
            print(f"Nenhum livro encontrado com o título '{titulo}'.")

biblioteca = Biblioteca()
biblioteca.adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
biblioteca.adicionar_livro("1984", "George Orwell", 1949)
biblioteca.listar_livros()
biblioteca.buscar_livro_por_titulo("1984")
