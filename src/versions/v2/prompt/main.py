import datetime
import os
import sys
import time

# > Importante: A definição abaixo referente ao diretório raiz deve ser efetuada antes das importações de arquivos do sistema.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from custom.helper import Helper
from custom.openweather import OpenWeather
from models.database.database import Database
from models.f2_c6_crop import F2C6Crop

# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes à estrutura do sistema
# ---------------------------------------------------------------------------------------------------------------

"""
Método responsável por executar teste de conexão com o banco de dados
"""
def test_connection_by_database():

    object_database = Database()
    object_database.test_connection_by_database()


"""
Método responsável por retornar o diretório de execução do sistema
"""
def get_current_path_dir() -> str:

    return os.path.dirname(os.path.dirname(__file__))


"""
Método responsável por executar o "reset" do bloco de comandos
"""
def reset_commands():

    os.system('cls')
    os.system('clear')


"""
Método responsável por recarregar o sistema
"""
def require_reload_system():

    input(f'\nPressione <enter> para voltar ao menu principal...')
    init_system()


"""
Método responsável por exibir uma mensagem para execução de uma determinada ação
"""
def loading(str_message: str = 'Processando, por favor aguarde...', int_seconds: int = 5, bool_reset: bool = True):

    if bool_reset == True:
        show_head_system()

    print(f'\n{str_message}', end='')
    time.sleep(int_seconds)


"""
Método responsável pela exibição do cabeçalho do sistema
"""
def show_head_system():

    reset_commands()
    
    print(f'█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████')
    print(f'█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░████████████████░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█')
    print(f'█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█')
    print(f'█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░████████████████░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█')
    print(f'█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░████████████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████')
    print(f'█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█░░░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█')
    print(f'█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█')
    print(f'█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░██░░▄▀░░█░░░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█')
    print(f'█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░████████████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████████░░▄▀░░█')
    print(f'█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░████████████████░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█')
    print(f'█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█')
    print(f'█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░████████████████░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█')
    print(f'█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████')


"""
Método responsável por parametrizar a visualização para uma nova estapa de módulo
"""
def init_step():

    show_head_system()

    print('')


"""
Método responsável por retornar as opções de menu do sistema

Return: list
"""
def get_system_menu_options() -> list:

    return [
        {
            'code': 1,
            'title': 'Culturas',
            'action': action_crops
        },{
            'code': 2,
            'title': 'Análises e alertas para plantio',
            'action': action_planting_alert
        },{
            'code': 3,
            'title': 'Sair',
            'action': action_exit
        }
    ]


"""
Método responsável por retornar os códigos das opções de menu do sistema

Return: list
"""
def get_system_menu_options_codes() -> list:

    list_return = []

    list_menu_options = get_system_menu_options()

    for dict_menu_option in list_menu_options:
        list_return.append(dict_menu_option['code'])

    return list_return


"""
Método responsável pela validação do parâmetro "Opção do menu"

Return: str
"""
def validate_system_menu_option() -> str:

    str_return = input(f'Digite uma opção: ')

    while True:

        try:

            if str_return.strip() == '':
                raise Exception('Deve ser definida uma opção válida.')

            if Helper.is_int(str_return) == False: 
                raise Exception('A opção informada deve ser numérica.')

            if int(str_return) not in get_system_menu_options_codes(): 
                raise Exception('A opção informada deve representar um dos menus disponíveis.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            str_return = input()

    return str_return


"""
Método responsável por solicitar a opção do sistema que deverá ser executada
"""
def require_system_menu_option():

    str_option = validate_system_menu_option()

    list_menu_options = get_system_menu_options()

    for dict_menu_option in list_menu_options:
        if dict_menu_option['code'] == int(str_option):
            dict_menu_option['action']()


"""
Método responsável por executar a inicialização do sistema
"""
def init_system():

    try:

        init_step()

        test_connection_by_database()

        list_menu_options = get_system_menu_options()

        for dict_menu_option in list_menu_options:
            print(f'{dict_menu_option['code']}. {dict_menu_option['title']}')

        print('')

        require_system_menu_option()

    except Exception as error:

        print(f'> Ocorreu o seguinte erro: {error}')
        require_reload_system()


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes a opção "Culturas"
# ---------------------------------------------------------------------------------------------------------------

"""
Método responsável por verificar se existem culturas cadastradas
"""
def validate_exists_crops():

    object_f2c6_crop = F2C6Crop()
    bool_exists_data = object_f2c6_crop.validate_exists_data()

    if bool_exists_data == False:
        raise Exception('Não existem culturas cadastradas.')


"""
Método responsável por recarregar o módulo "Culturas"
"""
def require_reload_crops():

    input(f'\nPressione <enter> para voltar ao menu do módulo "Culturas"...')
    action_crops()


"""
Método responsável por retornar as opções de menu do módulo "Culturas"

Return: list
"""
def get_crops_menu_options() -> list:

    return [
        {
            'code': 1,
            'title': 'Visualizar cadastros',
            'action': action_crops_list
        },{
            'code': 2,
            'title': 'Cadastrar',
            'action': action_crops_insert
        },{
            'code': 3,
            'title': 'Editar',
            'action': action_crops_update
        },{
            'code': 4,
            'title': 'Excluir',
            'action': action_crops_delete
        },{
            'code': 5,
            'title': 'Voltar ao menu principal',
            'action': init_system
        }
    ]


"""
Método responsável por retornar os códigos das opções de menu do módulo "Culturas"

Return: list
"""
def get_crops_menu_options_codes() -> list:

    list_return = []

    list_menu_options = get_crops_menu_options()

    for dict_menu_option in list_menu_options:
        list_return.append(dict_menu_option['code'])

    return list_return


"""
Método responsável pela validação do parâmetro "Opção do menu" do módulo "Culturas"

Return: str
"""
def validate_crops_menu_option() -> str:

    str_return = input(f'Digite uma opção: ')

    while True:

        try:

            if str_return.strip() == '':
                raise Exception('Deve ser definida uma opção válida.')

            if Helper.is_int(str_return) == False: 
                raise Exception('A opção informada deve ser numérica.')

            if int(str_return) not in get_crops_menu_options_codes(): 
                raise Exception('A opção informada deve representar um dos menus disponíveis.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            str_return = input()

    return str_return


"""
Método responsável por solicitar a opção do sistema que deverá ser executada
"""
def require_crops_menu_option():

    str_option = validate_crops_menu_option()

    list_menu_options = get_crops_menu_options()

    for dict_menu_option in list_menu_options:
        if dict_menu_option['code'] == int(str_option):
            dict_menu_option['action']()


"""
Método responsável pela formatação de visualização do ID do módulo "Culturas"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def format_data_view_crops_id(dict_data: dict = {}) -> str:

    str_return = 'ID: '
    str_return += f'{dict_data['CRP_ID']}' if 'CRP_ID' in dict_data and type(dict_data['CRP_ID']) != None and Helper.is_int(dict_data['CRP_ID']) == True else 'N/I'

    return str_return


"""
Método responsável pela validação do parâmetro "ID"

Return: int
"""
def validate_crops_id() -> int:

    int_return = input(f'Informe o ID da cultura: ')

    while True:

        try:

            if int_return.strip() == '':
                raise Exception('Deve ser informado um ID válido.')

            if Helper.is_int(int_return) == False: 
                raise Exception('O conteúdo informado deve ser numérico.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            int_return = input()

    return int(int_return)


"""
Método responsável pela formatação de visualização do nome do módulo "Culturas"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def format_data_view_crops_name(dict_data: dict = {}) -> str:

    str_return = 'Nome: '
    str_return += f'{dict_data['CRP_NAME'].strip()}' if 'CRP_NAME' in dict_data and type(dict_data['CRP_NAME']) != None and type(dict_data['CRP_NAME']) == str else 'N/I'

    return str_return


"""
Método responsável pela validação do parâmetro "Nome"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def validate_crops_name(dict_data: dict = {}) -> str:

    bool_is_update = ('CRP_ID' in dict_data and type(dict_data['CRP_ID']) == int)

    str_label = f'Importante: Caso deseje manter o nome atual ( abaixo ), basta ignorar o preenchimento.\n{format_data_view_crops_name(dict_data)}\n' if bool_is_update == True else ''
    str_label += f'Informe o nome da cultura: '
    str_return = input(f'{str_label}')

    object_f2c6_crop = F2C6Crop()

    while True:

        try:

            if bool_is_update == False and str_return.strip() == '':
                raise Exception('Deve ser informado um nome válido.')

            if bool_is_update == False and type(str_return) != str: 
                raise Exception('O conteúdo informado deve ser texto.')

            if str_return.strip() != '':

                list_params_validate = [

                    {'str_column': 'LOWER(CRP_NAME)', 'str_type_where': '=', 'value': str_return.lower().strip()},
                    F2C6Crop.get_params_to_active_data()

                ]

                if bool_is_update == True:

                    list_params_validate.append({'str_column': 'CRP_ID', 'str_type_where': '!=', 'value': dict_data['CRP_ID']})

                dict_crop = object_f2c6_crop.set_where(list_params_validate).get_one()

                if type(dict_crop) == dict:
                    raise Exception(f'Já existe um registro cadastrado com o nome "{str_return.strip()}".')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            str_return = input()

    return str(str_return.strip())


"""
Método responsável pela formatação de visualização da temperatura do módulo "Culturas"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def format_data_view_crops_temp(dict_data: dict = {}) -> str:

    str_return = None
    list_labels = []

    if 'CRP_TEMP_MIN' in dict_data and type(dict_data['CRP_TEMP_MIN']) != None and Helper.is_float(dict_data['CRP_TEMP_MIN']) == True:
        list_labels.append(f'Mínimo de {dict_data['CRP_TEMP_MIN']}°C')

    if 'CRP_TEMP_MAX' in dict_data and type(dict_data['CRP_TEMP_MAX']) != None and Helper.is_float(dict_data['CRP_TEMP_MAX']) == True:
        list_labels.append(f'Máximo de {dict_data['CRP_TEMP_MAX']}°C')

    str_return = 'Temperatura ideal: '
    str_return += f'{' | ' . join(list_labels)}' if len(list_labels) > 0 else 'N/I'

    return str_return


"""
Método responsável pela validação dos parâmetros "temperatura mínima" e "temperatura máxima"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: dict
"""
def validate_crops_temp(dict_data: dict = {}) -> dict:

    dict_return = {'float_crp_temp_min': None, 'float_crp_temp_max': None}

    bool_is_update = ('CRP_ID' in dict_data and type(dict_data['CRP_ID']) == int)

    print('> Temperatura')
    print('A temperatura será exibida no formato [valor]°C ( ex.: 12°C, 21°C, etc. )')
    print('')

    if bool_is_update == True:
        print(f'Importante: Caso deseje manter os valores atuais ( abaixo ), basta ignorar os preenchimentos.\n{format_data_view_crops_temp(dict_data)}\n')

    # ----------------
    # Parâmetro mínimo
    # ----------------

    float_crp_temp_min = input(f'Caso exista, informe a temperatura mínima para plantio em formato numérico ( ex.: 123, 123.45 ou 123,45 ): ')

    while True:

        try:

            if float_crp_temp_min.strip() != '':

                if ',' in float_crp_temp_min:
                    float_crp_temp_min = float_crp_temp_min.replace(',', '.')

                if Helper.is_float(float_crp_temp_min) == False and Helper.is_int(float_crp_temp_min) == False:
                    raise Exception('O conteúdo informado deve ser numérico ( ex.: 123, 123.45 ou 123,45 ).')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            float_crp_temp_min = input()

    if float_crp_temp_min.strip() != '':
        dict_return['float_crp_temp_min'] = float(float_crp_temp_min)

    # ----------------
    # Parâmetro máximo
    # ----------------

    print('')

    float_crp_temp_max = input(f'Caso exista, informe a temperatura máxima para plantio em formato numérico ( ex.: 123, 123.45 ou 123,45 ): ')

    while True:

        try:

            if float_crp_temp_max.strip() != '':

                if ',' in float_crp_temp_max:
                    float_crp_temp_max = float_crp_temp_max.replace(',', '.')

                if Helper.is_float(float_crp_temp_max) == False and Helper.is_int(float_crp_temp_max) == False:
                    raise Exception('O conteúdo informado deve ser numérico ( ex.: 123, 123.45 ou 123,45 ).')

                if type(dict_return['float_crp_temp_min']) != type(None):

                    if float(float_crp_temp_max) <= dict_return['float_crp_temp_min']:
                        raise Exception(f'O valor máximo deve ser maior que o valor mínimo.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            float_crp_temp_max = input()

    if float_crp_temp_max.strip() != '':
        dict_return['float_crp_temp_max'] = float(float_crp_temp_max)

    return dict_return


"""
Método responsável pela formatação de visualização da umidade do módulo "Culturas"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def format_data_view_crops_humidity(dict_data: dict = {}) -> str:

    str_return = None
    list_labels = []

    if 'CRP_HUMIDITY_MIN' in dict_data and type(dict_data['CRP_HUMIDITY_MIN']) != None and Helper.is_float(dict_data['CRP_HUMIDITY_MIN']) == True:
        list_labels.append(f'Mínimo de {dict_data['CRP_HUMIDITY_MIN']}%')

    if 'CRP_HUMIDITY_MAX' in dict_data and type(dict_data['CRP_HUMIDITY_MAX']) != None and Helper.is_float(dict_data['CRP_HUMIDITY_MAX']) == True:
        list_labels.append(f'Máximo de {dict_data['CRP_HUMIDITY_MAX']}%')

    str_return = 'Umidade ideal: '
    str_return += f'{' | ' . join(list_labels)}' if len(list_labels) > 0 else 'N/I'

    return str_return


"""
Método responsável pela validação dos parâmetros "umidade mínima" e "umidade máxima"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: dict
"""
def validate_crops_humidity(dict_data: dict = {}) -> dict:

    dict_return = {'float_crp_humidity_min': None, 'float_crp_humidity_max': None}

    print('> Umidade')
    print('A umidade será exibida no formato [valor]% ( ex.: 12%, 21%, etc. )')
    print('')

    bool_is_update = ('CRP_ID' in dict_data and type(dict_data['CRP_ID']) == int)

    if bool_is_update == True:
        print(f'Importante: Caso deseje manter os valores atuais ( abaixo ), basta ignorar os preenchimentos.\n{format_data_view_crops_humidity(dict_data)}\n')

    # ----------------
    # Parâmetro mínimo
    # ----------------

    float_crp_humidity_min = input(f'Caso exista, informe a umidade mínima para plantio em formato numérico ( ex.: 123, 123.45 ou 123,45 ): ')

    while True:

        try:

            if float_crp_humidity_min.strip() != '':

                if ',' in float_crp_humidity_min:
                    float_crp_humidity_min = float_crp_humidity_min.replace(',', '.')

                if Helper.is_float(float_crp_humidity_min) == False and Helper.is_int(float_crp_humidity_min) == False:
                    raise Exception('O conteúdo informado deve ser numérico ( ex.: 123, 123.45 ou 123,45 ).')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            float_crp_humidity_min = input()

    if float_crp_humidity_min.strip() != '':
        dict_return['float_crp_humidity_min'] = float(float_crp_humidity_min)

    # ----------------
    # Parâmetro máximo
    # ----------------

    print('')

    float_crp_humidity_max = input(f'Caso exista, informe a umidade máxima para plantio em formato numérico ( ex.: 123, 123.45 ou 123,45 ): ')

    while True:

        try:

            if float_crp_humidity_max.strip() != '':

                if ',' in float_crp_humidity_max:
                    float_crp_humidity_max = float_crp_humidity_max.replace(',', '.')

                if Helper.is_float(float_crp_humidity_max) == False and Helper.is_int(float_crp_humidity_max) == False:
                    raise Exception('O conteúdo informado deve ser numérico ( ex.: 123, 123.45 ou 123,45 ).')

                if type(dict_return['float_crp_humidity_min']) != type(None):

                    if float(float_crp_humidity_max) <= dict_return['float_crp_humidity_min']:
                        raise Exception(f'O valor máximo deve ser maior que o valor mínimo.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            float_crp_humidity_max = input()

    if float_crp_humidity_max.strip() != '':
        dict_return['float_crp_humidity_max'] = float(float_crp_humidity_max)

    return dict_return


"""
Método responsável pela formatação de visualização da velocidade do vento do módulo "Culturas"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def format_data_view_crops_wind_speed(dict_data: dict = {}) -> str:

    str_return = None
    list_labels = []

    if 'CRP_WIND_SPEED_MIN' in dict_data and type(dict_data['CRP_WIND_SPEED_MIN']) != None and Helper.is_float(dict_data['CRP_WIND_SPEED_MIN']) == True:
        list_labels.append(f'Mínimo de {dict_data['CRP_WIND_SPEED_MIN']} m/s')

    if 'CRP_WIND_SPEED_MAX' in dict_data and type(dict_data['CRP_WIND_SPEED_MAX']) != None and Helper.is_float(dict_data['CRP_WIND_SPEED_MAX']) == True:
        list_labels.append(f'Máximo de {dict_data['CRP_WIND_SPEED_MAX']} m/s')

    str_return = 'Velocidade do vento ideal: '
    str_return += f'{' | ' . join(list_labels)}' if len(list_labels) > 0 else 'N/I'

    return str_return


"""
Método responsável pela validação dos parâmetros "velocidade do vento mínima" e "velocidade do vento máxima"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: dict
"""
def validate_crops_wind_speed(dict_data: dict = {}) -> dict:

    dict_return = {'float_crp_wind_speed_min': None, 'float_crp_wind_speed_max': None}

    print('> Velocidade do vento')
    print('A velocidade do vento será exibida no formato [valor] m/s ( ex.: 12 m/s, 21 m/s, etc. )')
    print('')

    bool_is_update = ('CRP_ID' in dict_data and type(dict_data['CRP_ID']) == int)

    if bool_is_update == True:
        print(f'Importante: Caso deseje manter os valores atuais ( abaixo ), basta ignorar os preenchimentos.\n{format_data_view_crops_wind_speed(dict_data)}\n')

    # ----------------
    # Parâmetro mínimo
    # ----------------

    float_crp_wind_speed_min = input(f'Caso exista, informe a velocidade do vento mínima para plantio em formato numérico ( ex.: 123, 123.45 ou 123,45 ): ')

    while True:

        try:

            if float_crp_wind_speed_min.strip() != '':

                if ',' in float_crp_wind_speed_min:
                    float_crp_wind_speed_min = float_crp_wind_speed_min.replace(',', '.')

                if Helper.is_float(float_crp_wind_speed_min) == False and Helper.is_int(float_crp_wind_speed_min) == False:
                    raise Exception('O conteúdo informado deve ser numérico ( ex.: 123, 123.45 ou 123,45 ).')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            float_crp_wind_speed_min = input()

    if float_crp_wind_speed_min.strip() != '':
        dict_return['float_crp_wind_speed_min'] = float(float_crp_wind_speed_min)

    # ----------------
    # Parâmetro máximo
    # ----------------

    print('')

    float_crp_wind_speed_max = input(f'Caso exista, informe a velocidade do vento máxima para plantio em formato numérico ( ex.: 123, 123.45 ou 123,45 ): ')

    while True:

        try:

            if float_crp_wind_speed_max.strip() != '':

                if ',' in float_crp_wind_speed_max:
                    float_crp_wind_speed_max = float_crp_wind_speed_max.replace(',', '.')

                if Helper.is_float(float_crp_wind_speed_max) == False and Helper.is_int(float_crp_wind_speed_max) == False:
                    raise Exception('O conteúdo informado deve ser numérico ( ex.: 123, 123.45 ou 123,45 ).')

                if type(dict_return['float_crp_wind_speed_min']) != type(None):

                    if float(float_crp_wind_speed_max) <= dict_return['float_crp_wind_speed_min']:
                        raise Exception(f'O valor máximo deve ser maior que o valor mínimo.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            float_crp_wind_speed_max = input()

    if float_crp_wind_speed_max.strip() != '':
        dict_return['float_crp_wind_speed_max'] = float(float_crp_wind_speed_max)

    return dict_return


"""
Método responsável pela formatação de visualização da chuva do módulo "Culturas"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def format_data_view_crops_rain(dict_data: dict = {}) -> str:

    str_return = None
    list_labels = []

    if 'CRP_RAIN_MIN' in dict_data and type(dict_data['CRP_RAIN_MIN']) != None and Helper.is_float(dict_data['CRP_RAIN_MIN']) == True:
        list_labels.append(f'Mínimo de {dict_data['CRP_RAIN_MIN']} mm')

    if 'CRP_RAIN_MAX' in dict_data and type(dict_data['CRP_RAIN_MAX']) != None and Helper.is_float(dict_data['CRP_RAIN_MAX']) == True:
        list_labels.append(f'Máximo de {dict_data['CRP_RAIN_MAX']} mm')

    str_return = 'Quantidade de chuva ideal: '
    str_return += f'{' | ' . join(list_labels)}' if len(list_labels) > 0 else 'N/I'

    return str_return


"""
Método responsável pela validação dos parâmetros "quantidade de chuva mínima" e "quantidade de chuva máxima"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: dict
"""
def validate_crops_rain(dict_data: dict = {}) -> dict:

    dict_return = {'float_crp_rain_min': None, 'float_crp_rain_max': None}

    print('> Quantidade de Chuva')
    print('A quantidade de chuva será exibida no formato [valor] mm ( ex.: 12 mm, 21 mm, etc. )')
    print('')

    bool_is_update = ('CRP_ID' in dict_data and type(dict_data['CRP_ID']) == int)

    if bool_is_update == True:
        print(f'Importante: Caso deseje manter os valores atuais ( abaixo ), basta ignorar os preenchimentos.\n{format_data_view_crops_rain(dict_data)}\n')

    # ----------------
    # Parâmetro mínimo
    # ----------------

    float_crp_rain_min = input(f'Caso exista, informe a quantidade de chuva para plantio em formato numérico ( ex.: 123, 123.45 ou 123,45 ): ')

    while True:

        try:

            if float_crp_rain_min.strip() != '':

                if ',' in float_crp_rain_min:
                    float_crp_rain_min = float_crp_rain_min.replace(',', '.')

                if Helper.is_float(float_crp_rain_min) == False and Helper.is_int(float_crp_rain_min) == False:
                    raise Exception('O conteúdo informado deve ser numérico ( ex.: 123, 123.45 ou 123,45 ).')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            float_crp_rain_min = input()

    if float_crp_rain_min.strip() != '':
        dict_return['float_crp_rain_min'] = float(float_crp_rain_min)

    # ----------------
    # Parâmetro máximo
    # ----------------

    print('')

    float_crp_rain_max = input(f'Caso exista, informe a quantidade de chuva máxima para plantio em formato numérico ( ex.: 123, 123.45 ou 123,45 ): ')

    while True:

        try:

            if float_crp_rain_max.strip() != '':

                if ',' in float_crp_rain_max:
                    float_crp_rain_max = float_crp_rain_max.replace(',', '.')

                if Helper.is_float(float_crp_rain_max) == False and Helper.is_int(float_crp_rain_max) == False:
                    raise Exception('O conteúdo informado deve ser numérico ( ex.: 123, 123.45 ou 123,45 ).')

                if type(dict_return['float_crp_rain_min']) != type(None):

                    if float(float_crp_rain_max) <= dict_return['float_crp_rain_min']:
                        raise Exception(f'O valor máximo deve ser maior que o valor mínimo.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            float_crp_rain_max = input()

    if float_crp_rain_max.strip() != '':
        dict_return['float_crp_rain_max'] = float(float_crp_rain_max)

    return dict_return


"""
Método responsável pela formatação de visualização da data de cadastro do módulo "Culturas"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def format_data_view_crops_insert_date(dict_data: dict = {}) -> str:

    str_return = 'Data de cadastro: '
    str_return += f'{Helper.convert_date_to_pt_br(dict_data['CRP_INSERT_DATE'])}' if 'CRP_INSERT_DATE' in dict_data and type(dict_data['CRP_INSERT_DATE']) != None and type(dict_data['CRP_INSERT_DATE']) == datetime.datetime else 'N/I'

    return str_return


"""
Método responsável pela formatação de visualização da data de atualização do módulo "Culturas"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def format_data_view_crops_update_date(dict_data: dict = {}) -> str:

    str_return = 'Data de atualização: '
    str_return += f'{Helper.convert_date_to_pt_br(dict_data['CRP_UPDATE_DATE'])}' if 'CRP_UPDATE_DATE' in dict_data and type(dict_data['CRP_UPDATE_DATE']) != None and type(dict_data['CRP_UPDATE_DATE']) == datetime.datetime else 'N/I'

    return str_return


"""
Método responsável pela formatação de visualização de dados do módulo "Culturas"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )
- bool_show_id: Status informando se o parâmetro "ID" deverá ser exibido ( bool )
- bool_show_insert_date: Status informando se o parâmetro "Data de cadastro" deverá ser exibido ( bool )
- bool_show_update_date Status informando se o parâmetro "Data de atualização" deverá ser exibido ( bool )

Return: str
"""
def format_data_view_crops(dict_data: dict = {}, bool_show_id: bool = True, bool_show_insert_date: bool = True, bool_show_update_date: bool = True) -> str:

    str_return = None

    if len(dict_data) > 0:

        str_return = ''
        str_return += f'- {format_data_view_crops_id(dict_data)} \n' if bool_show_id == True else ''
        str_return += f'- {format_data_view_crops_name(dict_data)} \n'
        str_return += f'- {format_data_view_crops_temp(dict_data)} \n'
        str_return += f'- {format_data_view_crops_humidity(dict_data)} \n'
        str_return += f'- {format_data_view_crops_wind_speed(dict_data)} \n'
        str_return += f'- {format_data_view_crops_rain(dict_data)} \n'
        str_return += f'- {format_data_view_crops_insert_date(dict_data)} \n' if bool_show_insert_date == True else ''
        str_return += f'- {format_data_view_crops_update_date(dict_data)} \n' if bool_show_update_date == True else ''

    return str_return


"""
Método responsável pela exibição de cadastros do módulo "Culturas"
"""
def action_crops_list():

    init_step()

    validate_exists_crops()

    object_f2c6_crop = F2C6Crop()

    object_f2c6_crop.set_where([F2C6Crop.get_params_to_active_data()])
    object_f2c6_crop.set_order([{'str_column': 'CRP_ID', 'str_type_order': 'ASC'}])
    list_data = object_f2c6_crop.get_data().get_list()

    for dict_data in list_data:

        print(format_data_view_crops(dict_data))
    
    require_reload_crops()


"""
Método responsável por executar a ação de retorno de dados de uma determinada cultura
"""
def get_data_by_crop(int_crp_id: int = 0) -> dict:

    object_f2c6_crop = F2C6Crop()

    object_f2c6_crop.set_where([

        {'str_column': 'CRP_ID', 'str_type_where': '=', 'value': int_crp_id},
        F2C6Crop.get_params_to_active_data()

    ])

    dict_data = object_f2c6_crop.get_data().get_one()

    if type(dict_data) == type(None):
        raise Exception(f'Nenhum registro foi localizado com o ID {int_crp_id}.')

    return object_f2c6_crop




# ... Demais parâmetros...


"""
Método responsável pela exibição da funcionalidade de cadastro do módulo "Culturas"
"""
def action_crops_insert():

    init_step()

    print('Os parâmetros abaixo fazem parte do cadastro principal da cultura.')
    print('')

    str_crp_name = validate_crops_name()

    # -------
    # Etapa 2
    # -------

    init_step()

    print('Os próximos parâmetros fazem parte da configuração da cultura e não são obrigatórios.')
    input(f'\nPressione <enter> para continuar...')

    # -------
    # Etapa 3
    # -------

    init_step()

    dict_temp = validate_crops_temp()

    # -------
    # Etapa 4
    # -------

    init_step()

    dict_humidity = validate_crops_humidity()

    # -------
    # Etapa 5
    # -------

    init_step()

    dict_wind_speed = validate_crops_wind_speed()

    # -------
    # Etapa 6
    # -------

    init_step()

    dict_rain = validate_crops_rain()

    # -------
    # Etapa 7
    # -------

    loading('Salvando dados, por favor aguarde...')

    # -------
    # Etapa 8
    # -------

    init_step()

    dict_data = {}

    dict_data['CRP_NAME'] = str_crp_name

    if 'float_crp_temp_min' in dict_temp and type(dict_temp['float_crp_temp_min']) != type(None):
        dict_data['CRP_TEMP_MIN'] = dict_temp['float_crp_temp_min']

    if 'float_crp_temp_max' in dict_temp and type(dict_temp['float_crp_temp_max']) != type(None):
        dict_data['CRP_TEMP_MAX'] = dict_temp['float_crp_temp_max']

    if 'float_crp_humidity_min' in dict_humidity and type(dict_humidity['float_crp_humidity_min']) != type(None):
        dict_data['CRP_HUMIDITY_MIN'] = dict_humidity['float_crp_humidity_min']

    if 'float_crp_humidity_max' in dict_humidity and type(dict_humidity['float_crp_humidity_max']) != type(None):
        dict_data['CRP_HUMIDITY_MAX'] = dict_humidity['float_crp_humidity_max']

    if 'float_crp_wind_speed_min' in dict_wind_speed and type(dict_wind_speed['float_crp_wind_speed_min']) != type(None):
        dict_data['CRP_WIND_SPEED_MIN'] = dict_wind_speed['float_crp_wind_speed_min']

    if 'float_crp_wind_speed_max' in dict_wind_speed and type(dict_wind_speed['float_crp_wind_speed_max']) != type(None):
        dict_data['CRP_WIND_SPEED_MAX'] = dict_wind_speed['float_crp_wind_speed_max']

    if 'float_crp_rain_min' in dict_rain and type(dict_rain['float_crp_rain_min']) != type(None):
        dict_data['CRP_RAIN_MIN'] = dict_rain['float_crp_rain_min']

    if 'float_crp_rain_max' in dict_rain and type(dict_rain['float_crp_rain_max']) != type(None):
        dict_data['CRP_RAIN_MAX'] = dict_rain['float_crp_rain_max']

    object_f2c6_crop = F2C6Crop()
    object_f2c6_crop.insert(dict_data)

    print(format_data_view_crops(dict_data = dict_data, bool_show_id = False, bool_show_insert_date = False, bool_show_update_date = False))

    print('Registro cadastrado com sucesso.')

    require_reload_crops()


"""
Método responsável pela exibição da funcionalidade de atualização do módulo "Culturas"
"""
def action_crops_update():

    init_step()

    validate_exists_crops()

    int_crp_id = validate_crops_id()

    # -------
    # Etapa 2
    # -------

    loading('Verificando dados, por favor aguarde...')

    init_step()

    object_f2c6_crop = get_data_by_crop(int_crp_id)
    dict_data = object_f2c6_crop.get_one()

    print('Os dados abaixo representam o cadastro atual do registro informado.')
    print('')

    print(format_data_view_crops(dict_data))

    input(f'Pressione <enter> para continuar...')

    # -------
    # Etapa 3
    # -------

    init_step()

    print('Os parâmetros abaixo fazem parte do cadastro principal da cultura.')
    print('')

    str_crp_name = validate_crops_name(dict_data)

    # -------
    # Etapa 4
    # -------

    init_step()

    print('Os próximos parâmetros fazem parte da configuração da cultura e não são obrigatórios.')
    input(f'\nPressione <enter> para continuar...')

    # -------
    # Etapa 5
    # -------

    init_step()

    dict_temp = validate_crops_temp(dict_data)

    # -------
    # Etapa 6
    # -------

    init_step()

    dict_humidity = validate_crops_humidity(dict_data)

    # -------
    # Etapa 7
    # -------

    init_step()

    dict_wind_speed = validate_crops_wind_speed(dict_data)

    # -------
    # Etapa 8
    # -------

    init_step()

    dict_rain = validate_crops_rain(dict_data)

    # -------
    # Etapa 9
    # -------

    loading('Salvando dados, por favor aguarde...')

    # --------
    # Etapa 10
    # --------

    init_step()

    if str_crp_name.strip() != '':
        dict_data['CRP_NAME'] = str_crp_name

    if 'float_crp_temp_min' in dict_temp and type(dict_temp['float_crp_temp_min']) != type(None):
        dict_data['CRP_TEMP_MIN'] = dict_temp['float_crp_temp_min']

    if 'float_crp_temp_max' in dict_temp and type(dict_temp['float_crp_temp_max']) != type(None):
        dict_data['CRP_TEMP_MAX'] = dict_temp['float_crp_temp_max']

    if 'float_crp_humidity_min' in dict_humidity and type(dict_humidity['float_crp_humidity_min']) != type(None):
        dict_data['CRP_HUMIDITY_MIN'] = dict_humidity['float_crp_humidity_min']

    if 'float_crp_humidity_max' in dict_humidity and type(dict_humidity['float_crp_humidity_max']) != type(None):
        dict_data['CRP_HUMIDITY_MAX'] = dict_humidity['float_crp_humidity_max']

    if 'float_crp_wind_speed_min' in dict_wind_speed and type(dict_wind_speed['float_crp_wind_speed_min']) != type(None):
        dict_data['CRP_WIND_SPEED_MIN'] = dict_wind_speed['float_crp_wind_speed_min']

    if 'float_crp_wind_speed_max' in dict_wind_speed and type(dict_wind_speed['float_crp_wind_speed_max']) != type(None):
        dict_data['CRP_WIND_SPEED_MAX'] = dict_wind_speed['float_crp_wind_speed_max']

    if 'float_crp_rain_min' in dict_rain and type(dict_rain['float_crp_rain_min']) != type(None):
        dict_data['CRP_RAIN_MIN'] = dict_rain['float_crp_rain_min']

    if 'float_crp_rain_max' in dict_rain and type(dict_rain['float_crp_rain_max']) != type(None):
        dict_data['CRP_RAIN_MAX'] = dict_rain['float_crp_rain_max']

    object_f2c6_crop.update(dict_data)

    print(format_data_view_crops(dict_data = dict_data, bool_show_update_date = False))

    print('Registro atualizado com sucesso.')
    
    require_reload_crops()


"""
Método responsável pela exibição da funcionalidade de exclusão do módulo "Culturas"
"""
def action_crops_delete():

    init_step()

    validate_exists_crops()

    int_crp_id = validate_crops_id()

    # -------
    # Etapa 2
    # -------

    loading('Verificando dados, por favor aguarde...')

    init_step()

    object_f2c6_crop = get_data_by_crop(int_crp_id)
    dict_data = object_f2c6_crop.get_one()

    dict_data['CRP_STATUS'] = 0

    object_f2c6_crop.update(dict_data)

    print('Registro excluído com sucesso.')

    require_reload_crops()


"""
Método responsável pela exibição padrão do módulo "Culturas"
"""
def action_crops():

    try:

        init_step()

        test_connection_by_database()

        list_menu_options = get_crops_menu_options()

        for dict_menu_option in list_menu_options:
            print(f'{dict_menu_option['code']}. {dict_menu_option['title']}')

        print('')

        require_crops_menu_option()

    except Exception as error:

        print(f'> Ocorreu o seguinte erro: {error}')
        require_reload_crops()


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes a opção "Análises e alertas para plantio"
# ---------------------------------------------------------------------------------------------------------------

"""
Método responsável por verificar se existem culturas cadastradas
"""
def validate_exists_crops_to_planting_alert():

    try:

        validate_exists_crops()

    except Exception as error:

        print(f'> Ocorreu o seguinte erro: {error}')
        require_reload_system()


"""
Método responsável por recarregar o módulo "Análises e alertas para plantio"
"""
def require_reload_planting_alert():

    input(f'\nPressione <enter> para voltar a tela principal de simulação de alertas para plantio...')
    action_planting_alert()


"""
Método responsável pela validação do tipo de cálculo para simulação de alertas para plantio

Return: str
"""
def validate_calc_type() -> int:

    print(f'Opções disponíveis para execução dos cálculos da simulação de alertas para plantio:')
    print(f'- 1: Utilizar os valores cadastrados para a cultura selecionada;')
    print(f'- 2: Preencher outros valores a seguir. Caso algum valor não seja preenchido, por padrão, será utilizado o que foi cadastrado para a cultura selecionada;')
    int_return = input(f'Digite uma das opções: ')

    while True:

        try:

            if int_return.strip() == '':
                raise Exception('Deve ser informada uma opção válida.')

            if Helper.is_int(int_return) == False: 
                raise Exception('O conteúdo informado deve ser numérico.')

            if int(int_return) not in [1, 2]:
                raise Exception('A opção informada deve representar uma das opções disponíveis.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            int_return = input()

    return int(int_return)


"""
Método responsável pela validação do tipo de definição de localização para simulação de alertas para plantio

Return: str
"""
def validate_locality_type() -> int:

    print(f'Opções disponíveis para definição de localização para simulação de alertas para plantio:')
    print(f'- 1: Informar cidade, estado/província e país no formato [nome_cidade],[sigla_estado_província],[sigla_país] ( ex.: São Paulo,SP,BR , Rio grande do sul,RS,BR , Noventa Vicentina,Ve,IT , etc. );')
    print(f'- 2: Informar latitude e longitude ( ex.: 43.98882933123789, 18.180055506117746 , -21.786002807359086, -46.56287094468699, 45.41024449730194, 11.877725912383978 , etc. );')
    int_return = input(f'Digite uma das opções: ')

    while True:

        try:

            if int_return.strip() == '':
                raise Exception('Deve ser informada uma opção válida.')

            if Helper.is_int(int_return) == False: 
                raise Exception('O conteúdo informado deve ser numérico.')

            if int(int_return) not in [1, 2]:
                raise Exception('A opção informada deve representar uma das opções disponíveis.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            int_return = input()

    return int(int_return)


"""
Método responsável pela validação do parâmetro "Cidade"

Return: str
"""
def validate_planting_alert_city() -> str:

    str_return = input(f'Informe o nome da cidade: ')

    while True:

        try:

            if str_return.strip() == '':
                raise Exception('Deve ser informada uma cidade válida.')

            if type(str_return) != str: 
                raise Exception('O conteúdo informado deve ser texto.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            str_return = input()

    return str(str_return.strip())


"""
Método responsável pela validação do parâmetro "Estado/Província"

Return: str
"""
def validate_planting_alert_state() -> str:

    str_return = input(f'Informe a sigla do estado/província: ')

    while True:

        try:

            if str_return.strip() == '':
                raise Exception('Deve ser informada uma sigla válida.')

            if type(str_return) != str: 
                raise Exception('O conteúdo informado deve ser texto.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            str_return = input()

    return str(str_return.strip())


"""
Método responsável pela validação do parâmetro "País"

Return: str
"""
def validate_planting_alert_country() -> str:

    str_return = input(f'Informe a sigla do país: ')

    while True:

        try:

            if str_return.strip() == '':
                raise Exception('Deve ser informada uma sigla válida.')

            if type(str_return) != str: 
                raise Exception('O conteúdo informado deve ser texto.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            str_return = input()

    return str(str_return.strip())


"""
Método responsável pela validação do parâmetro "Latitude"

Return: float
"""
def validate_planting_alert_latitude() -> float:

    float_return = input(f'Informe a latitude da localização: ')

    while True:

        try:

            if float_return.strip() == '':
                raise Exception('Deve ser informada uma latitude válida.')

            if ',' in float_return:
                float_return = float_return.replace(',', '.')

            if Helper.is_float(float_return) == False and Helper.is_int(float_return) == False:
                raise Exception('O conteúdo informado deve ser numérico ( ex.: 123, 123.45 ou 123,45 ).')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            float_return = input()

    return float(float_return)


"""
Método responsável pela validação do parâmetro "Longitude"

Return: float
"""
def validate_planting_alert_longitude() -> float:

    float_return = input(f'Informe a longitude da localização: ')

    while True:

        try:

            if float_return.strip() == '':
                raise Exception('Deve ser informada uma longitude válida.')

            if ',' in float_return:
                float_return = float_return.replace(',', '.')

            if Helper.is_float(float_return) == False and Helper.is_int(float_return) == False:
                raise Exception('O conteúdo informado deve ser numérico ( ex.: 123, 123.45 ou 123,45 ).')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            float_return = input()

    return float(float_return)


"""
Método responsável pela validação do tipo de retorno após conclusão dos cálculos

Return: int
"""
def validate_planting_alert_return_type() -> int:

    print(f'Opções disponíveis para finalização da simulação:')
    print(f'- 1: Voltar para a opção de seleção da cultura;')
    print(f'- 2: Voltar para a opção de definição de localização;')
    print(f'- 3: Voltar ao menu principal;')
    int_return = input(f'Digite uma das opções: ')

    while True:

        try:

            if int_return.strip() == '':
                raise Exception('Deve ser informada uma opção válida.')

            if Helper.is_int(int_return) == False: 
                raise Exception('O conteúdo informado deve ser numérico.')

            if int(int_return) not in [1, 2, 3]:
                raise Exception('A opção informada deve representar uma das opções disponíveis.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            int_return = input()

    return int(int_return)


"""
Método responsável pela disponibilização das opções para finalização após conclusão dos cálculos

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )
"""
def request_planting_alert_return_type(dict_data: dict = {}):

    print('')

    int_return_type = validate_planting_alert_return_type()

    if int_return_type == 1:

        action_planting_alert()

    elif int_return_type == 2:

        init_planting_alert_step_calc(dict_data)

    elif int_return_type == 3:

        init_system()


"""
Método responsável pela formatação de visualização da cidade

Arguments:
- dict_forecast_calc: Dict contendo os dados conforme retorno do cálculo ( dictionary )

Return: str
"""
def format_data_view_forecast_calc_city(dict_forecast_calc: dict = {}) -> str:

    str_return = 'Cidade: '
    str_return += f'{dict_forecast_calc['str_city'].strip()}' if 'str_city' in dict_forecast_calc and type(dict_forecast_calc['str_city']) != None and type(dict_forecast_calc['str_city']) == str else 'N/I'

    return str_return


"""
Método responsável pela formatação de visualização do país

Arguments:
- dict_forecast_calc: Dict contendo os dados conforme retorno do cálculo ( dictionary )

Return: str
"""
def format_data_view_forecast_calc_country(dict_forecast_calc: dict = {}) -> str:

    str_return = 'País: '
    str_return += f'{dict_forecast_calc['str_country'].strip()}' if 'str_country' in dict_forecast_calc and type(dict_forecast_calc['str_country']) != None and type(dict_forecast_calc['str_country']) == str else 'N/I'

    return str_return


"""
Método responsável pela formatação de visualização da latitude

Arguments:
- dict_forecast_calc: Dict contendo os dados conforme retorno do cálculo ( dictionary )

Return: str
"""
def format_data_view_forecast_calc_latitude(dict_forecast_calc: dict = {}) -> str:

    str_return = 'Latitude: '
    str_return += f'{dict_forecast_calc['float_latitude']}' if 'float_latitude' in dict_forecast_calc and type(dict_forecast_calc['float_latitude']) != None and type(dict_forecast_calc['float_latitude']) == float else 'N/I'

    return str_return


"""
Método responsável pela formatação de visualização da longitude

Arguments:
- dict_forecast_calc: Dict contendo os dados conforme retorno do cálculo ( dictionary )

Return: str
"""
def format_data_view_forecast_calc_longitude(dict_forecast_calc: dict = {}) -> str:

    str_return = 'Longitude: '
    str_return += f'{dict_forecast_calc['float_longitude']}' if 'float_longitude' in dict_forecast_calc and type(dict_forecast_calc['float_longitude']) != None and type(dict_forecast_calc['float_longitude']) == float else 'N/I'

    return str_return


"""
Método responsável pela formatação de visualização da data e hora

Arguments:
- dict_forecast_calc: Dict contendo os dados conforme retorno do cálculo ( dictionary )

Return: str
"""
def format_data_view_forecast_calc_datetime(dict_forecast_calc: dict = {}) -> str:

    str_return = 'Data e hora: '
    str_return += f'{Helper.convert_date_to_pt_br(Helper.get_datetime_object_by_date_oracle(dict_forecast_calc['str_datetime'].strip()))}' if 'str_datetime' in dict_forecast_calc and type(dict_forecast_calc['str_datetime']) != None and type(dict_forecast_calc['str_datetime']) == str else 'N/I'

    return str_return


"""
Método responsável pela formatação de visualização da descrição da previsão

Arguments:
- dict_forecast_calc: Dict contendo os dados conforme retorno do cálculo ( dictionary )

Return: str
"""
def format_data_view_forecast_calc_forecast_description(dict_forecast_calc: dict = {}) -> str:

    str_return = 'Previsão: '
    str_return += f'{dict_forecast_calc['str_weather_description']}' if 'str_weather_description' in dict_forecast_calc and type(dict_forecast_calc['str_weather_description']) != None and type(dict_forecast_calc['str_weather_description']) == str else 'N/I'

    return str_return


"""
Método responsável pela formatação de visualização dos títulos dos parâmetros

Arguments:
- dict_forecast_calc: Dict contendo os dados conforme retorno do cálculo ( dictionary )

Return: str
"""
def format_data_view_forecast_calc_title(dict_forecast_calc: dict = {}) -> str:

    str_return = ''
    str_return += f'{dict_forecast_calc['str_title'].strip()}' if 'str_title' in dict_forecast_calc and type(dict_forecast_calc['str_title']) != None and type(dict_forecast_calc['str_title']) == str else 'N/I'

    return str_return


"""
Método responsável pela formatação de visualização da análise

Arguments:
- dict_forecast_calc: Dict contendo os dados conforme retorno do cálculo ( dictionary )

Return: str
"""
def format_data_view_forecast_calc_analisys(dict_forecast_calc: dict = {}) -> str:

    str_return = 'Análise: '
    str_return += f'{dict_forecast_calc['str_analysis'].strip()}' if 'str_analysis' in dict_forecast_calc and type(dict_forecast_calc['str_analysis']) != None and type(dict_forecast_calc['str_analysis']) == str else 'N/I'

    return str_return


"""
Método responsável pela formatação de visualização das informações adicionais

Arguments:
- dict_forecast_calc: Dict contendo os dados conforme retorno do cálculo ( dictionary )

Return: str
"""
def format_data_view_forecast_calc_additional_info(dict_forecast_calc: dict = {}) -> str:

    str_return = 'Informações adicionais: '

    if 'list_additional_info' not in dict_forecast_calc or type(dict_forecast_calc['list_additional_info']) != list or len(dict_forecast_calc['list_additional_info']) == 0:

        str_return += f'N/I'

    else:

        for str_additional_info in dict_forecast_calc['list_additional_info']:

            str_return += f'\n    - {str_additional_info}'

    return str_return


"""
Método responsável pela formatação de conclusão final

Arguments:
- dict_forecast_calc: Dict contendo os dados conforme retorno do cálculo ( dictionary )

Return: str
"""
def format_data_view_forecast_calc_conclusion(dict_forecast_calc: dict = {}) -> str:

    str_return = 'Conclusão: '
    str_return += f'{dict_forecast_calc['str_conclusion'].strip()}' if 'str_conclusion' in dict_forecast_calc and type(dict_forecast_calc['str_conclusion']) != None and type(dict_forecast_calc['str_conclusion']) == str else 'N/I'

    return str_return


"""
Método responsável por parametrizar a visualização para a etapa de cálculos da simulação de alertas para plantio

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )
"""
def init_planting_alert_step_calc(dict_data: dict = {}):

    try:

        if type(dict_data) != dict or len(dict_data) == 0:
            raise Exception('Não foi possível iniciar a etapa de cálculos da simulação de alertas para plantio pois os parâmetros necessários não foram definidos.')

        init_step()

        int_locality_type = validate_locality_type()

        # -------
        # Etapa 2
        # -------

        init_step()

        object_open_weather = OpenWeather()

        if int_locality_type == 1:

            # ---------
            # Etapa 2.1
            # ---------

            print('> Localização a partir de cidade, estado/província e país.')
            print('')

            str_city = validate_planting_alert_city()

            print('')

            str_state = validate_planting_alert_state()

            print('')

            str_country = validate_planting_alert_country()

            loading('Preparando valores para cálculo a partir de cidade, estado/província e país, por favor aguarde...')

            dict_data_open_weather = object_open_weather.get_weather_forecast_data_by_location(str_city_state_country = f'{str_city},{str_state},{str_country}')

        elif int_locality_type == 2:

            # ---------
            # Etapa 2.1
            # ---------

            print('> Localização a partir de latitude e longitude.')
            print('')

            float_latitude = validate_planting_alert_latitude()

            print('')

            float_longitude = validate_planting_alert_longitude()

            loading('Preparando valores para cálculo a partir de latitude e longitude, por favor aguarde...')

            dict_data_open_weather = object_open_weather.get_weather_forecast_data_by_location(float_latitude = float_latitude, float_longitude = float_longitude)

        # Validação do retorno dos dados meteorológicos de forma padrão independente do tipo selecionado acima
        if dict_data_open_weather['status'] == False: 
            raise Exception(dict_data_open_weather['message'])

        # -------
        # Etapa 3
        # -------

        init_step()

        dict_params_calc = {}

        if 'CRP_TEMP_MIN' in dict_data and type(dict_data['CRP_TEMP_MIN']) != type(None):
            dict_params_calc['float_temp_min'] = dict_data['CRP_TEMP_MIN']

        if 'CRP_TEMP_MAX' in dict_data and type(dict_data['CRP_TEMP_MAX']) != type(None):
            dict_params_calc['float_temp_max'] = dict_data['CRP_TEMP_MAX']

        if 'CRP_HUMIDITY_MIN' in dict_data and type(dict_data['CRP_HUMIDITY_MIN']) != type(None):
            dict_params_calc['float_humidity_min'] = dict_data['CRP_HUMIDITY_MIN']

        if 'CRP_HUMIDITY_MAX' in dict_data and type(dict_data['CRP_HUMIDITY_MAX']) != type(None):
            dict_params_calc['float_humidity_max'] = dict_data['CRP_HUMIDITY_MAX']

        if 'CRP_WIND_SPEED_MIN' in dict_data and type(dict_data['CRP_WIND_SPEED_MIN']) != type(None):
            dict_params_calc['float_wind_speed_min'] = dict_data['CRP_WIND_SPEED_MIN']

        if 'CRP_WIND_SPEED_MAX' in dict_data and type(dict_data['CRP_WIND_SPEED_MAX']) != type(None):
            dict_params_calc['float_wind_speed_max'] = dict_data['CRP_WIND_SPEED_MAX']

        if 'CRP_RAIN_MIN' in dict_data and type(dict_data['CRP_RAIN_MIN']) != type(None):
            dict_params_calc['float_rain_min'] = dict_data['CRP_RAIN_MIN']

        if 'CRP_RAIN_MAX' in dict_data and type(dict_data['CRP_RAIN_MAX']) != type(None):
            dict_params_calc['float_rain_max'] = dict_data['CRP_RAIN_MAX']

        dict_forecast_calc = object_open_weather.execute_forecast_calc(dict_data_open_weather['dict_data'], dict_params_calc)
        if dict_forecast_calc['status'] == False: 
            raise Exception(dict_forecast_calc['message'])

        print('Os dados abaixo representam o cadastro atual do registro informado.')
        print('')

        print(format_data_view_crops(dict_data))

        if len(dict_forecast_calc['dict_data']['list_weather']) == 0:
            print('Não existem dados para serem exbidos.')

        else:

            print('As informações abaixo representam a localização definida.')
            print('')

            print(f'- {format_data_view_forecast_calc_city(dict_forecast_calc['dict_data'])}')
            print(f'- {format_data_view_forecast_calc_country(dict_forecast_calc['dict_data'])}')
            print(f'- {format_data_view_forecast_calc_latitude(dict_forecast_calc['dict_data'])}')
            print(f'- {format_data_view_forecast_calc_longitude(dict_forecast_calc['dict_data'])}')
            
            print('')
            print('As informações abaixo se baseiam em intervalos de 6h para os próximos dias.')
            print('')

            for dict_weather in dict_forecast_calc['dict_data']['list_weather']:

                print('> --------------------------------------------------------------------------------------------------------------------------------------')
                print('')

                print('> Dados gerais da previsão')
                print(f'- {format_data_view_forecast_calc_datetime(dict_weather)}')
                print(f'- {format_data_view_forecast_calc_forecast_description(dict_weather)}')
                print('')

                print(f'> {format_data_view_forecast_calc_title(dict_weather['dict_temp'])}')
                print(f'- {format_data_view_forecast_calc_analisys(dict_weather['dict_temp'])}')
                print(f'- {format_data_view_forecast_calc_additional_info(dict_weather['dict_temp'])}')
                print('')

                print(f'> {format_data_view_forecast_calc_title(dict_weather['dict_umidity'])}')
                print(f'- {format_data_view_forecast_calc_analisys(dict_weather['dict_umidity'])}')
                print(f'- {format_data_view_forecast_calc_additional_info(dict_weather['dict_umidity'])}')
                print('')

                print(f'> {format_data_view_forecast_calc_title(dict_weather['dict_wind_speed'])}')
                print(f'- {format_data_view_forecast_calc_analisys(dict_weather['dict_wind_speed'])}')
                print(f'- {format_data_view_forecast_calc_additional_info(dict_weather['dict_wind_speed'])}')
                print('')

                print(f'> {format_data_view_forecast_calc_title(dict_weather['dict_rain'])}')
                print(f'- {format_data_view_forecast_calc_analisys(dict_weather['dict_rain'])}')
                print(f'- {format_data_view_forecast_calc_additional_info(dict_weather['dict_rain'])}')
                print('')

                print(f'> {format_data_view_forecast_calc_conclusion(dict_weather['dict_conclusion'])}')
                print('')

        request_planting_alert_return_type(dict_data)

    except Exception as error:

        init_step()

        print(f'> Ocorreu o seguinte erro: {error}')

        request_planting_alert_return_type(dict_data)


"""
Método responsável pela exibição padrão do módulo "Análises e alertas para plantio"
"""
def action_planting_alert():

    try:

        init_step()

        test_connection_by_database()

        validate_exists_crops_to_planting_alert()

        int_crp_id = validate_crops_id()

        # -------
        # Etapa 2
        # -------

        loading('Verificando dados, por favor aguarde...')

        init_step()

        object_f2c6_crop = get_data_by_crop(int_crp_id)
        dict_data = object_f2c6_crop.get_one()

        print('Os dados abaixo representam o cadastro atual do registro informado.')
        print('')

        print(format_data_view_crops(dict_data))

        int_calc_type = validate_calc_type()

        # -------
        # Etapa 3
        # -------

        if int_calc_type == 2:

            # ---------
            # Etapa 3.1
            # ---------

            init_step()

            dict_temp = validate_crops_temp()

            if 'float_crp_temp_min' in dict_temp and type(dict_temp['float_crp_temp_min']) != type(None):
                dict_data['CRP_TEMP_MIN'] = dict_temp['float_crp_temp_min']

            if 'float_crp_temp_max' in dict_temp and type(dict_temp['float_crp_temp_max']) != type(None):
                dict_data['CRP_TEMP_MAX'] = dict_temp['float_crp_temp_max']

            # ---------
            # Etapa 3.2
            # ---------

            init_step()

            dict_humidity = validate_crops_humidity()

            if 'float_crp_humidity_min' in dict_humidity and type(dict_humidity['float_crp_humidity_min']) != type(None):
                dict_data['CRP_HUMIDITY_MIN'] = dict_humidity['float_crp_humidity_min']

            if 'float_crp_humidity_max' in dict_humidity and type(dict_humidity['float_crp_humidity_max']) != type(None):
                dict_data['CRP_HUMIDITY_MAX'] = dict_humidity['float_crp_humidity_max']

            # ---------
            # Etapa 3.3
            # ---------

            init_step()

            dict_wind_speed = validate_crops_wind_speed()

            if 'float_crp_wind_speed_min' in dict_wind_speed and type(dict_wind_speed['float_crp_wind_speed_min']) != type(None):
                dict_data['CRP_WIND_SPEED_MIN'] = dict_wind_speed['float_crp_wind_speed_min']

            if 'float_crp_wind_speed_max' in dict_wind_speed and type(dict_wind_speed['float_crp_wind_speed_max']) != type(None):
                dict_data['CRP_WIND_SPEED_MAX'] = dict_wind_speed['float_crp_wind_speed_max']

            # ---------
            # Etapa 3.4
            # ---------

            init_step()

            dict_rain = validate_crops_rain()

            if 'float_crp_rain_min' in dict_rain and type(dict_rain['float_crp_rain_min']) != type(None):
                dict_data['CRP_RAIN_MIN'] = dict_rain['float_crp_rain_min']

            if 'float_crp_rain_max' in dict_rain and type(dict_rain['float_crp_rain_max']) != type(None):
                dict_data['CRP_RAIN_MAX'] = dict_rain['float_crp_rain_max']

        # -------
        # Etapa 4
        # -------

        init_planting_alert_step_calc(dict_data)

    except Exception as error:

        print(f'> Ocorreu o seguinte erro: {error}')
        require_reload_planting_alert()


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes a opção "Sair"
# ---------------------------------------------------------------------------------------------------------------

"""
Método responsável pela saída do sistema
"""
def action_exit():

    init_step()

    print(f'Obrigado por utilizar o sistema.\n')


# ---------------------------------------------------------------------------------------------------------------

"""
Ação responsável por executar a inicialização do sistema
"""
if(__name__ == '__main__'):

    init_system()

