class Endereco:
    """
    Representa um endereço físico.
    """
    def __init__(self, logradouro: str, numero: int, bairro: str, cidade: str):
        self._logradouro = logradouro
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade

    @property
    def logradouro(self) -> str:
        return self._logradouro

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def bairro(self) -> str:
        return self._bairro

    @property
    def cidade(self) -> str:
        return self._cidade