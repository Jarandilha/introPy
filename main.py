# 1 - Imports / bibliotecas

# 2 - Classe

# 3 Metodos e Funções
# Def = definition = definição


def print_hi(name):
       print(f'Oi, {name}')
       print('Oi, ' + name)

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadardo(lado):
    return lado ** 2

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2

def contagem_progressiva(fim):
    for numero  in range(fim): # repetir o bloco de zero até o fim
        print(numero)          # exibir o numero

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        # contador = numero + 1
        # print(f'{contador} - nome')

            if numero < 9:
                print(f'00{numero + 1} - {nome}')
            elif numero < 99:
                print(f'0{numero + 1} - {nome}')
            else:
                print(numero + 1, '-', nome)

def brincar_de_plin(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))

# estrutura de identificação / exeução do escript
if __name__ == '__main__':

    resposta = "C"

    while resposta.upper() != 'Z':

        print('#########################################')
        print('#                                       #')
        print('#     M E N U    D E    O P Ç Õ E S     #')
        print('#                                       #')
        print('#         1 - Olá Mundo                 #')
        print('#         2 - Área do Retângulo         #')
        print('#         3 - Área do Quadrado          #')
        print('#         4 - Área do Triângulo         #')
        print('#         5 - Contagem Progressiva      #')
        print('#         6 - Apoiar candidato          #')
        print('#         7 - Brincar de Plim           #')
        print('#                                       #')
        print('#          Z - Sair                     #')
        print('#                                       #')
        print('#########################################')

        resposta = input("Escolha Sua Opção")
        print(f'A sua escolha foi: {resposta} ')

        if resposta.upper() != 'Z':
            if resposta == '1':
                print_hi('Jefferson')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(8,7)
                print(f' A área do retângulo é de {resultado} m²')
            elif resposta == '3':
                resultado = calcular_area_do_quadardo(6)
                print(f' A área do quadrado é de {resultado} m²')
            elif resposta == '4':
                resultado = calcular_area_do_triangulo(5,8)
                print(f' A área do triângulo é de {resultado} m²')
            elif resposta == '5':
                contagem_progressiva(10)
            elif resposta == '6':
                apoiar_candidato('Murphy',13)
            elif resposta == '7':
                brincar_de_plin(20)
            else:
                print('Você digitou uma opção inválida. Escolha uma opção de 1 a 7')
        else:
            print("Você escolheu sair. Volte sempre")