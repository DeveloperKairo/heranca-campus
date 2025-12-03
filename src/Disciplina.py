class Disciplina:
    """
    Representa uma disciplina de um curso.
    """
    def __init__(self, codigo: str, nome: str, quantidade_horas: int):
        self._codigo = codigo
        self._nome = nome
        self._quantidade_horas = quantidade_horas

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
    def quantidade_horas(self) -> int:
        return self._quantidade_horas

    @quantidade_horas.setter
    def quantidade_horas(self, nova_carga: int) -> None:
        self._quantidade_horas = nova_carga

    def imprimir_informacoes(self) -> None:
        print(f"""{self.nome} --- {self.codigo}
Carga Horária: {self.quantidade_horas}""")