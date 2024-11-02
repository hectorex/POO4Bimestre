class PessoaIFRO:   #mãe
    def __init__(self, nome: str, idade: int, cpf: int, email: str):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__email = email
    
    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def setIdade(self, idade):
        if idade > 10:
            self.__idade = idade

    def getCpf(self):
        return self.__cpf
    
    def getEmail(self):
        return self.__email
    
    def setEmail(self):
        print("Defina um novo email.")
        novoemail = input("Email: ")
        self.__email = novoemail

    def exibir(self):
        print(
            f"Meu nome: {self.__nome}\nIdade: {self.__idade}\nCPF: {self.__cpf}\nEmail: {self.__email}."
            )

class Prof(PessoaIFRO): #prof
    def __init__(self, nome: str, idade: int, cpf: int, email: str, atendimento: str, curso: str):
        self.__atendimento = atendimento
        self.__curso = curso
    
        super().__init__(nome, idade, cpf, email)
    
    def exibir(self):
        super().exibir()
        print(f"\nAtendimento: {self.__atendimento}\nCurso: {self.__curso}.")
        
class Adm(PessoaIFRO): #adm
    def __init__(self, nome: str, idade: int, cpf: int, email: str):
        super().__init__(nome, idade, cpf, email)
    
    def exibir(self):
        super().exibir()


class Aluno(PessoaIFRO): #aluno
    def __init__(self, nome: str, idade: int, cpf: int, email: str, matricula:str, curso: str):
        self.matricula = matricula
        self.curso = curso
        super().__init__(nome, idade, cpf, email)
        
    def getmatricula(self):
        return self.matricula
    
    def exibir(self):
        super().exibir()
        print("\nMatrícula: {self.matricula}")