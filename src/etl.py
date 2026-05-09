import pandas as pd
import os

# 1. Garante que a pasta 'dados' existe antes de salvar
if not os.path.exists('dados'):
    os.makedirs('dados')

# 2. Carrega o arquivo original
# Ajustei o caminho para buscar dentro de 'dados/' conforme nossa organização
df = pd.read_csv('dados/global_power_plant_database.csv', low_memory=False)

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
df_tratado = df[list(traducoes.keys())].rename(columns=traducoes).copy()

# 5. CORREÇÃO DE ESCALA: Transforma inteiros em decimais para o mapa
# Como vimos que o Power BI/Excel "comeu" os pontos, dividimos por 10.000
df_tratado['Latitude'] = df_tratado['Latitude'] / 10000
df_tratado['Longitude'] = df_tratado['Longitude'] / 10000

# 6. Elimina valores nulos em colunas críticas
df_tratado.dropna(subset=['Pais', 'Capacidade_MW', 'Latitude', 'Longitude'], inplace=True)

# 7. Dicionário para traduzir os tipos de combustíveis
dicionario_combustivel = {
    'Hydro': 'Hidrica',
    'Solar': 'Solar',
    'Gas': 'Gas Natural',
    'Coal': 'Carvao',
    'Wind': 'Eolica',
    'Nuclear': 'Nuclear',
    'Oil': 'Petroleo',
    'Waste': 'Residuos',
    'Biomass': 'Biomassa',
    'Geothermal': 'Geotermica'
}

# 8. Traduz os combustíveis e mantém o original caso não esteja no dicionário
df_tratado['Tipo_de_Combustivel'] = df_tratado['Tipo_de_Combustivel'].map(dicionario_combustivel).fillna(df_tratado['Tipo_de_Combustivel'])

# 9. Salva o arquivo final tratado na pasta 'dados'
# O encoding utf-8-sig garante que o Excel abra os acentos corretamente
df_tratado.to_csv('dados/usinas_limpas_faculdade.csv', index=False, encoding='utf-8-sig')

print(f"Sucesso! O arquivo agora tem {df_tratado.shape[0]} linhas prontas para o Power BI.")
print("Arquivo salvo em: dados/usinas_limpas_faculdade.csv")

# 10. Cria uma amostra pequena para visualização rápida
df_tratado.head(100).to_csv('dados/amostra_usinas.csv', index=False, encoding='utf-8-sig')

