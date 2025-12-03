from src.SistemaUniversitario import SistemaUniversitario
from src.Campus import Campus
from src.Curso import Curso
from src.Disciplina import Disciplina
from src.Endereco import Endereco
from src.Aluno import Aluno
from src.Professor import Professor

sistema = SistemaUniversitario()
sistema.criar_exemplo()

def menu_principal():
    print("""
=== SISTEMA UNIVERSITÁRIO ===
1 - Criar campus
2 - Listar campus
3 - Entrar em um campus
4 - Editar campus
5 - Excluir campus
0 - Sair
""")

def menu_campus(campus: Campus):
    print(f"""
=== Campus {campus.codigo} - {campus.nome} ===
1 - Criar curso
2 - Listar cursos
3 - Entrar em um curso
4 - Editar campus
5 - Excluir campus
0 - Voltar
""")

def menu_curso(curso: Curso):
    print(f"""
=== Curso {curso.codigo} - {curso.nome} ===
1 - Criar disciplina
2 - Listar disciplinas
3 - Editar disciplina
4 - Excluir disciplina
5 - Cadastrar pessoa (aluno/professor)
6 - Listar pessoas deste curso
7 - Detalhes de uma pessoa
0 - Voltar
""")


def main():
    while True:
        menu_principal()
        opc = input("Digite a opção desejada: ")

        if opc == "1":
            codigo = input("Código do campus: ")
            nome = input("Nome do campus: ")
            logradouro = input("Logradouro: ")
            try:
                numero = int(input("Número: "))
            except ValueError:
                print("Número inválido.")
                continue
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")

            endereco = Endereco(logradouro, numero, bairro, cidade)
            novo_campus = Campus(codigo, nome, endereco)
            sistema.adicionar_campus(novo_campus)

        elif opc == "2":
            sistema.listar_campus()

        elif opc == "3":
            codigo = input("Código do campus: ")
            campus = sistema.buscar_campus(codigo)
            if not campus:
                print("Campus não encontrado.")
                continue

            while True:
                menu_campus(campus)
                op2 = input("Escolha: ")

                if op2 == "1":
                    codigo_curso = input("Código do curso: ")
                    nome_curso = input("Nome do curso: ")
                    curso = Curso(codigo_curso, nome_curso)
                    campus.adicionar_curso(curso)

                elif op2 == "2":
                    campus.listar_cursos()

                elif op2 == "3":
                    codigo_curso = input("Código do curso: ")
                    curso = campus.buscar_curso(codigo_curso)
                    if not curso:
                        print("Curso não encontrado.")
                        continue

                    while True:
                        menu_curso(curso)
                        op3 = input("Escolha: ")

                        if op3 == "1":
                            codigo_disc = input("Código da disciplina: ")
                            nome_disc = input("Nome da disciplina: ")
                            try:
                                horas = int(input("Carga horária: "))
                                disciplina = Disciplina(codigo_disc, nome_disc, horas)
                                curso.adicionar_disciplina(disciplina)
                            except ValueError:
                                print("Carga horária inválida.")

                        elif op3 == "2":
                            curso.imprimir_disciplinas()

                        elif op3 == "3":
                            codigo_disc = input("Código da disciplina a editar: ")
                            disciplina = curso.buscar_disciplina(codigo_disc)
                            if disciplina:
                                novo_nome = input(f"Novo nome ({disciplina.nome}): ")
                                if novo_nome:
                                    disciplina.nome = novo_nome
                                try:
                                    nova_carga_str = input(f"Nova carga horária ({disciplina.quantidade_horas}): ")
                                    if nova_carga_str:
                                        disciplina.quantidade_horas = int(nova_carga_str)
                                    print("Disciplina atualizada.")
                                except ValueError:
                                    print("Carga horária inválida.")
                            else:
                                print("Disciplina não encontrada.")

                        elif op3 == "4":
                            codigo_disc = input("Código da disciplina a remover: ")
                            if curso.remover_disciplina(codigo_disc):
                                print("Disciplina removida.")
                            else:
                                print("Disciplina não encontrada.")

                        elif op3 == "5":
                            tipo = input("Cadastrar [A]luno ou [P]rofessor? ").strip().upper()
                            identificador = input("Identificador (matrícula ou SIAPE): ")
                            nome_pessoa = input("Nome: ")
                            cpf = input("CPF: ")
                            nascimento = input("Data de nascimento: ")
                            email = input("Email: ")
                            
                            if tipo == "A":
                                periodo = input("Período do aluno: ")
                                aluno = Aluno(identificador, nome_pessoa, cpf, nascimento, email, curso.nome, periodo)
                                curso.adicionar_pessoa(aluno)
                            elif tipo == "P":
                                departamento = input("Departamento: ")
                                titulacao = input("Titulação: ")
                                professor = Professor(identificador, nome_pessoa, cpf, nascimento, email, departamento, titulacao)
                                curso.adicionar_pessoa(professor)
                            else:
                                print("Tipo inválido.")

                        elif op3 == "6":
                            curso.listar_pessoas()

                        elif op3 == "7":
                            ident = input("Informe o identificador da pessoa: ")
                            pessoa = curso.buscar_pessoa(ident)
                            if pessoa:
                                pessoa.exibir_dados()
                            else:
                                print("Pessoa não encontrada.")

                        elif op3 == "0":
                            break

                elif op2 == "4":
                    print(f"Editando campus {campus.nome}")
                    novo_nome = input("Novo nome: ")
                    if novo_nome:
                        campus.nome = novo_nome
                        print("Nome atualizado.")

                elif op2 == "5":
                    # Remover campus atual e sair do menu
                    if sistema.remover_campus(campus.codigo):
                        print("Campus removido.")
                        break
                    else:
                        print("Erro ao remover campus.")

                elif op2 == "0":
                    break

        elif opc == "4":
            codigo = input("Código do campus a editar: ")
            campus = sistema.buscar_campus(codigo)
            if campus:
                novo_nome = input(f"Novo nome ({campus.nome}): ")
                if novo_nome:
                    campus.nome = novo_nome
                    print("Campus atualizado.")
            else:
                print("Campus não encontrado.")

        elif opc == "5":
            codigo = input("Código do campus a remover: ")
            if sistema.remover_campus(codigo):
                print("Campus removido.")
            else:
                print("Campus não encontrado.")

        elif opc == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
