from .Campus import Campus
from .Endereco import Endereco

class SistemaUniversitario:
    def __init__(self):
        self.campus = []

    def criar_exemplo(self):
        endereco_itapaje = Endereco("Rua Francisco José de Oliveira", 596, "Santa Rita", "Itapajé")
        campus_itapaje = Campus("008", "Jardins de Anita", endereco_itapaje)

        self.campus.append(campus_itapaje)

        campus_itapaje.criar_exemplo_curso()

    def criar_campus(self):
        codigo = input("Código do campus: ")
        nome = input("Nome do campus: ")
        logradouro = input("Logradouro: ")
        numero = int(input("Número: "))
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")

        endereco = Endereco(logradouro, numero, bairro, cidade)
        novo_campus = Campus(codigo, nome, endereco)

        self.campus.append(novo_campus)

        print("Campus criado:")
        novo_campus.informacoes_campus()

    def listar_campus(self):
        if not self.campus:
            print("Nenhum campus cadastrado.")
            return
        
        for c in self.campus:
            print(f"{c.codigo} - {c.nome}")

    def buscar_campus(self):
        codigo = input("Código do campus: ")
        for c in self.campus:
            if c.codigo == codigo:
                return c
        return None

    def remover_campus(self):
        codigo = input("Código do campus a remover: ")
        self.campus = [c for c in self.campus if c.codigo != codigo]
        print("Campus removido.")

    def editar_campus(self):
        campus = self.buscar_campus()
        if not campus:
            print("Campus não encontrado.")
            return
        campus.editar_campus()
