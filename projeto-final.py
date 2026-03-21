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
                if num.isalpha() == True or num is None:
                    raise ValueError
            break

        except TypeError:
            print("Insira seu cpf completo")
            continue

        except ValueError:
            print("Seu cpf pode ter apenas numeros")
            continue
        
    return cpf
        

name = str(input("Insira seu nome: "))
cpf = pegar_cpf()
senha = pegar_senha()
