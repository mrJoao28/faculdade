"""
cadastro bancario
"""
import math


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
            cpf = str(input("Insira seu cpf em formato xxx-xxx-xxx-xx: "))
            if len(cpf) != 14:
                raise TypeError
            nums =  cpf.split("-")
            for num in nums:
                for n in num:
                    if n.isalnum != False or n is None:
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
            email = str(input("Digite seu email: "))
            if "@" not in email :
                raise ValueError
            
            break
        except ValueError:
            print("Digite o email corretamente")
            continue
    return email

name = str(input("Insira seu nome: "))
email = pegar_email()
cpf = pegar_cpf()
senha = pegar_senha()
