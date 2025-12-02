from .Curso import Curso

class Campus:
    def __init__(self, codigo, nome, endereco):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.cursos = []

    def criar_exemplo_curso(self):
        curso_ads = Curso("001", "Análise e Desenvolvimento dee Sistemas")
        self.cursos.append(curso_ads)

        curso_ads.adicionar_exemplo_disciplina()

    def adicionar_curso(self):
        codigo_curso = input("Código do curso: ")
        nome_curso = input("Nome do curso: ")

        curso = Curso(codigo_curso, nome_curso)
        self.cursos.append(curso)

        print("Curso criado:")
        curso.informacoes_curso()

    def listar_cursos(self):
        if not self.cursos:
            print("Nenhum curso cadastrado.")
            return
        for c in self.cursos:
            print(f"{c.codigo} - {c.nome}")

    def buscar_curso(self):
        codigo = input("Código do curso: ")
        for c in self.cursos:
            if c.codigo == codigo:
                return c
        return None

    def remover_curso(self):
        codigo = input("Código do curso: ")
        self.cursos = [c for c in self.cursos if c.codigo != codigo]

    def editar_campus(self):
        print(f"Editando campus {self.nome}")
        self.nome = input("Novo nome: ") or self.nome

    def informacoes_campus(self):
        print(f"""
Campus: {self.nome} ({self.codigo})
Endereço: {self.endereco.logradouro}, {self.endereco.numero}
Bairro: {self.endereco.bairro}
Cidade: {self.endereco.cidade}
""")
