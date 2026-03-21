lista = ["comprimento","largura","altura"]

for a in range(len(lista)):
    lista[a] = float(input("Insira a " + lista[a] + ": "))

for a in lista:
    print(a,end=" ")

