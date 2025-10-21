ARQUIVOS_DADOS = 'data/vendas.csv'
DADOS_PROCESSADOS = [] #Lista para armazenar os dicionários processados

def carregar_e_limpar_dados(nome_arquivo):
    """Lê o arquivo CSV e converte cada linha em um dicionário de dados limpos."""
    try:
        with open (nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            cabecalho = linhas[0].strip().split(',')
            dados_brutos = linhas[1:]

            for linha in dados_brutos:
                valores = linha.strip().split(',')

                if len(valores) == len(cabecalho):
                    registro = {}
                    # Cria um dicionário para o registro

                    registro[cabecalho[0]] = int(valores[0]) # ID_Venda
                    registro[cabecalho[1]] = valores[1] # Produto
                    registro[cabecalho[2]] = valores[2] # Categoria
                    
                    # Converte para tipos numéricos
                    try:
                        registro[cabecalho[3]] = int(valores[3]) # Quantidade
                        registro[cabecalho[4]] = float(valores[4]) # Preco_Unitario
                        registro[cabecalho[5]] = valores[5] # Data

                        # Adiciona o campo calculado: Venda Total
                        registro['Venda_Total'] = registro['Quantidade'] * registro['Preco_Unitario']

                        DADOS_PROCESSADOS.append(registro)

                    except ValueError:
                        print(f'ERRO: Pulando linha com valores não numéricos: {linha.strip()}')
                        continue
            print(f'Dados carregados e limpos: {len(DADOS_PROCESSADOS)} registros.')
    except FileNotFoundError:
        print(f'ERRO: Arquivo não encontrado em {nome_arquivo}.')

# Chamada da função de carregamento
carregar_e_limpar_dados(ARQUIVOS_DADOS)

def calcular_vendas_totais(dados):
    """Calcula o valor total de todas as vendas."""
    total_geral = 0.0
    for registro in dados:
        total_geral += registro['Venda_Total']
    return total_geral

def analisar_vendas_por_categoria(dados):
    """Agrupa as vendas por Categoria e calcula a soma por grupo."""
    vendas_por_categoria = {}

    for registro in dados:
        categoria = registro['Categoria']
        venda_total  = registro['Venda_Total']

        # Usa dicionário para agregar: se a chave não existe, inicializa com 0
        if categoria in vendas_por_categoria:
            vendas_por_categoria[categoria] += venda_total

        else:
            vendas_por_categoria[categoria] = venda_total
        
    return vendas_por_categoria

def apresentar_resultados(total_geral, vendas_por_categoria):
    """Imprime os resultados da análise de forma clara."""
    print('\n' + '='*50)
    print('Relatório de Análise de Vendas Simples')
    print('='*50)

    # Apresenta o Total Geral
    print(f'\nTotal Geral de Vendas: R$ {total_geral:,.2f}')

    # Apresenta Vendas por Categoria
    print('\n---Vendas por Categoria---')
    for categoria, total in vendas_por_categoria.items(): 
        porcentagem = (total / total_geral) * 100
        print(f'| {categoria:<15}: R$ {total:10,.2f} ({porcentagem:.1f}%)')

if __name__  == '__main__':
    # Garante que só executa se o carregamento foi bem-sucedido
    if DADOS_PROCESSADOS: 
        # 1. Calcular o total geral
        total_vendas = calcular_vendas_totais(DADOS_PROCESSADOS)

         # 2. Analisar vendas por categoria
        vendas_categoria = analisar_vendas_por_categoria(DADOS_PROCESSADOS)

        # 3. Apresentar
        apresentar_resultados(total_vendas, vendas_categoria)