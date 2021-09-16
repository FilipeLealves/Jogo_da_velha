import os

linhas = ['\u2503','\u2501','\u254B']
A = linhas[0]
B = linhas[1]
C = linhas[2]
P1 = ''
P2 = ''
ganhador = 0
os.system('cls')

M = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def ganhar():
    global ganhador
    
    if  (M[0][0] == 'X' and M[0][1] == 'X' and M[0][2] == 'X'):
        ganhador = 1
    elif(M[1][0] == 'X' and M[1][1] == 'X' and M[1][2] == 'X'):
        ganhador = 1
    elif(M[2][0] == 'X' and M[2][1] == 'X' and M[2][2] == 'X'):
        ganhador = 1
    elif(M[0][0] == 'X' and M[1][0] == 'X' and M[2][0] == 'X'):
        ganhador = 1
    elif(M[0][1] == 'X' and M[1][1] == 'X' and M[2][1] == 'X'):
        ganhador = 1
    elif(M[0][2] == 'X' and M[1][2] == 'X' and M[2][2] == 'X'):
        ganhador = 1
    elif(M[0][0] == 'X' and M[1][1] == 'X' and M[2][2] == 'X'):
        ganhador = 1
    elif(M[2][0] == 'X' and M[1][1] == 'X' and M[0][2] == 'X'):
        ganhador = 1
    elif(M[0][0] == 'O' and M[0][1] == 'O' and M[0][2] == 'O'):
        ganhador = 2
    elif(M[1][0] == 'O' and M[1][1] == 'O' and M[1][2] == 'O'):
        ganhador = 2
    elif(M[2][0] == 'O' and M[2][1] == 'O' and M[2][2] == 'O'):
        ganhador = 2
    elif(M[0][0] == 'O' and M[1][0] == 'O' and M[2][0] == 'O'):
        ganhador = 2
    elif(M[0][1] == 'O' and M[1][1] == 'O' and M[2][1] == 'O'):
        ganhador = 2
    elif(M[0][2] == 'O' and M[1][2] == 'O' and M[2][2] == 'O'):
        ganhador = 2
    elif(M[0][0] == 'O' and M[1][1] == 'O' and M[2][2] == 'O'):
        ganhador = 2
    elif(M[2][0] == 'O' and M[1][1] == 'O' and M[0][2] == 'O'):
        ganhador = 2

    
def jogadores():
    global P1, P2
    print('    | JOGO DA VELHA |\n')
    P1 = input('Jogador Nº 1: ')
    P2 = input('Jogador Nº 2: ')
    os.system('cls')

def grid():
    troca = 0
    global ganhador
    while True:
        print('    | JOGO DA VELHA |\n')
        print('        1   2   3\n')
        print(f'   A    {M[0][0]} {A} {M[0][1]} {A} {M[0][2]} ')
        print(f'       {B}{B}{B}{C}{B}{B}{B}{C}{B}{B}{B}')
        print(f'   B    {M[1][0]} {A} {M[1][1]} {A} {M[1][2]} ')
        print(f'       {B}{B}{B}{C}{B}{B}{B}{C}{B}{B}{B}')
        print(f'   C    {M[2][0]} {A} {M[2][1]} {A} {M[2][2]} ')

        ganhar()
        if ganhador == 1:
            print(f'\nJogador {P1} ganhou o jogo!')
        elif ganhador == 2:
            print(f'\nJogador {P2} ganhou o jogo!')

        if ganhador == 0:
            if (troca%2) == 0:
                print(f'\n\n\t {P1} ')
                troca+=1
                marca = True
            else:
                print(f'\n\n\t {P2} ')
                troca+=1
                marca = False
        if ganhador == 0:
            X = input('\nOnde deseja colocar? \n\n>>> ').upper()
        else:
            Y = int(input('\nDeseja reiniciar ?\n[1] - SIM\n[2] - NÃO\n\n>>> '))
            if Y == 1:
                a=0
                while a < 3:
                    M[0][a] = ' '
                    M[1][a] = ' '
                    M[2][a] = ' '
                    a+=1
                X = ' '
                troca = 0
                ganhador = 0
            #else:
                #quit()
                
        
        if marca == True:
            if X == 'A1' or X == '1A':
                M[0][0] = 'X'
            elif X == 'A2' or X == '2A':
                M[0][1] = 'X'
            elif X == 'A3' or X == '3A':
                M[0][2] = 'X'
            elif X == 'B1' or X == '1B':
                M[1][0] = 'X'
            elif X == 'B2' or X == '2B':
                M[1][1] = 'X'
            elif X == 'B3' or X == '3B':
                M[1][2] = 'X'
            elif X == 'C1' or X == '1C':
                M[2][0] = 'X'
            elif X == 'C2' or X == '2C':
                M[2][1] = 'X'
            elif X == 'C3' or X == '3C':
                M[2][2] = 'X'
        else:
            if X == 'A1' or X == '1A':
                M[0][0] = 'O'
            elif X == 'A2' or X == '2A':
                M[0][1] = 'O'
            elif X == 'A3' or X == '3A':
                M[0][2] = 'O'
            elif X == 'B1' or X == '1B':
                M[1][0] = 'O'
            elif X == 'B2' or X == '2B':
                M[1][1] = 'O'
            elif X == 'B3' or X == '3B':
                M[1][2] = 'O'
            elif X == 'C1' or X == '1C':
                M[2][0] = 'O'
            elif X == 'C2' or X == '2C':
                M[2][1] = 'O'
            elif X == 'C3' or X == '3C':
                M[2][2] = 'O'

        os.system('cls')

jogadores()
grid()
