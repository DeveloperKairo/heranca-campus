class Pessoa:
    """
    Classe base que representa uma pessoa no sistema.
    """
    def __init__(
        self, 
        identificador: str, 
        nome: str, 
        cpf: str, 
        data_de_nascimento: str, 
        email: str
    ):
        self._identificador = identificador
        self._nome = nome
        self._cpf = cpf
        self._data_de_nascimento = data_de_nascimento
        self._email = email

    @property
    def identificador(self) -> str:
        return self._identificador

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def data_de_nascimento(self) -> str:
        return self._data_de_nascimento

    @property
    def email(self) -> str:
        return self._email

    def exibir_dados(self) -> None:
        """Exibe os dados básicos da pessoa."""
        print(f"Nome: {self.nome}")
        print(f"Identificador: {self.identificador}")
        print(f"CPF: {self.cpf}")
        print(f"Nascimento: {self.data_de_nascimento}")
        print(f"E-mail: {self.email}")