from typing import List, Optional, Union
from .Disciplina import Disciplina
from .Pessoa import Pessoa
from .Aluno import Aluno
from .Professor import Professor

class Curso:
    """
    Representa um curso da universidade.
    """
    def __init__(self, codigo: str, nome: str):
        self._codigo = codigo
        self._nome = nome
        self._disciplinas: List[Disciplina] = []
        self._alunos: List[Aluno] = []
        self._professores: List[Professor] = []

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome

    @property
    def disciplinas(self) -> List[Disciplina]:
        return self._disciplinas

    @property
    def alunos(self) -> List[Aluno]:
        return self._alunos

    @property
    def professores(self) -> List[Professor]:
        return self._professores

    def adicionar_exemplo_disciplina(self) -> None:
        disciplina_poo = Disciplina("004", "Programação Orientada a Objetos", 64)
        self.adicionar_disciplina(disciplina_poo)

    def adicionar_disciplina(self, disciplina: Disciplina) -> None:
        self._disciplinas.append(disciplina)
        print("Disciplina adicionada com sucesso.")

    def remover_disciplina(self, codigo: str) -> bool:
        """Remove uma disciplina pelo código. Retorna True se removeu, False se não encontrou."""
        for d in self._disciplinas:
            if d.codigo == codigo:
                self._disciplinas.remove(d)
                return True
        return False

    def buscar_disciplina(self, codigo: str) -> Optional[Disciplina]:
        for d in self._disciplinas:
            if d.codigo == codigo:
                return d
        return None

    def imprimir_disciplinas(self) -> None:
        if not self._disciplinas:
            print("Nenhuma disciplina cadastrada.")
            return

        print(f"=== Disciplinas do curso {self.nome} ===")
        for d in self._disciplinas:
            d.imprimir_informacoes()

    def informacoes_curso(self) -> None:
        print(f"Curso {self.nome} - Código {self.codigo}")

    def adicionar_pessoa(self, pessoa: Union[Aluno, Professor]) -> None:
        if isinstance(pessoa, Aluno):
            self._alunos.append(pessoa)
            print("Aluno cadastrado com sucesso!")
        elif isinstance(pessoa, Professor):
            self._professores.append(pessoa)
            print("Professor cadastrado com sucesso!")
        else:
            print("Tipo de pessoa inválido para este curso.")

    def listar_pessoas(self) -> None:
        print("=== Alunos ===")
        if not self._alunos:
            print("Nenhum aluno cadastrado.")
        for aluno in self._alunos:
            print(f"{aluno.identificador} - {aluno.nome}")

        print("=== Professores ===")
        if not self._professores:
            print("Nenhum professor cadastrado.")
        for prof in self._professores:
            print(f"{prof.identificador} - {prof.nome}")

    def buscar_pessoa(self, identificador: str) -> Optional[Union[Aluno, Professor]]:
        for aluno in self._alunos:
            if aluno.identificador == identificador:
                return aluno
        for prof in self._professores:
            if prof.identificador == identificador:
                return prof
        return None
