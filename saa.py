from classes import *
import time

# 2º Ano B Vespertino Informática
# Alunos:
# André Luís Bento Ferreira
# Celso Hector Silva Sales
# Luiz Felipe Macedo Alencar de Menezes
# Judson Gabriel Ferreira dos Santos

# Atençãaaaaaaao!!!!!!!!!!!!!!!!!! ----> Confirmar usuario (Arrumar) / fazer a interface para cada carinha la

usuarios = []


# Home
def home():
    option = input("\n1- Login | 2- Registrar | 0- Sair: ")
    if option == "1":
        acesso()
    elif option == "2":
        registrar()
    elif option == "0":
        print("Saindo... Até a próxima!")
        exit()
    else:
        print("Escolha uma opção válida.")
        home()


# Função de verificação do email
def verificacaoEMAIL(email):
    for user in usuarios:
        if user["objeto"].getEmail() == email:
            return True
    return False


# Função de verificação do telefone
def verificacaoTELEFONE(telefone):
    for user in usuarios:
        if user["objeto"].getTelefone() == telefone:
            return True
    return False


# Função de verificação do cpf
def verificacaoCPF(cpf):
    for user in usuarios:
        if user["objeto"].getCpf() == cpf:
            return True
    return False


# Função de verificação da matrícula
def verificar_matricula(matricula):
    for user in usuarios:
        if user["tipo"] == "1" and user["objeto"].getmatricula() == matricula:
            return True
    return False


# Escolha de Curso
def escolher_curso():
    print("\nEscolha seu curso técnico integrado:")
    print("1- Informática")
    print("2- Química")
    print("3- Eletrotécnica")
    print("4- Edificações")
    opcao = input("Escolha de 1-4: ")

    if opcao == "1":
        return "Informática"
    elif opcao == "2":
        return "Química"
    elif opcao == "3":
        return "Eletrotécnica"
    elif opcao == "4":
        return "Edificações"
    else:
        print("Insira uma opção válida")
        return escolher_curso()


# Registro
def registrar():
    print("\nVocê é: 1- Aluno | 2- Professor | 3- Administrador | 0- Voltar")
    tipo = input("Escolha uma opção: ")

    if tipo == "0":
        home()

    if tipo != "1" and tipo != "2" and tipo != "3":
        print("Valor inválido. Escolha de 1-3.")
        registrar()

    # Nome
    nome = input("Digite seu nome: ")

    # Idade
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade <= 14 or idade >= 75:
                print("\nInsira um número válido (Maior que 14 e menor que 75)\n")

            else:
                break

        except:
            print("Insira um número!")

        # CPF
    while True:
        try:
            cpf = int(input("Digite seu CPF: "))
            if verificacaoCPF(cpf):
                print("\nCPF já registrado. Tente novamente.\n")
                continue

            else:
                break

        except:
            print("\nInsira um valor válido.\n")

    # Email
    while True:
        email = input("Digite seu email: ")
        if verificacaoEMAIL(email):
            print("\nEmail já registrado. Tente novamente.\n")
            continue

        else:
            break

    # Telefone
    while True:
        telefone = input("Digite seu telefone: ")
        if verificacaoTELEFONE(telefone):
            print("\nTelefone já registrado. Tente novamente.\n")
            continue

        else:
            break

        # PCD
    while True:
        try:
            pcdAsk = int(input("\nVocê é uma Pessoa com Deficiência?\n1- Sim\n2- Não\nR: "))
            if pcdAsk == 1:
                qualpcd = input("\nQual sua deficiência?\nSiga o exemplo: 'Possuo deficiência <deficiência>'\nR: ")
                pcd = qualpcd.split("Possuo ")
                pcd = pcd[1]
                pcd = "Possui " + pcd
                break


            elif pcdAsk == 2:
                break

            else:
                print("Opção incorreta!")

        except:
            print("insira uma Opcção!")

    # Usuário
    usuario = input("Digite seu usuário: ")
    for user in usuarios:
        if user["usuario"] == usuario:
            print("O usuário informado já existe. Tente novamente.")

    # Senha
    while True:
        senha = input("Digite sua senha: ")
        if len(senha) < 6:
            print("A senha deve conter no mínimo 6 caracteres. Tente novamente.")

        else:
            break

    # Confirmando senha
    while True:
        senha1 = input("Confirme sua senha: ")
        time.sleep(0.5)
        if senha != senha1:
            print("As senhas não coincidem. Tente novamente.")

        else:
            break

        # Aluno
    if tipo == "1":
        while True:
            try:
                # Matricula
                matricula = int(input("Digite sua matrícula: "))
                if verificar_matricula(matricula):
                    print("Matrícula já registrada. Tente novamente.")
                    continue

                else:
                    break

            except:
                print("Insira um número!")

        curso = escolher_curso()
        novo_usuario = Aluno(nome, idade, cpf, email, telefone, matricula, curso)

    # Professor
    elif tipo == "2":
        curso = escolher_curso()  # definindo o curso
        novo_usuario = Prof(nome, idade, cpf, email, telefone, curso)

    # Adiministrador
    elif tipo == "3":
        novo_usuario = Adm(nome, idade, cpf, email, telefone)

    else:
        print("Opção inválida. Tente novamente.")
        registrar()

    usuarios.append({"usuario": usuario, "senha": senha, "tipo": tipo, "objeto": novo_usuario})
    print("Registro realizado com sucesso.\n")
    time.sleep(0.5)
    print("Redirecionando para o login...\n")
    time.sleep(1)
    acesso()


# Acesso
def acesso():
    time.sleep(0.5)
    print("(digite 0 se quiser retornar ao menu)")
    time.sleep(0.5)
    usuario = input("Digite seu usuário: ")
    if usuario == "0":
        home()
        return
    senha = input("Digite sua senha: ")

    dados_usuario = None  # definindo os dados do usuario no login // felipe
    for user in usuarios:
        if user["usuario"] == usuario and user["senha"] == senha:
            dados_usuario = user
            break

    if dados_usuario:
        tipo_usuario = "Aluno" if dados_usuario["tipo"] == "1" else "Professor" if dados_usuario[
                                                                                       "tipo"] == "2" else "Administrador"
        nome_pessoa = dados_usuario["objeto"].getNome()
        print("Login realizado!\n")
        print(f"Olá, {tipo_usuario} {nome_pessoa} ")
        time.sleep(0.5)
        menu = int(input("1- Marcar atendimento\n2- Consultar atendimentos: \nR: "))
        if menu == 1:
            print("fazer o processo da classe atendimento... cada atributo")

    else:
        print("\nUsuário ou senha incorretos.")
        acesso()


# Saída
def saida():
    print("\nDigite 0 para sair ou 1 para voltar ao menu principal.")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        home()
    elif escolha == "0":
        print("Saindo... Até a próxima!")
        exit()
    else:
        print("Escolha uma opção válida.")
        saida()


print("Bem-vindo ao SAA - Sistema de Atendimento ao Aluno\nIFRO Campus Calama - Técnico Integrado")
home()