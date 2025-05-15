nomes = ["Aurelio","Guilherme","joao","Jose","Maria","Beatriz","Joana","Julia","Maria Luiza","Tamyre","    ana    "]
def nome_curto(nomes):
    mais_curto = nomes[0]
    for i in range(len(nomes)):
        if len(nomes[i].strip()) < len(mais_curto.strip()):
            mais_curto = nomes[i]
    return mais_curto.strip().capitalize()
print(nome_curto(nomes))