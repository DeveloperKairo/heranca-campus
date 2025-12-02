from .Pessoa import Pessoa

class Aluno(Pessoa):
  def __init__(
    self, 
    identificador, 
    nome, 
    cpf, 
    data_de_nascimento, 
    email, 
    curso, 
    periodo
  ):
    super().__init__(identificador, nome, cpf, data_de_nascimento, email)
    self.curso = curso
    self.periodo = periodo

  def exibir_dados(self):
    print("=== Dados do Aluno ===")
    super().exibir_dados()  
    print(f"Curso: {self.curso}")
    print(f"Período: {self.periodo}")