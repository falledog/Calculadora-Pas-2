import streamlit as st
st.header("Calculadora PAS 2", divider="rainbow")
matricula_especifica = (st.text_input("Insira seu número de matrícula:"))
try:
    num = int(matricula_especifica)
    matricula_especifica = num
except ValueError:
    st.write("")
# Abrir e ler o arquivo
with open("Notaspas2.txt", "r") as file:
    linhas = file.readlines()

# Criar uma lista para armazenar os usuários
candidatos = []

# Variáveis para calcular as médias
total_candidatos = 0
soma_escore1 = 0
soma_escore2 = 0
soma_total_escores = 0
soma_tipoD = 0
soma_redacao = 0
# Função para limpar e converter a string para float
def limpar_e_converter(valor):
    try:
        return float(valor.strip())  # Limpar espaços extras e converter para float
    except ValueError:
        return 0.0  # Retornar 0.0 caso o valor não seja válido

# Processar cada linha
for linha in linhas:
    dados = linha.strip().split(",")  # Remover espaços e dividir por vírgula
    matricula = int(dados[0])  # Número da matrícula
    nome = dados[1]  # Nome do usuário
    escoreparte1 = limpar_e_converter(dados[2])  # Limpar e converter para float
    escoreparte2 = limpar_e_converter(dados[3])  
    somatorio = limpar_e_converter(dados[4])  
    tipod = limpar_e_converter(dados[5])  
    redacao = limpar_e_converter(dados[6])  

    # Somar valores para cálculo da média
    total_candidatos += 1
    soma_escore1 += escoreparte1
    soma_escore2 += escoreparte2
    soma_total_escores += somatorio
    soma_tipoD += tipod
    soma_redacao += redacao

    # Adicionar os dados à lista
    candidatos.append({
        "matricula": matricula,
        "nome": nome,
        "escore bruto na parte 1": escoreparte1,
        "escore bruto na parte 2": escoreparte2,
        "somatório dos escores brutos nas partes 1 e 2": somatorio,
        "nota final nos itens do tipo D": tipod, 
        "nota redação": redacao
    })

# Calcular as médias
if total_candidatos > 0:
    media_escore1 = soma_escore1 / total_candidatos
    media_escore2 = soma_escore2 / total_candidatos
    media_total_escores = soma_total_escores / total_candidatos
    media_tipoD = soma_tipoD / total_candidatos
    media_redacao = soma_redacao / total_candidatos
# Encontrar o candidato específico
candidato_especifico = None
for candidato in candidatos:
    if candidato["matricula"] == matricula_especifica:
        candidato_especifico = candidato
        break

# Função para calcular a diferença percentual
def calcular_diferenca_percentual(candidato_valor, media_valor):
    if media_valor == 0:
        return 0  # Evitar divisão por zero
    return ((candidato_valor - media_valor) / media_valor) * 100

# Função para contar quantos candidatos têm um valor acima do candidato específico
def contar_candidatos_acima(candidato_valor, item):
    count = 0
    for candidato in candidatos:
        if candidato[item] > candidato_valor:
            count += 1
    return count
# Comparar os dados do candidato específico com as médias
if candidato_especifico: 
    st.markdown(f"\nResultado do candidato {candidato_especifico['nome']}")  
    # Exibir as diferenças percentuais para cada item
    escore1_diff = calcular_diferenca_percentual(candidato_especifico['escore bruto na parte 1'], media_escore1)
    escore2_diff = calcular_diferenca_percentual(candidato_especifico['escore bruto na parte 2'], media_escore2)
    somatorio_diff = calcular_diferenca_percentual(candidato_especifico['somatório dos escores brutos nas partes 1 e 2'], media_total_escores)
    tipoD_diff = calcular_diferenca_percentual(candidato_especifico['nota final nos itens do tipo D'], media_tipoD)
    redacao_diff = calcular_diferenca_percentual(candidato_especifico['nota redação'], media_redacao)
    st.header(" ", divider="violet")
    # Exibir resultados
    st.markdown(f"Escores da parte 1: {candidato_especifico['escore bruto na parte 1']} (Diferença: {escore1_diff:.2f}%) vs. Média: {media_escore1:.2f}")
    st.markdown(f"Escores da parte 2: {candidato_especifico['escore bruto na parte 2']} (Diferença: {escore2_diff:.2f}%) vs. Média: {media_escore2:.2f}")
    st.markdown(f"Somatório dos escores: {candidato_especifico['somatório dos escores brutos nas partes 1 e 2']} (Diferença: {somatorio_diff:.2f}%) vs. Média: {media_total_escores:.2f}")
    st.markdown(f"Nota final nos itens do tipo D: {candidato_especifico['nota final nos itens do tipo D']} (Diferença: {tipoD_diff:.2f}%) vs. Média: {media_tipoD:.2f}")
    st.markdown(f"Nota de redação: {candidato_especifico['nota redação']} (Diferença: {redacao_diff:.2f}%) vs. Média: {media_redacao:.2f}")
    
    # Contar quantos candidatos ficaram acima do candidato específico
    escore1_acima = contar_candidatos_acima(candidato_especifico['escore bruto na parte 1'], 'escore bruto na parte 1')
    escore2_acima = contar_candidatos_acima(candidato_especifico['escore bruto na parte 2'], 'escore bruto na parte 2')
    somatorio_acima = contar_candidatos_acima(candidato_especifico['somatório dos escores brutos nas partes 1 e 2'], 'somatório dos escores brutos nas partes 1 e 2')
    tipoD_acima = contar_candidatos_acima(candidato_especifico['nota final nos itens do tipo D'], 'nota final nos itens do tipo D')
    redacao_acima = contar_candidatos_acima(candidato_especifico['nota redação'], 'nota redação')
    st.header(" ", divider="green")
    # Exibir o ranking de candidatos acima
    st.markdown(f"\nRanking de candidatos acima de {candidato_especifico['nome']}")
    st.markdown(f"Escores da parte 1: {escore1_acima} candidatos acima")
    st.markdown(f"Escores da parte 2: {escore2_acima} candidatos acima")
    st.markdown(f"Somatório dos escores: {somatorio_acima} candidatos acima")
    st.markdown(f"Nota final nos itens do tipo D: {tipoD_acima} candidatos acima")
    st.markdown(f"Nota de redação: {redacao_acima} candidatos acima")
else:
    st.markdown(f"Candidato {matricula_especifica} não encontrado.")
