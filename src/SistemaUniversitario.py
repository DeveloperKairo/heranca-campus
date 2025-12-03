from typing import List, Optional
from .Campus import Campus
from .Endereco import Endereco

class SistemaUniversitario:
    """
    Classe principal que gerencia o sistema universitário.
    """
    def __init__(self):
        self._campus: List[Campus] = []

    @property
    def campus(self) -> List[Campus]:
        return self._campus

    def criar_exemplo(self) -> None:
        endereco_itapaje = Endereco("Rua Francisco José de Oliveira", 596, "Santa Rita", "Itapajé")
        campus_itapaje = Campus("008", "Jardins de Anita", endereco_itapaje)

        self.adicionar_campus(campus_itapaje)
        campus_itapaje.criar_exemplo_curso()

    def adicionar_campus(self, campus: Campus) -> None:
        self._campus.append(campus)
        print("Campus criado com sucesso.")
        campus.informacoes_campus()

    def listar_campus(self) -> None:
        if not self._campus:
            print("Nenhum campus cadastrado.")
            return
        
        for c in self._campus:
            print(f"{c.codigo} - {c.nome}")

    def buscar_campus(self, codigo: str) -> Optional[Campus]:
        for c in self._campus:
            if c.codigo == codigo:
                return c
        return None

    def remover_campus(self, codigo: str) -> bool:
        """Remove um campus pelo código. Retorna True se removeu, False se não encontrou."""
        for c in self._campus:
            if c.codigo == codigo:
                self._campus.remove(c)
                return True
        return False
