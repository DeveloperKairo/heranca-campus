from .Pessoa import Pessoa

class Aluno(Pessoa):
    """
    Representa um aluno da universidade.
    """
    def __init__(
        self, 
        identificador: str, 
        nome: str, 
        cpf: str, 
        data_de_nascimento: str, 
        email: str, 
        curso: str, 
        periodo: str
    ):
        super().__init__(identificador, nome, cpf, data_de_nascimento, email)
        self._curso = curso
        self._periodo = periodo

    @property
    def curso(self) -> str:
        return self._curso

    @property
    def periodo(self) -> str:
        return self._periodo

    def exibir_dados(self) -> None:
        print("=== Dados do Aluno ===")
        super().exibir_dados()  
        print(f"Curso: {self.curso}")
        print(f"Período: {self.periodo}")