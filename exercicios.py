def media_ponderada(n1,n2,n3,n4,n5):
    media = (n1*1 + n2*2 + n3*3 + n4*4 + n5*5) /(15)
    return media

def area_circulo(raio):
    return (raio**2) *3.14

def inverter_numero(numero):
    temp = numero[2]
    numero[2] = numero[0]
    numero[0] = temp
    return numero

def calcurar_terreno():
    largura = float(input("Qual é a largura? : "))
    comprimento = float(input("QUal é o comprimeto? : "))
    return "O terreno tem a area de {} metros quadrados".format(largura*comprimento)
