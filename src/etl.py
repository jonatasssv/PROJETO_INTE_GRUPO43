import pandas as pd

df = pd.read_csv('../data/global_power_plant_database.csv', low_memory = False)

# 2. Criada uma lista de traduções
traducoes = {
    'country_long': 'Pais',
    'name': 'Nome_da_Usina',
    'capacity_mw': 'Capacidade_MW',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'primary_fuel': 'Tipo_de_Combustivel',
    'owner': 'Proprietario'
}

# 3. Arquivo renomeado
df_tratado = df[list(traducoes.keys())].rename(columns=traducoes)

# 4. Aqui foi eleiminado os arquivos nulos
df_tratado.dropna(subset=['Pais', 'Capacidade_MW', 'Latitude', 'Longitude'], inplace=True)

# 5. Criada uma lista de tradução para combustíveis
dicionario_combustivel = {
    'Hydro': 'Hidrica',
    'Solar': 'Solar',
    'Gas': 'Gas Natural',
    'Coal': 'Carvao',
    'Wind': 'Eolica',
    'Nuclear': 'Nuclear',
    'Oil': 'Petroleo',
    'Waste': 'Residuos',
    'Biomass': 'Biomassa'
}
 # 6. Combustíveis renomeados
df_tratado['Tipo_de_Combustivel'] = df_tratado['Tipo_de_Combustivel'].map(dicionario_combustivel).fillna(df_tratado['Tipo_de_Combustivel'])

df_tratado.to_csv('usinas_limpas_faculdade.csv', index=False, encoding='utf-8-sig')

print(f"Sucesso! O arquivo agora tem {df_tratado.shape[0]} linhas prontas para o Power BI.")

# Cria uma amostra pequena para visualização rápida no Excel
df_tratado.head(100).to_csv('../data/amostra_usinas.csv', index=False, encoding='utf-8-sig')

