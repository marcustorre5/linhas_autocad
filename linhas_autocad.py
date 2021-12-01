from time import sleep

print('→'*20)
print('LINHAS CAD')
print("→"*20)

def linhas():

    line = open('linhascad.scr','a')
    line.write('LINE'+"\n")
    line.close()

    arq = open('linhascad.scr','a')
    arq.write('0,0'+"\n")
    arq.close()
    while True:
        numero = input('Tamanho da linha: ')
        ang = input(('Ângulo da Linha: '))
        arquivo = open('linhascad.scr', 'a',)
        arquivo.write('@'+numero+'<'+ang+"\n")
        arquivo.close()

        if numero == '++':
            break
        if ang == '++':
            break
linhas()

def creditos():
    print('▬' * 17)
    print('▐                         ▐')
    print('▐      Desenvolvido by:   ▐')
    print('▐      Marcus Torres      ▐')
    print('▐      @marcustorre5      ▐')
    print('▐           ☺             ▐')
    print('▐                         ▐')
    print('▬' * 17)

    sleep(3)

creditos()