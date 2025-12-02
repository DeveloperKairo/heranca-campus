class Disciplina:
  def __init__ (self, codigo, nome, quantidade_horas):
    self.codigo = codigo
    self.nome = nome
    self.quantidade_horas = quantidade_horas

  def imprimir_informacoes(self):
    print(f"""{self.nome} --- {self.codigo}
Carga Horária: {self.quantidade_horas}""")

  