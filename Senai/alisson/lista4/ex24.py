candidatoa = 0
candidatob = 0
candidatoc = 0
branco = 0
nulo = 0
contador = 0
while True:
    if contador >= 20:
        break
    else:
        while True:
            print("1- Candidato A\n2- Candidato B\n3- Candidato C\n4- Voto em Branco\n5- Voto nulo")
            voto = int(input("Digite seu voto: "))
            print()
            if voto == 1:
                candidatoa += 1
                break
            elif voto == 2:
                candidatob += 1
                break
            elif voto == 3:
                candidatoc += 1
                break
            elif voto == 4:
                branco += 1
                break
            elif voto == 5:
                nulo += 1
                break
            else:
                print("Voto invalido. Digite novamente!")
                continue
    contador += 1
if candidatoa > candidatob and candidatoa > candidatoc:
    resultado = "Vencedor: Candidato A"
elif candidatob > candidatoa and candidatob > candidatoc:
    resultado = "Vencedor: Candidato B"
elif candidatoc > candidatoa and candidatoc > candidatob:
    resultado = "Vencedor: Candidato C"
elif candidatoa == candidatob and candidatoa > candidatoc:
    resultado = "Empate entre Candidato A e B"
elif candidatoa == candidatoc and candidatoa > candidatob:
    resultado = "Empate entre Candidato A e C"
elif candidatob == candidatoc and candidatob > candidatoa:
    resultado = "Empate entre Candidato B e C"
elif candidatoa == candidatob == candidatoc:
    resultado = "Empate entre todos os candidatos"
print(f"1. Candidato A: {candidatoa}, Candidato B: {candidatob}, Candidato C: {candidatoc}")
print(f"2. Votos em branco: {branco}")
print(f"3. Votos nulos: {nulo}")
print(f"4. Resultado: {resultado}")