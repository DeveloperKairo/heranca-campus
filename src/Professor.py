from .Pessoa import Pessoa

class Professor(Pessoa):
    """
    Representa um professor da universidade.
    """
    def __init__(
        self,
        identificador: str,          
        nome: str,
        cpf: str,
        data_de_nascimento: str,
        email: str,
        departamento: str,
        titulacao: str
    ):
        super().__init__(identificador, nome, cpf, data_de_nascimento, email)
        self._departamento = departamento
        self._titulacao = titulacao
    
    @property
    def departamento(self) -> str:
        return self._departamento

    @property
    def titulacao(self) -> str:
        return self._titulacao

    def exibir_dados(self) -> None:
        print("=== Dados do Professor ===")
        super().exibir_dados()
        print(f"Departamento: {self.departamento}")
        print(f"Titulação: {self.titulacao}")