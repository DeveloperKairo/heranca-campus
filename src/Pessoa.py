class Pessoa:
  def __init__(
    self, 
    identificador, 
    nome, 
    cpf, 
    data_de_nascimento, 
    email
  ):
    self.identificador = identificador
    self.nome = nome
    self.cpf = cpf
    self.data_de_nascimento = data_de_nascimento
    self.email = email

  def exibir_dados(self):
    print(f"Nome: {self.nome}")
    print(f"Identificador: {self.identificador}")
    print(f"CPF: {self.cpf}")
    print(f"Nascimento: {self.data_de_nascimento}")
    print(f"E-mail: {self.email}")