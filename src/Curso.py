from .Disciplina import Disciplina
from .Aluno import Aluno
from .Professor import Professor

class Curso:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.disciplinas = []
        self.alunos = []
        self.professores = []

    def adicionar_exemplo_disciplina(self):
        disciplina_poo = Disciplina("004", "Programação Orientada a Objetos", 64)
        self.disciplinas.append(disciplina_poo)

    def adicionar_disciplina(self):
        codigo = input("Código da disciplina: ")
        nome = input("Nome da disciplina: ")
        horas = int(input("Carga horária: "))

        disciplina = Disciplina(codigo, nome, horas)
        self.disciplinas.append(disciplina)

        print("Disciplina adicionada:")
        disciplina.imprimir_informacoes()

    def remover_disciplina(self):
        codigo = input("Código da disciplina a remover: ")
        self.disciplinas = [d for d in self.disciplinas if d.codigo != codigo]

    def editar_disciplina(self):
        codigo = input("Código da disciplina a editar: ")
        for d in self.disciplinas:
            if d.codigo == codigo:
                d.nome = input("Novo nome: ") or d.nome
                d.quantidade_horas = int(input("Nova carga horária: "))
                print("Disciplina atualizada.")
                return
        print("Disciplina não encontrada.")

    def imprimir_disciplinas(self):
        if not self.disciplinas:
            print("Nenhuma disciplina cadastrada.")
            return

        print(f"=== Disciplinas do curso {self.nome} ===")
        for d in self.disciplinas:
            d.imprimir_informacoes()

    def informacoes_curso(self):
        print(f"Curso {self.nome} - Código {self.codigo}")

    def adicionar_pessoa(self):
        tipo = input("Cadastrar [A]luno ou [P]rofessor? ").strip().upper()
        identificador = input("Identificador (matrícula ou SIAPE): ")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        nascimento = input("Data de nascimento: ")
        email = input("Email: ")
        
        if tipo == "A":
            periodo = input("Período do aluno: ")
            pessoa = Aluno(identificador, nome, cpf, nascimento, email, self.nome, periodo)
            self.alunos.append(pessoa)
            print("Aluno cadastrado com sucesso!")
        elif tipo == "P":
            departamento = input("Departamento: ")
            titulacao = input("Titulação: ")
            pessoa = Professor(identificador, nome, cpf, nascimento, email, departamento, titulacao)
            self.professores.append(pessoa)
            print("Professor cadastrado com sucesso!")
        else:
            print("Tipo inválido.")

    def listar_pessoas(self):
        print("=== Alunos ===")
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        for aluno in self.alunos:
            print(f"{aluno.identificador} - {aluno.nome}")

        print("=== Professores ===")
        if not self.professores:
            print("Nenhum professor cadastrado.")
        for prof in self.professores:
            print(f"{prof.identificador} - {prof.nome}")

    def detalhes_pessoa(self):
        ident = input("Informe o identificador da pessoa: ")
        for aluno in self.alunos:
            if aluno.identificador == ident:
                aluno.exibir_dados()
                return
        for prof in self.professores:
            if prof.identificador == ident:
                prof.exibir_dados()
                return
        print("Pessoa não encontrada.")


