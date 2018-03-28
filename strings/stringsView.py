def solicitarMaximo():
    #max = 'Aguardando valor máximo'
    max = input('Qual o valor máximo de caracteres por linha? ')
    
    while not max.isnumeric():
        max = input('Qual o valor máximo de caracteres por linha? ')

    max = int(max)
    return max

def checarMaximo(max):
    if max > 40:
        print('O valor escolhido excede o máximo permitido que é de 40 caracteres')
        return False
    else:
        return True
