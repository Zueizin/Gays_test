def computador_escolhe_jogada(n, m):
    jogada = n % (m + 1)
    if jogada == 0:
        jogada = m
    return jogada

def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada >= 1 and jogada <= m and jogada <= n:
            return jogada
        else:
            print("Jogada inválida!")
            
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("\nVocê começa!")
        vez_do_computador = False
    else:
        print("\nComputador começa!")
        vez_do_computador = True

    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            print(f"\nO computador tirou {jogada} peça(s).")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            print(f"\nVocê tirou {jogada} peça(s).")

        n -= jogada
        print(f"Agora restam {n} peça(s) no tabuleiro.\n")

        vez_do_computador = not vez_do_computador

    if vez_do_computador:
        print("Você ganhou!")
    else:
        print("O computador ganhou!")

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

escolha = int(input("Escolha: "))

i = 1

if escolha == 1:
    print("\nVocê escolheu uma partida isolada!")
    partida()
elif escolha == 2:
    print("\nVocê escolheu um campeonato!")
    while i <= 3:
        print(f"\n**** Rodada {i} ****")
        partida()
        i = i + 1
    print("\n**** Final do campeonato! ****")
    print("Placar: Você 0 X 3 Computador")
else:
    print("Opção inválida. Encerrando o jogo.")