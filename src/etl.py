import pandas as pd
import os

# 1. Garante que a pasta 'dados' existe no nível acima
if not os.path.exists('../dados'):
    os.makedirs('../dados')
    print("Pasta 'dados' criada.")

# 2. Carrega o arquivo original
# Removido 'low_memory' para não conflitar com o engine='python'
try:
    print("Carregando base de dados...")
    df = pd.read_csv(
        '../dados/global_power_plant_database.csv',
        sep=None,
        engine='python',
        encoding='latin1',
        on_bad_lines='skip'
    )
    print("Arquivo carregado com sucesso!")
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")
    df = None # Define como None para evitar o NameError caso falhe

# Só continua se o 'df' foi criado com sucesso
if df is not None:
    # 3. Lista de traduções das colunas
    traducoes = {
        'country_long': 'Pais',
        'name': 'Nome_da_Usina',
        'capacity_mw': 'Capacidade_MW',
        'latitude': 'Latitude',
        'longitude': 'Longitude',
        'primary_fuel': 'Tipo_de_Combustivel',
        'owner': 'Proprietario'
    }

    # 4. Seleciona e renomeia as colunas
    # Verificamos se as colunas existem antes de filtrar
    colunas_presentes = [col for col in traducoes.keys() if col in df.columns]
    df_tratado = df[colunas_presentes].rename(columns=traducoes).copy()

    # 5. CORREÇÃO DE ESCALA
    # Convertendo para numerico primeiro para garantir
    df_tratado['Latitude'] = pd.to_numeric(df_tratado['Latitude'], errors='coerce') / 10000
    df_tratado['Longitude'] = pd.to_numeric(df_tratado['Longitude'], errors='coerce') / 10000

    # 6. Elimina valores nulos
    df_tratado.dropna(subset=['Pais', 'Capacidade_MW', 'Latitude', 'Longitude'], inplace=True)

    # 7. Dicionário para traduzir os tipos de combustíveis
    dicionario_combustivel = {
        'Hydro': 'Hidrica',
        'Solar': 'Solar',
        'Gas': 'Gas Natural',
        'Coal': 'Carvao',
        'Wind': 'Eolica',
        'Oil': 'Oleo',
        'Nuclear': 'Nuclear'
    }
    df_tratado['Tipo_de_Combustivel'] = df_tratado['Tipo_de_Combustivel'].map(dicionario_combustivel).fillna(df_tratado['Tipo_de_Combustivel'])

    # 8. Salva o arquivo final limpo
    caminho_saida = '../dados/usinas_limpas_faculdade.csv'
    df_tratado.to_csv(caminho_saida, index=False, encoding='utf-8-sig')

    print(f"Processo concluído! Arquivo salvo em: {caminho_saida}")
else:
    print("O processo foi interrompido porque o arquivo não pôde ser lido.")