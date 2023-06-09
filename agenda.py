print("Bem-vindo(a) à Agenda do Universitário!")

pergunta = input("Você já está cadastrado(a) em nossa Agenda? ")

if pergunta == "sim" or pergunta == "Sim":
  nome_usuario = input("Digite seu nome de usuário: ")
  senha_usuario = input("Digite a sua senha: ")
  
elif pergunta == "não" or pergunta == "Não":
  email_usuario = input("Ok! Então, para iniciarmos, digite seu email: ")
  senha2_usuario = input("Digite uma senha: ")
  confirmacao_senha = input("Confirme a sua senha: ")
  
  while senha2_usuario != confirmacao_senha:
    print("Está incorreta! Verifique e tente novamente.")
    confirmacao_senha = input("Confirme a senha: ") 

lista_aulas = []

print("Para iniciar a organização da sua agenda, responda às questões abaixo: ")
nome_aluno = input("Digite o seu nome completo: ").title()
nome_universidade = input("Digite o nome da Instituição de Ensino da qual faz parte: ")
nome_curso = input("Digite o nome do seu curso de graduação: ")

print("Tudo pronto. Faça o cadastro das suas aulas!")

continuar = input("Deseja adicionar uma nova aula? ")

while continuar  == "sim" or continuar == "Sim":
  materia = input("Qual o nome da matéria? ")
  horario = input("Qual o horário da aula? ")
  professor = input("Qual o nome do professor responsável por ela? ")
  continuar = input("Deseja adicionar mais alguma aula? ")
  aula = {
    'materia': materia,
    'horario': horario,
    'professor': professor
  }
  lista_aulas.append(aula)
  
  if continuar == "não" or continuar == "Não":
    break

print("\n Suas informações foram salvas!")
print("-------------------------------------")
print("Nome do aluno: {}".format(nome_aluno))
print("Instituição: {}".format(nome_universidade))
print("Curso: {}".format(nome_curso))
print("-------------------------------------\n")
for aula in lista_aulas:
  print("---------------------------")
  print("Matéria:", aula['materia'])
  print("Professor(a):", aula['professor'])
  print("Horário: ", aula['horario'])
  print("---------------------------\n")
