ARQUIVOS_DADOS = 'data/vendas.csv'
DADOS_PROCESSADOS = []

def carregar_e_limpar_dados(nome_arquivo):
    try:
        with open (nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            cabecalho = linhas[0].strip().split(',')
            dados_brutos = linhas[1:]

            for linha in dados_brutos:
                valores = linha.strip().split(',')

                if len(valores) == len(cabecalho):
                    registro = {}

                    registro[cabecalho[0]] = int(valores[0])
                    registro[cabecalho[1]] = valores[1]
                    registro[cabecalho[2]] = valores[2]
                    
                    try:
                        registro[cabecalho[3]] = int(valores[3])
                        registro[cabecalho[4]] = float(valores[4])
                        registro[cabecalho[5]] = valores[5]

                        registro['Venda_Total'] = registro['Quantidade'] * registro['Preco_Unitario']

                        DADOS_PROCESSADOS.append(registro)

                    except ValueError:
                        print(f'ERRO: Pulando linha com valores não numéricos: {linha.strip()}')
                        continue
            print(f'Dados carregados e limpos: {len(DADOS_PROCESSADOS)} registros.')
    except FileNotFoundError:
        print(f'ERRO: Arquivo não encontrado em {nome_arquivo}.')

carregar_e_limpar_dados(ARQUIVOS_DADOS)