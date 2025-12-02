from .Pessoa import Pessoa

class Professor(Pessoa):
  def __init__(
    self,
    identificador,          
    nome,
    cpf,
    data_de_nascimento,
    email,
    departamento,
    titulacao
  ):
    super().__init__(identificador, nome, cpf, data_de_nascimento, email)
    self.departamento = departamento
    self.titulacao = titulacao
    
  def exibir_dados(self):
    print("=== Dados do Professor ===")
    super().exibir_dados()
    print(f"Departamento: {self.departamento}")
    print(f"Titulação: {self.titulacao}")