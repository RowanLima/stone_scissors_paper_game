import random
import os
import time

contador_empate = 0
contador_derrotas = 0
contador_vitorias = 0
contador_msg = 0

class color:
    Vermelho = '\033[91m'
    verde = '\033[92m'
    Amarelo = '\033[93m'
    Resetar = '\033[0m'
    Negrito = '\033[1m'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def zerar_cont():
    global contador_empate
    global contador_derrotas
    global contador_vitorias
    contador_empate = 0
    contador_derrotas = 0
    contador_vitorias = 0


def jogar_novamente():
    print(color.Negrito + "Jogar Novamente?" + color.Resetar, "(", color.verde + "y" + color.Resetar, "/", color.Vermelho + "n" + color.Resetar,")", "\n")
    jogar_dnv = input()

    if jogar_dnv == ("y"):
        play()

    elif jogar_dnv == ("n"):
        print("\n", color.Amarelo + "Encerrando Jogo..." + color.Resetar)
        time.sleep(1)
        clear_screen()

    elif jogar_dnv != ("y", "n"):
        print("\n", color.Vermelho + "Opção Invalida" + color.Resetar)
        time.sleep(1)
        clear_screen()
        print(color.Negrito + "COMPUTADOR:" + color.Resetar, color.verde + "-Ok erros acontecem, vou te dar um desconto." + color.Resetar, "\n", "Jogar Novamente?" + color.Resetar, "(", color.verde + "y" + color.Resetar, "/", color.Vermelho + "n" + color.Resetar,")", "\n")
        jogar_dnv = input()

        if jogar_dnv == ("y"):
            play()

        elif jogar_dnv == ("n"):
            print("\n", color.Amarelo + "Encerrando Jogo..." + color.Resetar)
            time.sleep(1)
            clear_screen()

        elif jogar_dnv != ("y", "n"):
            print("\n", color.Vermelho + "Opção Invalida" + color.Resetar)
            time.sleep(1)
            clear_screen()
            print(color.Negrito + "COMPUTADOR:" + color.Resetar, color.Amarelo + "-Cara, isso já é sacangem. vou tentar uma ultima vez." + color.Resetar, "\n", "Jogar Novamente?" + color.Resetar, "(", color.verde + "y" + color.Resetar, "/", color.Vermelho + "n" + color.Resetar,")", "\n")
            jogar_dnv = input()

            if jogar_dnv == ("y"):
                play()

            elif jogar_dnv == ("n"):
                print("\n", color.Amarelo + "Encerrando Jogo..." + color.Resetar)
                time.sleep(1)
                clear_screen()

            elif jogar_dnv != ("y", "n"):
                print("\n", color.Vermelho + "Opção Invalida" + color.Resetar)
                time.sleep(1)
                clear_screen()
                print(color.Negrito + "COMPUTADOR:" + color.Resetar, color.Vermelho + "-Não fui programado para ter paciência..." + color.Resetar)
                time.sleep(2)
                clear_screen()


def play():
    global contador_empate
    global contador_derrotas
    global contador_vitorias
    clear_screen()
    print (color.Negrito + "Pedra" + color.Resetar, "=", color.Amarelo + "p" + color.Resetar, "|", color.Negrito + "Papel" + color.Resetar, "=", color.Amarelo + "pp" + color.Resetar, "|", color.Negrito + "Tesoura" + color.Resetar, "=", color.Amarelo + "t" + color.Resetar, "|", color.Negrito + "Zerar Contador" + color.Resetar, "=", color.Amarelo + "z" + color.Resetar, "\n")
    print(" Nº de Vitorias: ", contador_vitorias, "\n", "Nº de Empates:  ", contador_empate, "\n", "Nº de Derrotas: ", contador_derrotas,"\n")
    player = input("player: ")
    computador = random.choice(["p", "pp", "t"])


    if player == ("t") and computador == ("t"):
        contador_empate += 1
        print("maquina: ", computador, "\n")
        print(color.Amarelo + "EMPATE!" + color.Resetar)
        print("\n", "Nº de Empates: ", contador_empate, "\n")
       

    elif player == ("p") and computador == ("t"):
        contador_vitorias += 1
        print("maquina: ", computador, "\n")
        print(color.verde + "VENCEU!!!" + color.Resetar)
        print("\n", "Nº de Vitorias: ", contador_vitorias, "\n") 


    elif player == ("pp") and computador == ("t"):
        contador_derrotas += 1
        print("maquina: ", computador, "\n")
        print(color.Vermelho + "PERDEU :(" + color.Resetar)
        print("\n", "Nº de Derrotas: ", contador_derrotas, "\n")
       

    elif player == ("t") and computador == ("p"):
        contador_derrotas += 1
        print("maquina: ", computador, "\n")
        print(color.Vermelho + "PERDEU :(" + color.Resetar)
        print("\n", "Nº de Derrotas: ", contador_derrotas, "\n")


    elif player == ("p") and computador == ("p"):
        contador_empate += 1
        print("maquina: ", computador, "\n")
        print(color.Amarelo + "EMPATE!" + color.Resetar)
        print("\n", "Nº de Empates: ", contador_empate, "\n")
      

    elif player == ("pp") and computador == ("p"):
        contador_vitorias += 1
        print("maquina: ", computador, "\n")
        print(color.verde + "VENCEU!!!" + color.Resetar)
        print("\n", "Nº de Vitorias: ", contador_vitorias, "\n")


    elif player == ("t") and computador == ("pp"):
        contador_vitorias += 1
        print("maquina: ", computador, "\n")
        print(color.verde + "VENCEU!!!" + color.Resetar)
        print("\n", "Nº de Vitorias: ", contador_vitorias, "\n")
       

    elif player == ("p") and computador == ("pp"):
        contador_derrotas += 1
        print("maquina: ", computador, "\n")
        print(color.Vermelho + "PERDEU :(" + color.Resetar)
        print("\n", "Nº de Derrotas: ", contador_derrotas, "\n")
    

    elif player == ("pp") and computador == ("pp"):
        contador_empate += 1
        print("maquina: ", computador, "\n")
        print(color.Amarelo + "EMPATE!" + color.Resetar)
        print("\n", "Nº de Empates :", contador_empate, "\n") 


    elif player == ("z"):
        zerar_cont()
        play()


    elif player != ("p", "pp", "t", "z"):
        print("\n", color.Vermelho + "Opção Invalida" + color.Resetar)
        time.sleep(1)
        play()

    jogar_novamente()

play()