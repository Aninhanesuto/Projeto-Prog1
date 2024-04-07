######################################################
# Programação Funcional / Programção I (2022/2)
# EP2 - Jogo da Velha
# Nome: Ana Clara Sesana Moreira    
# Matrícula:2022100199
######################################################

import random
from os import system, name


def telaInicial():
    """
    Essa função serve para imprimir no Terminal a tela inicial do programa, imprimindo a formatação e a ASCII ART.
    Parâmetro: Nenhum
    Return: None
    """
    RED ="\033[1;31m" # Muda a cor do Terminal para vermelho
    print(RED)
    print(f"+{'-' * 37}+")
    print("| SEJA BEM VINDO(A) AO JOGO DA VELHA! |")
    print(f"+{'-' * 37}+")
    print("_"* 98)
    print("""⠀⠀⠀⠀⠀
|                                     ⣴⠉⡙⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⣚⡯⠴⢬⣱⡀                                  |⠀
|                                ⠀⠀⠀⠀⢰⡇⣷⡌⢲⣄⡑⢢⡀⠀⠀⠀⠀⠀⢠⠾⢋⠔⣨⣴⣿⣷⡌⠇⡇                                  |⠀
|                                ⠀⠀⠀⠀⢸⢹⣿⣿⣄⢻⣿⣷⣝⠷⢤⣤⣤⡶⢋⣴⣑⠟⠿⠿⠿⣿⣿⡀⡇⠀                                 |
|                                ⠀⠀⠀⠀⢸⢸⣿⡄⢁⣸⣿⣋⣥⣶⣶⣶⣶⣶⣶⣿⣿⣶⣟⡁⠚⣿⣿⡇⡇⠀                                 |
|                                ⢀⣠⡤⠤⠾⡘⠋⢀⣘⠋⠉⠉⠉⠉⢭⣭⣭⣭⣍⠉⢩⣭⠉⠉⠂⠙⠛⠃⣇⡀                                 |                               
|                                ⠏⠀⠀⢿⣿⣷⡀⠀⢿⡄⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣆⠀⢿⣇⠀⠀⠀⠀⠀⠀⠈⢱                               |
|                                ⣦⠀⠀⠈⢿⣿⣧⠀⠘⣿⠀⠀⠀⡀⠀⠀⠘⣿⣿⣿⣿⡆⠀⢻⡆⠀⠀⠀⠀⠀⠀⢸                               |
|                                ⢻⡄⠀⠀⠘⠛⠉⠂⠀⠙⠁⠀⣼⣧⠀⠀⠀⠈⠀⠀⠈⠙⠀⠘⠓⠀⠀⠀⠀⠀⢀⡟                               |
|                                ⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣏⠀                              |
|                                ⠀⠀⠛⢶⢰⣶⢢⣤⣤⣄⠲⣶⠖⠀⣙⣀⠀⠀⠀⠤⢤⣀⣀⡀⣀⣠⣾⠟⡌⠀                                 |
|                                ⠀⠀⠀⠘⢄⠃⣿⣿⣿⣿⠗⠀⠾⢿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⠸⠟⣡⣤⡳⢦                                 |
|                                ⠀⠀⠀⠀⠀⢻⡆⣙⡿⢷⣾⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⡿⠟⢡⣴⣾⣿⣿⣿⣦                                 |
|                                ⠀⠀⠀⠀⠀⡼⢁⡟⣫⣶⣍⡙⠛⠛⠛⠛⠛⣽⡖⣉⣠⣶⣶⣌⠛⢿⣿⣿⣿⣿                                 |
|                                ⠀⠀⠀⢀⠔⢡⢎⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠹⣿⣿⣿                                 |
|                                ⠀⢠⠖⢁⣴⡿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⣿⣿                                 |   
""")
    print("_"* 98)
    print("")
    print("")
    print("")
    print("")

    _ = input("---> Tecle Enter para Jogar.")
    limpaTela()

def getMatricula():
    """
    Retorna a matricula do aluno como string
    Parâmetro: Nenhum
    """
    return "2022100199" 

def getNome():
    """
    Retorna o nome completo do aluno
    Parâmetro: Nenhum
    """
    return "Ana Clara Sesana Moreira"

def escolhaUsuário():
    """
    Função que pergunta ao jogador se ele quer "X" ou "O". 
    Além disso, essa função também serve para verificar se o usuário digitou algo que não seja uma string ou que não seja os símbolos do jogo.
    Caso ele tenha digitado algo que não seja válido, a função irá chamar ela recursivamente até que seja válida.
    Parâmetros: Nenhum
    Return: "X" ou "O"
    """
    simboloJoga = verificar(input("Você quer ser 'X' ou 'O'? "), str)
    if (simboloJoga != "X" and simboloJoga != "x" and simboloJoga != "O" and simboloJoga != "o"):
        print("Simbolo Inválido!")
        return escolhaUsuário()
    elif simboloJoga == "X" or simboloJoga == "x":return "X", "O"
    elif simboloJoga == "O" or simboloJoga == "o":return "O", "X"

def imprimeTab(tab):
    """
    Função que imprime o tabuleiro.
    Return: None
    Parâmetros: tab - recebe o tabuleiro
    """
    RED ="\033[1;31m" # Muda a cor do Terminal para vermelho
    print(RED)
    print(f"+{'-' * 29}+")
    print(f"""|          {tab[7]} | {tab[8]} | {tab[9]}          |\n|         ---+---+---         |\n|          {tab[4]} | {tab[5]} | {tab[6]}          |\n|         ---+---+---         |\n|          {tab[1]} | {tab[2]} | {tab[3]}          |""")
    print(f"+{'-' *29}+")
    

def verificar(valor, convert):
    """
    Essa função recursiva, tenta  converter os valores para valores aceitos para não quebrar o programa
    Parâmetros: 
    - valor: Essa será a variável que será convertida
    - convert: Esse parâmetro poderá ser str, int ou float(para tentar converter a variável para seu tipo)
    Return:
    - Essa função retorna o valor convertido, ou uma mensagem pedindo o usuário que digite novamente até que o usuário
    digite um valor válido.
    """
    try: #Tenta fazer a conversão do valor digitado para int
        x = convert(valor)
        return x
    except : #Se não for possível fazer a conversão , uma exceção é lançada
        return verificar(input("Opção não reconhecida!, Digite Novamente: "), convert)

def jogadaUsuário(tabu):
    """
    Pergunta ao jogador onde ele quer jogar, e também verifica algumas posiçõs inválidas (pois alguém já jogou nela).
    Além disso, elá também irá verificar se o valor digitado é inteiro e se está dentro do intervalo
    Caso a posição não seja válida, ela irá chamar a função recursivamente até que seja digitado um valor válido.
    Parâmetros: tabu - tabuleiro(recebe o tabuleiro)
    Return: Retorna a posição digitada pelo Usuário
    """
    posicao = verificar(input("Qual posição deseja marcar (1-9): "), int)
    if posicao<1 or posicao>9:
        print("Operação Inválida!")
        return jogadaUsuário(tabu)
    elif (tabu[posicao] != " "):
        print("Essa posição já foi escolhida. Escolha outra!")
        return jogadaUsuário(tabu)
    else: return posicao



def randomComputador():
    """
    Essa função randomComputador irá sortear quem começa.
    Caso o sorteio seja 1, o Usuário irá começar,caso seja 2 o computador que irá começar.
    Parâmetros: Nenhum
    Return: escolha - a escolha de quem irá começar, ou seja o usuário ou o computador.
    """
    escolha = random.randint(1,2)    
    if escolha == 1:
        print("Você começa.")
        return escolha        
    elif escolha == 2:
        print("O computador começa.")
        return escolha


def limpaTela(): 
    """
    Essa função é autoexplicativa,ela irá limpar a tela do Terminal.
    Parâmetros: Nenhum
    """ 
    if name == 'nt': 
        system('cls') 
    else:
	    system('clear') 

def verificaGanhador(tab, simbolo):
    """
    Essa função irá verificar se o usuário ou o computador ganhou.
    Parâmetros: 
    *tab -  recebe o tabuleiro
    *simbolo - Se é o simbolo "X" ou "O"
    Return - Retorna True ou False, será True se o usuário ou o computador ganhou e False, caso contrário.
    """
    if tab[1] == simbolo and tab[2] == simbolo and tab[3] == simbolo: 
        return True
    elif tab[4] == simbolo and tab[5] == simbolo and tab[6] == simbolo: 
        return True
    elif tab[7] == simbolo and tab[8] == simbolo and tab[9] == simbolo: 
        return True
    elif tab[1] == simbolo and tab[5] == simbolo and tab[9] == simbolo: 
        return True
    elif tab[3] == simbolo and tab[5] == simbolo and tab[7] == simbolo: 
        return True
    elif tab[1] == simbolo and tab[4] == simbolo and tab[7] == simbolo: 
        return True
    elif tab[2] == simbolo and tab[5] == simbolo and tab[8] == simbolo: 
        return True
    elif tab[3] == simbolo and tab[6] == simbolo and tab[9] == simbolo: 
        return True
    return False


def empate(tab):
    """
    Essa função irá verificar se o jogo deu empate
    Parâmetros: tab - recebe o tabuleiro
    Return: Retornará True se o jogo deu velha e False, caso contrário.
    """
    if " " in tab: return False
    return True


def jogadas(tab,vez,simboloJoga, simboloComputado):
    """
    Essa função "jogadas"  será responsável por intercalar a jogada do Usuário e do Computador. 
    Primeiro, ela irá verificar se alguém ganhou ou se deu empate, caso isso não ocorra, ela chama a função pro 
    usuário escolher uma posição ou irá chamar a função "jogadaComputador", para o computador fornecer uma posição, dependendo de quem começou a jogar primeiro.
    Parâmetros:
    *tab - recebe o tabuleiro
    *vez - recebe uma váriavel Flag, pra verificar quem começa
    *simboloJoga - simbolo do Jogador.
    *simboloComputado - simbolo do Computador
    Return:
    Ela é uma função recursiva que fica retornando ela mesma, até que alguém ganhe, perca ou empate e  caso isso ocorra ela irá retorna None.
    """
    if verificaGanhador(tab, simboloJoga):
        print("Você venceu!")
        imprimeTab(tab)
        x = input("--> Enter para continuar...")
        return
    elif verificaGanhador(tab, simboloComputado):
        print("O Computador venceu!")
        imprimeTab(tab)
        x = input("--> Enter para continuar...")
        return
    elif empate(tab):
        print("Empate!")
        imprimeTab(tab)
        x = input("--> Enter para continuar...")
        return
    
    if vez == True:
        jc = jogadaUsuário(tab)
        tab[jc] = simboloJoga
        print(f"O usuário escolheu a posição: {jc}")
        imprimeTab(tab)
        vez = False
    elif vez == False:
        jc = jogadaComputador(tab, simboloComputado)
        tab[jc] = simboloComputado
        print(f"O computador escolheu a posição: {jc}")
        imprimeTab(tab)
        vez = True
    jogadas(tab, vez, simboloJoga, simboloComputado)
    

def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estrategia:
    *Primeiro eu verifico, se quem começará a jogar é o computador, se for, eu sorteio uma dessas posições [5, 1, 7, 9]
    *Em segundo,eu verifico se alguém jogou, caso tenham jogado eu escolho umas dessas opções [5,1,7] caso estejam disponíveis.
    *Depois eu verifico, se dar pro computador ganhar e retorno o valor.
    *Por último, se o usuário estiver tentando ganhar eu tento impedir ele e se não for nenhuma dessas opções eu sorteio uma posição livre que esteja disponível.
    *Mais informações no PDF.
    """
    simboloJoga = "X" if simboloComputador=="O" else "O"
    posicao = posicoeslivres(tabuleiro)
    if len(posicao) == 9: return random.choice([5, 1, 7, 9])
    elif len(posicao) == 8:
        if 5 in posicao: return 5
        elif 1 in posicao: return 1
        else: return 7
    elif tabuleiro[1] == simboloComputador and tabuleiro[2] == simboloComputador and 3 in posicao: 
        return 3
    elif tabuleiro[1] == simboloComputador and tabuleiro[3] == simboloComputador and 2 in posicao: 
        return 2
    elif tabuleiro[2] == simboloComputador and tabuleiro[3] == simboloComputador and 1 in posicao: 
        return 1
    elif tabuleiro[4] == simboloComputador and tabuleiro[5] == simboloComputador and 6 in posicao: 
        return 6
    elif tabuleiro[4] == simboloComputador and tabuleiro[6] == simboloComputador and 5 in posicao: 
        return 5
    elif tabuleiro[5] == simboloComputador and tabuleiro[6] == simboloComputador and 4 in posicao: 
        return 4
    elif tabuleiro[7] == simboloComputador and tabuleiro[8] == simboloComputador and 9 in posicao: 
        return 9
    elif tabuleiro[7] == simboloComputador and tabuleiro[9] == simboloComputador and 8 in posicao: 
        return 8
    elif tabuleiro[8] == simboloComputador and tabuleiro[9] == simboloComputador and 7 in posicao: 
        return 7
    elif tabuleiro[1] == simboloComputador and tabuleiro[4] == simboloComputador and 7 in posicao: 
        return 7
    elif tabuleiro[1] == simboloComputador and tabuleiro[7] == simboloComputador and 4 in posicao: 
        return 4
    elif tabuleiro[4] == simboloComputador and tabuleiro[7] == simboloComputador and 1 in posicao: 
        return 1
    elif tabuleiro[2] == simboloComputador and tabuleiro[5] == simboloComputador and 8 in posicao: 
        return 8
    elif tabuleiro[2] == simboloComputador and tabuleiro[8] == simboloComputador and 5 in posicao: 
        return 5
    elif tabuleiro[5] == simboloComputador and tabuleiro[8] == simboloComputador and 2 in posicao: 
        return 2
    elif tabuleiro[3] == simboloComputador and tabuleiro[6] == simboloComputador and 9 in posicao: 
        return 9
    elif tabuleiro[3] == simboloComputador and tabuleiro[9] == simboloComputador and 6 in posicao: 
        return 6
    elif tabuleiro[6] == simboloComputador and tabuleiro[9] == simboloComputador and 3 in posicao: 
        return 3
    elif tabuleiro[1] == simboloComputador and tabuleiro[5] == simboloComputador and 9 in posicao: 
        return 9
    elif tabuleiro[1] == simboloComputador and tabuleiro[9] == simboloComputador and 5 in posicao: 
        return 5
    elif tabuleiro[5] == simboloComputador and tabuleiro[9] == simboloComputador and 1 in posicao: 
        return 1
    elif tabuleiro[3] == simboloComputador and tabuleiro[5] == simboloComputador and 7 in posicao: 
        return 7
    elif tabuleiro[3] == simboloComputador and tabuleiro[7] == simboloComputador and 5 in posicao: 
        return 5
    elif tabuleiro[7] == simboloComputador and tabuleiro[5] == simboloComputador and 3 in posicao: 
        return 3
    elif tabuleiro[1] == simboloJoga and tabuleiro[2] == simboloJoga and 3 in posicao: 
        return 3
    elif tabuleiro[1] == simboloJoga and tabuleiro[3] == simboloJoga and 2 in posicao: 
        return 2
    elif tabuleiro[2] == simboloJoga and tabuleiro[3] == simboloJoga and 1 in posicao: 
        return 1
    elif tabuleiro[4] == simboloJoga and tabuleiro[5] == simboloJoga and 6 in posicao: 
        return 6
    elif tabuleiro[4] == simboloJoga and tabuleiro[6] == simboloJoga and 5 in posicao: 
        return 5
    elif tabuleiro[5] == simboloJoga and tabuleiro[6] == simboloJoga and 4 in posicao: 
        return 4
    elif tabuleiro[7] == simboloJoga and tabuleiro[8] == simboloJoga and 9 in posicao: 
        return 9
    elif tabuleiro[7] == simboloJoga and tabuleiro[9] == simboloJoga and 8 in posicao: 
        return 8
    elif tabuleiro[8] == simboloJoga and tabuleiro[9] == simboloJoga and 7 in posicao: 
        return 7
    elif tabuleiro[1] == simboloJoga and tabuleiro[4] == simboloJoga and 7 in posicao: 
        return 7
    elif tabuleiro[1] == simboloJoga and tabuleiro[7] == simboloJoga and 4 in posicao: 
        return 4
    elif tabuleiro[4] == simboloJoga and tabuleiro[7] == simboloJoga and 1 in posicao: 
        return 1
    elif tabuleiro[2] == simboloJoga and tabuleiro[5] == simboloJoga and 8 in posicao: 
        return 8
    elif tabuleiro[2] == simboloJoga and tabuleiro[8] == simboloJoga and 5 in posicao: 
        return 5
    elif tabuleiro[5] == simboloJoga and tabuleiro[8] == simboloJoga and 2 in posicao: 
        return 2
    elif tabuleiro[3] == simboloJoga and tabuleiro[6] == simboloJoga and 9 in posicao: 
        return 9
    elif tabuleiro[3] == simboloJoga and tabuleiro[9] == simboloJoga and 6 in posicao: 
        return 6
    elif tabuleiro[6] == simboloJoga and tabuleiro[9] == simboloJoga and 3 in posicao: 
        return 3
    elif tabuleiro[1] == simboloJoga and tabuleiro[5] == simboloJoga and 9 in posicao: 
        return 9
    elif tabuleiro[1] == simboloJoga and tabuleiro[9] == simboloJoga and 5 in posicao: 
        return 5
    elif tabuleiro[5] == simboloJoga and tabuleiro[9] == simboloJoga and 1 in posicao: 
        return 1
    elif tabuleiro[3] == simboloJoga and tabuleiro[5] == simboloJoga and 7 in posicao: 
        return 7
    elif tabuleiro[3] == simboloJoga and tabuleiro[7] == simboloJoga and 5 in posicao: 
        return 5
    elif tabuleiro[7] == simboloJoga and tabuleiro[5] == simboloJoga and 3 in posicao: 
        return 3
    
    return Livre(tabuleiro)

def posicoeslivres(ls, result = [], i=1):
    """
    Verifica as posições livres
    Parâmetros: ls, result and i.
    Return: Retorna as posições que estão livres de 1 ate 9.
    """
    if i==1: result = []
    if i>9: return result
    if ls[i] == " ": result+=[i]
    return posicoeslivres(ls, result, i+1)

def Livre(tab):
    """
    Essa funcao receba o tabuleiro e retorna uma posição livre.
    Parâmetro: tab - tabuleiro
    Return: pos - a posição livre
    """
    pos = posicoeslivres(tab)
    a = random.randint(0, len(pos)-1)
    return pos[a]


def main():
    """
    Essa é a função principal, na qual eu chamo as outras funções
    """
    limpaTela()
    telaInicial() 
    limpaTela()
    tab = [" "]*10
    tab[0] = "k" 
    imprimeTab(tab)
    simboloJoga, simboloComputador = escolhaUsuário()
    escolha = 0
    escolha = randomComputador()
    if escolha == 1:
        vez = True #Variável Flag
        jogadas(tab,vez, simboloJoga, simboloComputador)
    else:
        vez = False #Variável Flag
        jogadas(tab,vez, simboloJoga, simboloComputador)
   
    NovoJogo = input("Deseja jogar novamente? (S/N) ") #Verifica se o usuário quer jogar novamente
    if NovoJogo in "Ss": #Se for sim, ele irá executar a função main novamente.
        main()
    elif NovoJogo in "Nn":#Caso seja não, ele irá sair do programa.
        exit()
    
    #Você pode, se quiser, comentar os dois prints abaixo:
    #print(getNome())
    #print(getMatricula())


################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()
