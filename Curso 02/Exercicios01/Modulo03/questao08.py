class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"

    def __len__(self):
        return self.paginas

# Programa principal
livro1 = Livro("Dom Casmurro", "Machado de Assis", 256)

print(livro1)            # Usa o __str__()
print(len(livro1))       # Usa o __len__()
