import datetime

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


def aniversario():
    data = input("INsira a sua data de aniversario no formato dia/mes/ano: ")
    data = data.split("/")
    anos = datetime.datetime.now().year - int(data[2])
    meses = datetime.datetime.now().month - int(data[1]) + anos*12
    dias = datetime.datetime.now().day  - int(data[0]) + meses*30
    return "Voce tem {} anos , {} meses e {} dias de vida mn".format(anos,meses,dias)

def prestacao():
    valor = float(input("QUal é o valor da prestaçao em atraso? : "))
    return "O valor atual de sua prestaçao atraseda é {} reais ".format((valor*1,1)*0.9)

def receita():
    paos = int(input("Quantidade de paos vendidos: "))
    broas = int(input("QUantidade de brias vendidas: "))
    return "O total vendido é {} e voce deve colocar na poupança {} reais".format(paos+broas,0.1*(paos*0.12 +broas*1.5))


