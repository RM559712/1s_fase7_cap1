import sys
import subprocess
import os
import math

# Ajuste estes caminhos para corresponder à sua instalação do R
R_VERSION = "R-4.4.1"  # Substitua pela sua versão exata do R
R_HOME = fr'C:\Program Files\R\{R_VERSION}'
R_BIN = fr'{R_HOME}\bin\x64'

os.environ['R_HOME'] = R_HOME
os.environ['PATH'] = f"{R_BIN};{os.environ['PATH']}"

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


required_modules = [
    'tabulate',
    'rpy2==3.5.1'
]

for module in required_modules:
    try:
        if '==' in module:
            __import__(module.split('==')[0])
        else:
            __import__(module)
    except ImportError:
        print(f'{module} não está instalado. Instalando...')
        install(module)
        print(f'{module} foi instalado com sucesso.')

from tabulate import tabulate
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr

# Ativar a conversão automática entre pandas e R dataframes
pandas2ri.activate()

# Importar bibliotecas R necessárias
base = importr('base')
stats = importr('stats')
graphics = importr('graphics')

areas = {'quadrado': None, 'retângulo': None, 'triângulo': None, 'círculo': None}

insumos = {
    'milho': {
        'Sementes': (22.5, 'kg/ha'),
        'Água': (525, 'mm'),
        'Fertilizantes': (125, 'kg/ha'),
        'Defensivos': ('Herbicidas e inseticidas', 'conforme necessidade'),
        'Período de Plantio': 'Setembro a novembro (safra verão)'
    },
    'soja': {
        'Sementes': (60, 'kg/ha'),
        'Água': (625, 'mm'),
        'Fertilizantes': (250, 'kg/ha'),
        'Defensivos': ('Herbicidas, fungicidas e inseticidas', 'conforme necessidade'),
        'Período de Plantio': 'Outubro a dezembro'
    },
    'cana': {
        'Mudas': (11, 'ton/ha'),
        'Água': (2000, 'mm'),
        'Fertilizantes': (500, 'kg/ha'),
        'Defensivos': ('Herbicidas e inseticidas', 'conforme necessidade'),
        'Período de Plantio': 'Janeiro a março'
    },
    'café': {
        'Mudas': (4500, 'mudas/ha'),
        'Água': (1500, 'mm'),
        'Fertilizantes': (300, 'kg/ha'),
        'Defensivos': ('Fungicidas e inseticidas', 'conforme necessidade'),
        'Período de Plantio': 'Outubro a fevereiro'
    },
    'arroz': {
        'Sementes': (110, 'kg/ha'),
        'Água': (575, 'mm'),
        'Fertilizantes': (250, 'kg/ha'),
        'Defensivos': ('Herbicidas e inseticidas', 'conforme necessidade'),
        'Período de Plantio': 'Outubro a dezembro'
    }
}


def calcular_area(tipo, valor1, valor2=None):
    if tipo == 'quadrado':
        area = valor1 ** 2
    elif tipo == 'retângulo':
        area = valor1 * valor2
    elif tipo == 'triângulo':
        area = (valor1 * valor2) / 2
    elif tipo == 'círculo':
        area = math.pi * (valor1 ** 2)
    else:
        return None
    return area, area / 10000


def exibir_insumos(area_hectares):
    print(f'\nÁrea em hectares: {area_hectares:.4f} ha')

    headers = ['Insumo', 'Quantidade por Hectare', 'Total', 'Unidade']

    for cultura, dados in insumos.items():
        print(f'\nInsumos para {cultura.capitalize()}:')
        print(f'Período de Plantio: {dados["Período de Plantio"]}')

        tabela_insumos = []
        for insumo, valor in dados.items():
            if insumo != 'Período de Plantio':
                if isinstance(valor, tuple):
                    quantidade, unidade = valor
                    total = quantidade * area_hectares if isinstance(quantidade, (int, float)) else 'N/A'
                    total_str = f'{total:.2f}' if isinstance(total, (int, float)) else total
                    tabela_insumos.append([insumo, f'{quantidade}', total_str, unidade])
                else:
                    tabela_insumos.append([insumo, valor, 'N/A', 'N/A'])

        print(tabulate(tabela_insumos, headers=headers, tablefmt='grid'))
        print('\n' + '-' * 50)


def menu_calcular_area():
    while True:
        print("\nCalcular Área de Plantio:")
        print("1. Quadrado")
        print("2. Retângulo")
        print("3. Triângulo")
        print("4. Círculo")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '5':
            return

        if opcao == '1':
            lado = float(input("Digite o lado do quadrado (em metros): "))
            areas['quadrado'] = calcular_area('quadrado', lado)
        elif opcao == '2':
            largura = float(input("Digite a largura do retângulo (em metros): "))
            comprimento = float(input("Digite o comprimento do retângulo (em metros): "))
            areas['retângulo'] = calcular_area('retângulo', largura, comprimento)
        elif opcao == '3':
            base = float(input("Digite a base do triângulo (em metros): "))
            altura = float(input("Digite a altura do triângulo (em metros): "))
            areas['triângulo'] = calcular_area('triângulo', base, altura)
        elif opcao == '4':
            raio = float(input("Digite o raio do círculo (em metros): "))
            areas['círculo'] = calcular_area('círculo', raio)
        else:
            print("Opção inválida.")
            continue

        area, area_hectares = areas[list(areas.keys())[int(opcao) - 1]]
        print(f"\nÁrea calculada: {area:.2f} m²")
        exibir_insumos(area_hectares)


def menu_atualizar_area():
    while True:
        print("\nAtualizar Área de Plantio:")
        print("1. Quadrado")
        print("2. Retângulo")
        print("3. Triângulo")
        print("4. Círculo")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '5':
            return

        tipo = list(areas.keys())[int(opcao) - 1]
        if areas[tipo] is None:
            print(f"A área de {tipo} não foi cadastrada.")
            continue

        if opcao == '1':
            lado = float(input("Digite o novo lado do quadrado (em metros): "))
            areas['quadrado'] = calcular_area('quadrado', lado)
        elif opcao == '2':
            largura = float(input("Digite a nova largura do retângulo (em metros): "))
            comprimento = float(input("Digite o novo comprimento do retângulo (em metros): "))
            areas['retângulo'] = calcular_area('retângulo', largura, comprimento)
        elif opcao == '3':
            base = float(input("Digite a nova base do triângulo (em metros): "))
            altura = float(input("Digite a nova altura do triângulo (em metros): "))
            areas['triângulo'] = calcular_area('triângulo', base, altura)
        elif opcao == '4':
            raio = float(input("Digite o novo raio do círculo (em metros): "))
            areas['círculo'] = calcular_area('círculo', raio)
        else:
            print("Opção inválida.")
            continue

        area, area_hectares = areas[tipo]
        print(f"\nÁrea atualizada: {area:.2f} m²")
        exibir_insumos(area_hectares)


def deletar_areas():
    while True:
        print("\nÁreas cadastradas:")
        areas_cadastradas = [tipo for tipo, valor in areas.items() if valor is not None]
        for i, tipo in enumerate(areas_cadastradas, 1):
            print(f"{i}. {tipo}")
        print(f"{len(areas_cadastradas) + 1}. Deletar todas")
        print(f"{len(areas_cadastradas) + 2}. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")
        if opcao == str(len(areas_cadastradas) + 2):
            return
        elif opcao == str(len(areas_cadastradas) + 1):
            for tipo in areas:
                areas[tipo] = None
            print("Todas as áreas foram deletadas.")
        elif opcao.isdigit() and 1 <= int(opcao) <= len(areas_cadastradas):
            tipo = areas_cadastradas[int(opcao) - 1]
            areas[tipo] = None
            print(f"Área de {tipo} foi deletada.")
        else:
            print("Opção inválida.")


def gerar_relatorio_r():
    # Configurar a codificação do R para UTF-8
    robjects.r('Sys.setlocale(category = "LC_ALL", locale = "Portuguese")')
    robjects.r('options(encoding = "UTF-8")')

    # Criar dataframe R com os dados das culturas (sem acentos)
    r_df = robjects.DataFrame({
        'Cultura': robjects.StrVector(['Milho', 'Soja', 'Cana', 'Cafe', 'Arroz']),
        'Sementes': robjects.FloatVector(
            [dados['Sementes'][0] if 'Sementes' in dados else dados['Mudas'][0] for dados in insumos.values()]),
        'Agua': robjects.FloatVector([dados['Água'][0] for dados in insumos.values()]),
        'Fertilizantes': robjects.FloatVector([dados['Fertilizantes'][0] for dados in insumos.values()])
    })

    # Calcular médias em R
    r_code = """
    function(df) {
        medias <- colMeans(df[, c("Sementes", "Agua", "Fertilizantes")])
        print(medias)

        # Criar gráficos ASCII
        for (col in c("Sementes", "Agua", "Fertilizantes")) {
            cat("\nGrafico de", col, ":\n")
            valores <- df[[col]]
            max_valor <- max(valores)
            escala <- 50 / max_valor
            for (i in 1:nrow(df)) {
                barra <- paste(rep("*", round(valores[i] * escala)), collapse="")
                cat(sprintf("%-10s [%8.2f]: %s\n", df$Cultura[i], valores[i], barra))
            }
        }
    }
    """
    r_func = robjects.r(r_code)

    try:
        r_func(r_df)
    except Exception as e:
        print(f"Erro ao gerar relatório R: {e}")
        print("Tentando exibir dados em formato alternativo...")

        # Exibição alternativa em Python
        print("\nMédias dos Insumos:")
        medias = {col: sum(r_df.rx2(col)) / len(r_df.rx2(col)) for col in ['Sementes', 'Agua', 'Fertilizantes']}
        for insumo, media in medias.items():
            print(f"{insumo}: {media:.2f}")

        print("\nDados por Cultura:")
        for i, cultura in enumerate(r_df.rx2('Cultura')):
            print(f"\n{cultura}:")
            for col in ['Sementes', 'Agua', 'Fertilizantes']:
                valor = r_df.rx2(col)[i]
                print(f"  {col}: {valor:.2f}")

    print("\nRelatório gerado com sucesso.")


def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Calcular Área de Plantio")
        print("2. Atualizar Área de Plantio")
        print("3. Deletar Áreas Cadastradas")
        print("4. Gerar Relatório R")
        print("5. Sair do Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_calcular_area()
        elif opcao == '2':
            menu_atualizar_area()
        elif opcao == '3':
            deletar_areas()
        elif opcao == '4':
            gerar_relatorio_r()
        elif opcao == '5':
            confirmacao = input("Tem certeza que deseja sair? (S/N): ")
            if confirmacao.lower() == 's':
                print("Saindo do programa. Obrigado!")
                break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()