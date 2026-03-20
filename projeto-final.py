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



name = str(input("Insira seu nome: "))
cpf = str(input("Insira seu pdf em formato xxx-xxx-xxx-xx: "))
senha = pegar_senha()
