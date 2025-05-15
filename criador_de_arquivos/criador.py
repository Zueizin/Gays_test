import os

def selecionar_diretorio():
    """Permite ao usuário selecionar ou criar o diretório onde os arquivos serão salvos."""
    while True:
        caminho = input("Digite o caminho do diretório (deixe em branco para usar o diretório atual): ").strip()
        
        if not caminho:
            return os.getcwd()  # Retorna o diretório atual
        
        # Verifica se o caminho existe
        if os.path.isdir(caminho):
            return caminho
        else:
            print(f"O diretório '{caminho}' não existe.")
            criar = input("Deseja criar este diretório? (S/N): ").strip().upper()
            if criar == 'S':
                try:
                    os.makedirs(caminho)
                    return caminho
                except Exception as e:
                    print(f"Erro ao criar diretório: {e}")
            else:
                print("Por favor, insira um caminho válido.")

def criar_arquivo_py(caminho, nome_arquivo):
    """Cria um arquivo Python vazio no diretório especificado."""
    # Adiciona a extensão .py se não estiver presente
    if not nome_arquivo.endswith('.py'):
        nome_arquivo += '.py'
    
    caminho_completo = os.path.join(caminho, nome_arquivo)
    
    # Verifica se o arquivo já existe
    if os.path.exists(caminho_completo):
        print(f"Aviso: O arquivo '{nome_arquivo}' já existe em '{caminho}' e será sobrescrito.")
    
    # Cria/sobrescreve o arquivo
    try:
        with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
            pass  # Arquivo vazio
        print(f"Arquivo '{nome_arquivo}' criado com sucesso em '{caminho}'!")
    except Exception as e:
        print(f"Erro ao criar o arquivo '{nome_arquivo}': {e}")

def criar_arquivos_sequenciais(caminho, prefixo, inicio, fim):
    """Cria uma sequência de arquivos Python numerados no diretório especificado."""
    # Validação do intervalo
    if inicio > fim:
        inicio, fim = fim, inicio  # Inverte se início for maior que fim
        print(f"Aviso: Intervalo invertido para {inicio}-{fim}")
    
    for i in range(inicio, fim + 1):
        nome_arquivo = f"{prefixo}{i}"
        criar_arquivo_py(caminho, nome_arquivo)

def obter_entrada_usuario():
    """Obtém e valida a entrada do usuário."""
    while True:
        try:
            prefixo = input("Digite o prefixo para os nomes dos arquivos (ex: 'arquivo'): ").strip()
            inicio = int(input("Digite o número inicial da sequência: "))
            fim = int(input("Digite o número final da sequência: "))
            return prefixo, inicio, fim
        except ValueError:
            print("Erro: Por favor, digite números válidos para o início e fim.")

def main():
    print("=== Criador de Arquivos Python Sequenciais ===")
    
    # Seleciona o diretório
    diretorio = selecionar_diretorio()
    print(f"Os arquivos serão criados em: {diretorio}")
    
    # Obtém os parâmetros dos arquivos
    prefixo, inicio, fim = obter_entrada_usuario()
    
    # Cria os arquivos
    criar_arquivos_sequenciais(diretorio, prefixo, inicio, fim)

if __name__ == "__main__":
    main()