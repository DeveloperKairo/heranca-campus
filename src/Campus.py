from typing import List, Optional
from .Curso import Curso
from .Endereco import Endereco

class Campus:
    """
    Representa um campus da universidade.
    """
    def __init__(self, codigo: str, nome: str, endereco: Endereco):
        self._codigo = codigo
        self._nome = nome
        self._endereco = endereco
        self._cursos: List[Curso] = []

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
    def endereco(self) -> Endereco:
        return self._endereco

    @property
    def cursos(self) -> List[Curso]:
        return self._cursos

    def criar_exemplo_curso(self) -> None:
        curso_ads = Curso("001", "Análise e Desenvolvimento de Sistemas")
        self.adicionar_curso(curso_ads)
        curso_ads.adicionar_exemplo_disciplina()

    def adicionar_curso(self, curso: Curso) -> None:
        self._cursos.append(curso)
        print("Curso criado com sucesso.")

    def listar_cursos(self) -> None:
        if not self._cursos:
            print("Nenhum curso cadastrado.")
            return
        for c in self._cursos:
            print(f"{c.codigo} - {c.nome}")

    def buscar_curso(self, codigo: str) -> Optional[Curso]:
        for c in self._cursos:
            if c.codigo == codigo:
                return c
        return None

    def remover_curso(self, codigo: str) -> bool:
        """Remove um curso pelo código. Retorna True se removeu, False se não encontrou."""
        for c in self._cursos:
            if c.codigo == codigo:
                self._cursos.remove(c)
                return True
        return False

    def informacoes_campus(self) -> None:
        print(f"""
Campus: {self.nome} ({self.codigo})
Endereço: {self.endereco.logradouro}, {self.endereco.numero}
Bairro: {self.endereco.bairro}
Cidade: {self.endereco.cidade}
""")
