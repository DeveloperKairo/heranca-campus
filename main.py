from src.SistemaUniversitario import SistemaUniversitario

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

def menu_campus(campus):
    print(f"""
=== Campus {campus.codigo} - {campus.nome} ===
1 - Criar curso
2 - Listar cursos
3 - Entrar em um curso
4 - Editar campus
5 - Excluir campus
0 - Voltar
""")

def menu_curso(curso):
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
            sistema.criar_campus()

        elif opc == "2":
            sistema.listar_campus()

        elif opc == "3":
            campus = sistema.buscar_campus()
            if not campus:
                print("Campus não encontrado.")
                continue

            while True:
                menu_campus(campus)
                op2 = input("Escolha: ")

                if op2 == "1":
                    campus.adicionar_curso()

                elif op2 == "2":
                    campus.listar_cursos()

                elif op2 == "3":
                    curso = campus.buscar_curso()
                    if not curso:
                        print("Curso não encontrado.")
                        continue

                    while True:
                        menu_curso(curso)
                        op3 = input("Escolha: ")

                        if op3 == "1":
                            curso.adicionar_disciplina()
                        elif op3 == "2":
                            curso.imprimir_disciplinas()
                        elif op3 == "3":
                            curso.editar_disciplina()
                        elif op3 == "4":
                            curso.remover_disciplina()
                        elif op3 == "5":
                            curso.adicionar_pessoa()
                        elif op3 == "6":
                            curso.listar_pessoas()
                        elif op3 == "7":
                            curso.detalhes_pessoa()
                        elif op3 == "0":
                            break


                elif op2 == "4":
                    campus.editar_campus()

                elif op2 == "5":
                    sistema.remover_campus()
                    break

                elif op2 == "0":
                    break

        elif opc == "4":
            sistema.editar_campus()

        elif opc == "5":
            sistema.remover_campus()

        elif opc == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

main()
