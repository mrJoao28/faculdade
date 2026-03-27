"""
cadastro bancario
"""

class Conta :
    contas = list()
    conta_id = 0
    def __init__(self,nome,email,cpf,senha):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.id = Conta.conta_id
        self.dinheiro = 100
        Conta.conta_id +=1
        Conta.contas.append(self)


    def transferir (self , valor , conta):
        if self.dinheiro >= valor :
            Conta.contas[conta].dinheiro += valor
            self.dinheiro -= valor
        else :
            print("Saldo insuficiente")


def pegar_senha():
    while True:
        try :
            senha = int(input("Insira uma senha de cinco digitos: "))
            if len(str(senha)) != 5:
                raise TypeError
            else:
                break
        except ValueError:
            print("insira uma senha valida")

        except TypeError:
            print("Insira uma senha valida")
    return senha

def pegar_cpf():
    while True:
        try:
            cpf = str(input("Insira seu cpf em formato xxx-xxx-xxx-xx: ")).strip()
            if len(cpf) != 14:
                raise TypeError
            nums =  cpf.split("-")
            for num in nums:
                for n in num:
                    if n.isnumeric == False or n is None:
                        raise ValueError
            break

        except TypeError:
            print("Insira seu cpf completo")
            continue

        except ValueError:
            print("Seu cpf pode ter apenas numeros")
            continue
        
    return cpf
        
def pegar_email():
    while True:
        try:
            email = str(input("Digite seu email: ")).strip()
            if "@" not in email :
                raise ValueError
            
            break
        except ValueError:
            print("Digite o email corretamente")
            continue
    return email

def criar_conta():
    name = str(input("Insira seu nome: "))
    print("*"*24)
    email = pegar_email()
    print("*"*24)
    cpf = pegar_cpf()
    print("*"*24)
    senha = pegar_senha()
    print("*"*24)
    conta = Conta(name,email,cpf,senha)
    return conta

def deletar_conta(conta_id):
    Conta.contas.pop(conta_id)
    return "conta deletadaa"

print("*"*24)
print("*"+" "*3+"SISTEMA BANCÁRIO"+" "*3+"*")
print("*"*24)

