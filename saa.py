from classes import *
import time

# 2º Ano B Vespertino Informática
# Alunos:
# André Luís Bento Ferreira
# Celso Hector Silva Sales
# Luiz Felipe Macedo Alencar de Menezes
# Judson Gabriel de Souza Leticia Junior

usuarios = []  # .txt aposentado, agr eh lista // celso
dias = []  # lista de dias de atendimento


def verificacaoDIA(data):  # função para verificar se pro dia digitado já existe um atendimento // felipe w/ celso
    for datas in dias:
        if datas == data:
            return True
    return False


def marcarAtendimento(aluno, professor):  # vai ter q receber o professor e o aluno como parametro aqui
    if aluno.getcurso() != professor.getcurso():
        curso = input("Qual o curso que vai estar relacionado ao atendimento marcado?")
    else:
        curso = aluno.getcurso()

    materia = professor.getmateria()
    print(f"{materia}")

    sair = False
    while True:
        if sair == True:
            break
        try:
            atendimentomarcar = int(input("Você quer marcar um atendimento?\n 1 - Sim \n 0 - Não\n R: "))

            if atendimentomarcar == 0:
                print("Saindo...")
                sair = True
                break

            elif atendimentomarcar == 1:
                dia, mes, ano = input("Quer marcar seu atendimento para qual dia? ").split("/")
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                dia1 = date(ano, mes, dia)
                data = f"{dia}/{mes}/{ano}"
                print(dia1, data)
                var = calendar.day_name[dia1.weekday()]

                if verificacaoDIA(data):
                    print("Dia já cadastrado")
                    print("Veja os dias já cadastrados")
                    for datas in dias:
                        print(f"================= {datas} =================")




                else:
                    dias.append(data)
                    if var == "Monday":
                        print(f"Nova data marcada para: Segunda-Feira, {data}")
                        print(dias)

                    elif var == "Tuesday":
                        print(f"Nova data marcada para: Segunda-Feira, {data}")
                        print(dias)

                    elif var == "Wednesday":
                        print(f"Nova data marcada para: Segunda-Feira, {data}")
                        print(dias)

                    elif var == "Thursday":
                        print(f"Nova data marcada para: Segunda-Feira, {data}")
                        print(dias)

                    elif var == "Friday":
                        print(f"Nova data marcada para: Segunda-Feira, {data}")
                        print(dias)

        except:
            print("Insira um valor válido.")

    while True:
        try:
            horario = int(input(f"Escolha o horário desejado (9h-12h / 14h-19h) - escreva apenas o número: "))
            if 9 <= horario <= 12:
                print(f"Horário marcado para às {horario}h.")
                break
            elif 14 <= horario <= 19:
                print(f"Horário marcado para às {horario}h.")
                break

            elif horario == 13:
                print("Horário de almoço.\n")
                continue

            else:
                print("Horário inválido.\n")
                continue


        except:
            print("Insira números!\n")

    atendimento = Atendimento(curso, materia, data, horario)


def verificacaoEMAIL(email):  # função de verificação do email // felipe
    for user in usuarios:
        if user["objeto"].getEmail() == email:
            return True
    return False


def verificacaoTELEFONE(telefone):  # função de verificação do telefone // celso
    for user in usuarios:
        if user["objeto"].getTelefone() == telefone:
            return True
    return False


def verificacaoCPF(cpf):  # função de verificação do cpf // felipe
    for user in usuarios:
        if user["objeto"].getCpf() == cpf:
            return True
    return False


def verificar_matricula(matricula):  # msm coisa do cpf // felipe
    for user in usuarios:
        if user["tipo"] == "1" and user["objeto"].getmatricula() == matricula:
            return True
    return False


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


def registrar():
    print("\nVocê é: 1- Aluno | 2- Professor | 3- Administrador | 0- Voltar")
    tipo = input("Escolha uma opção: ")

    if tipo == "0":
        home()

    if tipo != "1" and tipo != "2" and tipo != "3":
        print("Valor inválido. Escolha de 1-3.")
        registrar()

    nome = input("Digite seu nome: ")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade <= 14 or idade >= 75:
                print("\nInsira um número válido (Maior que 14 e menor que 75)\n")

            else:
                break

        except:
            print("Insira um número!")

    while True:  # verificação da cpf
        try:
            cpf = int(input("Digite seu CPF: "))
            if verificacaoCPF(cpf):
                print("\nCPF já registrado. Tente novamente.\n")
                continue

            else:
                break

        except:
            print("\nInsira um valor válido.\n")

    while True:  # verificação de email
        try:
            email = input("Digite seu email: ")
            if verificacaoEMAIL(email):
                print("\nEmail já registrado. Tente novamente.\n")
                continue

            else:
                break

        except:
            print("\nInsira um email válido.\n")

    while True:  # verificação de número
        try:
            telefone = input("Digite seu telefone: ")
            if verificacaoTELEFONE(telefone):
                print("\nTelefone já registrado. Tente novamente.\n")
                continue

            else:
                break

        except:
            print("\nInsira um telefone válido.\n")

    usuario = input("Digite seu usuário: ")
    while True:
        senha = input("Digite sua senha: ")
        if len(senha) < 6:
            print("A senha deve conter no mínimo 6 caracteres. Tente novamente.")
            continue

        else:
            break

    while True:
        senha1 = input("Confirme sua senha: ")
        time.sleep(0.5)
        if senha != senha1:  # verificação e requisitos mínimos de senha
            print("As senhas não coincidem. Tente novamente.")
            continue

        else:
            for user in usuarios:  # verificação do usuário
                if user["usuario"] == usuario:
                    print("O usuário informado já existe. Tente novamente.")
                    registrar()

        if tipo == "1":

            while True:
                try:
                    matricula = int(input("Digite sua matrícula: "))  # definindo matricula
                    if verificar_matricula(matricula):
                        print("Matrícula já registrada. Tente novamente.")
                        continue

                    else:
                        break

                except:
                    print("Insira um número!")

            curso = escolher_curso()  # definindo o curso
            novo_usuario = Aluno(nome, idade, cpf, email, telefone, matricula, curso)
            pcd_y_or_n = input("Você é uma Pessoa com Deficiência?").upper()
            if pcd_y_or_n == "SIM":
                qualpcd = input("Qual sua deficiência?\nSiga o exemplo: 'possuo deficiência <deficiência>'\nR:")
                pcd = qualpcd.split("possuo ")
                pcd = pcd[1]
                pcd = "possui " + pcd
                novo_usuario.definindoPcd(pcd)

        elif tipo == "2":
            curso = escolher_curso()  # definindo o curso
            novo_usuario = Prof(nome, idade, cpf, email, telefone, curso)
            pcd_y_or_n = input("Você é uma Pessoa com Deficiência?").upper
            if pcd_y_or_n == "SIM":
                qualpcd = input("Qual sua deficiência?\nSiga o exemplo: 'possuo deficiência <deficiência>'\nR:")
                pcd = qualpcd.split("possuo ")
                pcd = pcd[1]
                pcd = "possui " + pcd
                novo_usuario.definindoPcd(pcd)


        elif tipo == "3":
            novo_usuario = Adm(nome, idade, cpf, email, telefone)
            pcd_y_or_n = input("Você é uma Pessoa com Deficiência?").upper
            if pcd_y_or_n == "SIM":
                qualpcd = input("Qual sua deficiência?\nSiga o exemplo: 'possuo deficiência <deficiência>'\nR:")
                pcd = qualpcd.split("possuo ")
                pcd = pcd[1]
                pcd = "possui " + pcd
                novo_usuario.definindoPcd(pcd)

        else:
            print("Opção inválida. Tente novamente.")
            registrar()
            return

        usuarios.append({"usuario": usuario, "senha": senha, "tipo": tipo, "objeto": novo_usuario})
        print("Registro realizado com sucesso.\n")
        time.sleep(0.5)
        print("Redirecionando para o login...\n")
        time.sleep(1)
        acesso()


def acesso():
    usuario = input("Digite seu usuário (digite 0 se quiser retornar ao menu): ")
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
        print(usuarios)
        menu = input(f"{nome_pessoa}, o que gostaria de fazer? 1- Realizar atendimento / 2- Consultar atendimentos: ")
        if menu == 1:
            print("fazer o processo da classe atendimento... cada atributo")


    else:
        print("\nUsuário ou senha incorretos.")
        acesso()


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


print("Bem-vindo ao SAA - Sistema de Atendimento ao Aluno\nIFRO Campus Calama - Técnico Integrado")
home()
