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

def quantas_ferraduras():
    cavalos  = int(input("QUantos cavalos tem? : "))
    return "Serão necessarios {} ferraduras".format(cavalos*4)

def carro():
    capacidade_maxima = float(input("QUal é a capacidade do tanque? : "))
    litros_abastecidos = float(input("QUantos litros foram abastecidos? : "))
    kilometros_percorridos = float(input("Quantos quilometors foram percorridos?: "))
    performace = kilometros_percorridos/litros_abastecidos
    resto = (capacidade_maxima-litros_abastecidos)*performace
    return "O carro tem uma performace de {} km/l e poderia percorrer mais {} km".format(performace , resto)

