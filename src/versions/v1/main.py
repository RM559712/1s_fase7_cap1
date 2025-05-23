import os
import json
import time
from custom.helper import Helper
from models.crop import Crop
from models.coffe import Coffe
from models.corn import Corn
from models.rice import Rice
from models.soy import Soy
from models.sugarcane import Sugarcane
import subprocess

# Objeto que atuará como "banco de dados"
database_temp = {
    'data': {},
    'crop_items': []
}

# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes à estrutura do sistema
# ---------------------------------------------------------------------------------------------------------------

def get_current_path_dir() -> str:

    return os.path.dirname(os.path.realpath(__file__))

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
def loading(message: str = 'Processando, por favor aguarde...', seconds: int = 5, is_reset: bool = True):

    if is_reset == True:
        show_head_system()

    print(f'\n{message}', end=' ')
    time.sleep(seconds)


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
Método responsável por retornar as opções de menu do sistema

Return: List
"""
def get_menu_options() -> list:

    return [
        {
            'code': 1,
            'title': 'Listar cálculos efetuados',
            'action': action_list
        },{
            'code': 2,
            'title': 'Executar cálculos',
            'action': action_insert
        },{
            'code': 3,
            'title': 'Editar cálculo',
            'action': action_update
        },{
            'code': 4,
            'title': 'Excluir cálculo',
            'action': action_delete
        },{
            'code': 5,
            'title': 'Visualizar cálculo',
            'action': action_view
        },{
            'code': 6,
            'title': 'Executar relatório de cálculos em R',
            'action': action_execute_calc_report_r
        },{
            'code': 7,
            'title': 'Executar relatório meteorológico em R',
            'action': action_execute_weather_report_r
        },{
            'code': 8,
            'title': 'Sair',
            'action': exit
        }
    ]


"""
Método responsável por retornar os códigos das opções de menu do sistema

Return: List
"""
def get_menu_options_codes() -> list:

    list = []

    list_menu_options = get_menu_options()

    for menu_option in list_menu_options:
        list.append(menu_option['code'])

    return list


"""
Método responsável pela validação do parâmetro "Opção do menu"

Arguments:
- value_validate: Conteúdo que deverá ser validado ( string )

Return: Dictionary
"""
def validate_menu_option(value_validate: str = '') -> dict:

    return_method = {'status': True}

    try:

        if value_validate.strip() == '':
            raise Exception('Deve ser definida uma opção válida.')

        if Helper.is_int(value_validate) == False: 
            raise Exception('A opção informada deve ser numérica.')

        if int(value_validate) not in get_menu_options_codes(): 
            raise Exception('A opção informada deve representar um dos menus disponíveis.')

    except Exception as error:

        return_method = {'status': False, 'message': error}

    return return_method


"""
Método responsável por solicitar a opção do sistema que deverá ser executada
"""
def require_options():

    try:

        option = input(f'Digite uma opção: ')

        while True:
            return_validate_menu_option = validate_menu_option(option)
            if return_validate_menu_option['status'] == False:
                print(f'{return_validate_menu_option['message']} Tente novamente: ', end = '')
                option = input()

            else: break

        show_head_system()

        list_menu_options = get_menu_options()

        for menu_option in list_menu_options:
            if menu_option['code'] == int(option):
                menu_option['action']()

    except Exception as error:

        print(f'\n> Ocorreu o seguinte erro: {error}')
        require_reload_system()


"""
Método responsável por executar a inicialização do sistema
"""
def init_system():

    append_crops()

    show_head_system()

    print('')

    list_menu_options = get_menu_options()

    for menu_option in list_menu_options:
        print(f'{menu_option['code']}. {menu_option['title']}')

    print('')

    require_options()


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes aos dados armazenados no sistema
# ---------------------------------------------------------------------------------------------------------------

"""
Método responsável pela validação de existência de dados cadastrados
"""
def validate_exists_data():

    if len(database_temp['data']) == 0:
        raise Exception('Não existem dados cadastrados.')


"""
Método responsável por retornar o próximo ID para armazenamento

Return: Int
"""
def get_next_id() -> int:

    last_id = 0

    if len(database_temp['data']) > 0:
        for id in database_temp['data']:
            if id > last_id: last_id = id

    last_id += 1

    return int(last_id)


"""
Método responsável pela validação do parâmetro "id"

Arguments:
- value_validate: Conteúdo que deverá ser validado ( int )

Return: Boolean
"""
def validate_id(value_validate: int = 0) -> bool:

    return False if int(value_validate) == 0 else True


"""
Método responsável por retornar os dados de um determinado registro
- id: ID do registro que deverá ser utilizado para retorno dos dados ( int )

Return: Dictionary
"""
def get_data_by_id(id: int = 0) -> dict:

    if(int(id) not in database_temp['data']):
        raise Exception(f'Nenhum registro foi localizado com o ID {id}.')

    return database_temp['data'][ int(id) ]


"""
Método responsável pela formatação de visualização de dados

Arguments:
- id: ID do registro que dverá ser exibido ( int )
- object_data: Objeto contendo os parâmetros do registro que deverá ser exibido ( dictionary )

Return: Boolean
"""
def format_data_view(id: int = 0, object_data: dict = {}) -> str:

    string_params = ''

    for params_calc in object_data['params_calc']:
        if string_params.strip() != '': string_params += ' | '
        string_params += f'''{params_calc['title']}: {params_calc['param']}'''

    principal_local = object_data['class_crop'].get_principal_local()

    string_return = f'\n'
    string_return += f'- ID: {id} \n'
    string_return += f'- Cultura: {object_data['class_crop'].get_name()} \n'
    string_return += f'- Local: {principal_local['city']} ( {principal_local['state']} ) \n'
    string_return += f'- Cálculo: {object_data['calc']['title']} \n'
    string_return += f'- Parâmetros utilizados: {string_params} \n'
    string_return += f'- Resultado: {object_data['result_calc']['label']}'

    return string_return


"""
Método responsável pela exportação de dados em formato json
"""
def export_data_to_json_file():

    validate_exists_data()

    list_data = []

    # Processo de remoção de keys que não serão utilizadas
    for id in database_temp['data']:
        object_data = database_temp['data'][ id ]

        principal_local = object_data['class_crop'].get_principal_local()

        list_data.append({
            'code': object_data['crop'],
            'crop': object_data['class_crop'].get_name(),
            'state': principal_local['state'],
            'city': principal_local['city'],
            'calc': {
                'code': object_data['calc']['code'],
                'title': object_data['calc']['title'],
                'params_calc': object_data['params_calc'],
                'result_calc': object_data['result_calc']
            }
        })

    current_dir_path = get_current_path_dir()
    
    with open(f'{current_dir_path}{os.sep}data{os.sep}_tempData.json', 'w+', encoding='utf-8') as jsonFile:
        json.dump(list_data, jsonFile, indent=4, ensure_ascii=False)


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes às culturas do sistema
# ---------------------------------------------------------------------------------------------------------------

"""
Método responsável por definir quais as culturas deverão estar disponíveis para utilização no sistema
"""
def append_crops():

    database_temp['crop_items'] = []

    class_coffe = Coffe()
    class_coffe.reset_infos()
    class_coffe.append_standard_infos()
    database_temp['crop_items'].append(class_coffe)

    class_corn = Corn()
    class_corn.reset_infos()
    class_corn.append_standard_infos()
    database_temp['crop_items'].append(class_corn)

    class_rice = Rice()
    class_rice.reset_infos()
    class_rice.append_standard_infos()
    database_temp['crop_items'].append(class_rice)

    class_soy = Soy()
    class_soy.reset_infos()
    class_soy.append_standard_infos()
    database_temp['crop_items'].append(class_soy)

    class_sugarcane = Sugarcane()
    class_sugarcane.reset_infos()
    class_sugarcane.append_standard_infos()
    database_temp['crop_items'].append(class_sugarcane)


"""
Método responsável por retornar as culturas disponíveis para utilização no sistema

Return: List
"""
def get_crops() -> list:

    if 'crop_items' not in database_temp or len(database_temp['crop_items']) == 0:
        raise Exception(f'Não foi possível concluir o processo pois não foram definidas as culturas para utilização no sistema.')

    return database_temp['crop_items']


"""
Método responsável por retornar os códigos das culturas disponíveis para utilização no sistema

Return: List
"""
def get_crops_codes() -> list:

    list = []

    crops = get_crops()

    for crop in crops:
        if isinstance(crop, Crop):
            list.append(crop.get_code())

    return list


"""
Método responsável pela exibição das culturas disponíveis para utilização no sistema
"""
def show_crops():

    crops = get_crops()

    print('')
    print(f'As culturas disponíveis para utilização no sistema são: \n')

    for crop in crops:
        if isinstance(crop, Crop):
            print(f'{crop.get_code()}. {crop.get_name()}')

    print('')


"""
Método responsável por retornar a instância de uma cultura a partir de um determinado código

Return: Class Crop
"""
def get_class_crop_by_code(code: int = 0) -> Crop:

    if Helper.is_int(code) == False:
        raise Exception('O código informado deve ser numérico.')

    return_crop = ''

    crops = get_crops()

    for crop in crops:
        if isinstance(crop, Crop):
            if(crop.get_code() == int(code)):
                return_crop = crop
                break

    if isinstance(return_crop, Crop) == False:
        raise Exception(f'Não foi possível concluir o processo pois nenhuma cultura foi localizada a partir do código {code}.')

    return return_crop


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes a opção "Listar cálculos efetuados"
# ---------------------------------------------------------------------------------------------------------------

"""
Método responsável pela listagem de dados
"""
def action_list():

    show_head_system()

    validate_exists_data()

    for id in database_temp['data']:
        object_data = database_temp['data'][ id ]
        print(format_data_view(id, object_data))

    require_reload_system()


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes a opção "Calcular área"
# ---------------------------------------------------------------------------------------------------------------

"""
Método responsável pela validação do parâmetro "Cultura"

Arguments:
- value_validate: Conteúdo que deverá ser validado ( string )

Return: Dictionary
"""
def validate_crop(value_validate: str = '') -> dict:

    return_method = {'status': True}

    try:

        if value_validate.strip() == '':
            raise Exception('Deve ser definido um código válido.')

        if Helper.is_int(value_validate) == False:
            raise Exception('O código informado deve ser numérico.')

        list_crops_codes = get_crops_codes()

        if int(value_validate) not in list_crops_codes:
            raise Exception('O código informado deve representar uma das culturas disponíveis.')

    except Exception as error:

        return_method = {'status': False, 'message': error}

    return return_method


"""
Método responsável por verificar se a classe de uma determinada cultura possui o método contendo os cálculos disponíveis
"""
def validate_exist_enabled_calcs(class_crop: Crop = Crop):

    if hasattr(class_crop, 'get_enabled_calcs') == False:
        raise Exception(f'Não foi possível concluir o processo pois a cultura {class_crop.get_name()} não possui a ação necessária para exibição dos cálculos disponíveis.')


"""
Método responsável pela validação do parâmetro "Opção de cálculo"

Arguments:
- value_validate: Conteúdo que deverá ser validado ( string )

Return: Dictionary
"""
def validate_calc_option(value_validate: str = '', class_crop: Crop = Crop) -> dict:

    return_method = {'status': True}

    try:

        if value_validate.strip() == '':
            raise Exception('Deve ser definido um código válido.')

        if Helper.is_int(value_validate) == False:
            raise Exception('O código informado deve ser numérico.')

        validate_exist_enabled_calcs(class_crop)

        enabled_calcs = class_crop.get_enabled_calcs()

        list_calcs_codes = [sub_list['code'] for sub_list in enabled_calcs]

        if(int(value_validate) not in list_calcs_codes):
            raise Exception('O código informado deve representar um dos cálculos disponíveis.')

    except Exception as error:

        return_method = {'status': False, 'message': error}

    return return_method


"""
Método responsável por cadastrar dados
"""
def action_insert():

    return_step_1 = step_1()

    if return_step_1['status'] == False:
        raise Exception(f'{return_step_1['message']}')

    id = get_next_id()

    # Processo de armazenamento dos parâmetros
    database_temp['data'][ id ] = return_step_1['data']

    export_data_to_json_file()

    input(f'\nCadastro efetuado com sucesso. Pressione <enter> para exibir a listagem atualizada.')

    action_list()


"""
Método responsável por acessar a etapa 1

Return: Dictionary
"""
def step_1() -> dict:

    return_method = {'status': True, 'data': {}}

    try:

        show_head_system()

        show_crops()

        crop = input(f'Informe o código da cultura desejada: ')
        while True:
            return_validate_crop = validate_crop(crop)
            if return_validate_crop['status'] == False:
                print(f'{return_validate_crop['message']} Tente novamente: ', end = '')
                crop = input()

            else:
                break

        return_method['data']['crop'] = int(crop)

        return_step_2 = step_2(return_method['data'])

        if return_step_2['status'] == False:
            raise Exception(f'{return_step_2['message']}')

        return_method['data'].update(return_step_2['data'])

    except Exception as error:

        return_method = {'status': False, 'message': f'{error}'}

    return return_method


"""
Método responsável por acessar a etapa 2

Arguments:
- params: Dictionary contendo os parâmetros que serão utilizados no método ( dict )
    key 'crop': Código da cultura que deverá ser utilizada ( int )

Return: Dictionary
"""
def step_2(params: dict = {}) -> dict:

    return_method = {'status': True, 'data': {}}

    try:

        if 'crop' not in params or Helper.is_int(params['crop']) == False:
            raise Exception('Não foi possível iniciar o processo da etapa 2 pois o parâmetro "crop" não foi definido corretamente.');

        loading('Carregando parâmetros da cultura selecionada, por favor aguarde...')

        show_head_system()

        class_crop = get_class_crop_by_code(params['crop'])

        # Bloco referente à informações adicionais da cultura
        # > Regras: Pode ser desabilitado bastando alterar a flag abaixo para "False"
        is_show_infos = True

        if(is_show_infos == True):

            principal_local = class_crop.get_principal_local()

            print('')
            print(f'> Cultura: {class_crop.get_name()}')
            print(f'> Local: {principal_local['city']} ( {principal_local['state']} )')

            list_infos = class_crop.get_infos()

            if len(list_infos) == 0: print(f'\nNão existem informações sobre essa cultura para serem exibidas.')

            else:

                print('')

                item_count = 1

                for object_info in list_infos:
                    title_info = object_info['title'] if 'title' in object_info else ''
                    print(f'{item_count}. {title_info}')

                    if 'items' in object_info:
                        for object_info_items in object_info['items']:
                            title_info_item = object_info_items['title'] if 'title' in object_info_items and object_info_items['title'].strip() != '' else 'Descrição'
                            text_info_item = object_info_items['text'] if 'text' in object_info_items and object_info_items['text'].strip() != '' else 'N/A'
                            print(f'- {title_info_item}: {text_info_item}')

                            if 'items' in object_info_items:
                                for object_info_items_items in object_info_items['items']:
                                    title_info_item_item = object_info_items_items['title'] if 'title' in object_info_items_items and object_info_items_items['title'].strip() != '' else 'Item'
                                    text_info_item_item = object_info_items_items['text'] if 'text' in object_info_items_items and object_info_items_items['text'].strip() != '' else 'N/A'
                                    print(f'    - {title_info_item_item}: {text_info_item_item}')

                    print('')
                    item_count += 1

        back_step = input(f'> Digite "-1" para voltar à tela de seleção de culturas ou <enter> para continuar: ')
        if(back_step == '-1'): step_1()

        else:
            validate_exist_enabled_calcs(class_crop)

            print('')
            print(f'> Opções de cálculo')

            enabled_calcs = class_crop.get_enabled_calcs()

            if len(enabled_calcs) == 0:
                raise Exception('Não foi possível concluir o processo pois essa cultura não possui cálculos habilitados para execução')

            else:
                print('')

                for calcs in enabled_calcs:
                    code_calc = f'{calcs['code']}.' if 'code' in calcs else ''
                    title_calc = f'{calcs['title']}' if 'title' in calcs and calcs['title'].strip() != '' else 'Cálculo'
                    print(f'{code_calc} {title_calc}')

            print('')

            calc_option = input(f'Informe o código do cálculo desejado: ')

            while True:
                return_validate_calc_option = validate_calc_option(calc_option, class_crop)
                if return_validate_calc_option['status'] == False:
                    print(f'{return_validate_calc_option['message']} Tente novamente: ', end = '')
                    calc_option = input()

                else: break

            return_method['data']['class_crop'] = class_crop
            return_method['data']['calc_option'] = int(calc_option)

            return_step_3 = step_3(return_method['data'])
            if return_step_3['status'] == False:
                raise Exception(f'{return_step_3['message']}')

            return_method['data'].update(return_step_3['data'])

    except Exception as error:

        return_method = {'status': False, 'message': f'{error}'}

    return return_method


"""
Método responsável por acessar a etapa 3

Arguments:
- params: Dictionary contendo os parâmetros que serão utilizados no método ( dict )
    key 'class_crop': Instância da classe da cultura que deverá ser utilizada ( int )
    key 'calc_option': Código do cálculo da cultura que deverá ser utilizado ( int )

Return: Dictionary
"""
def step_3(params: dict = {}) -> dict:

    return_method = {'status': True, 'data': {}}

    try:

        if 'class_crop' not in params or isinstance(params['class_crop'], Crop) == False:
            raise Exception('Não foi possível iniciar o processo da etapa 3 pois o parâmetro "class_crop" não foi definido corretamente.');

        if 'calc_option' not in params or Helper.is_int(params['calc_option']) == False:
            raise Exception('Não foi possível iniciar o processo da etapa 3 pois o parâmetro "calc_option" não foi definido corretamente.');

        # ----------------
        # Parte 1 da etapa
        # ----------------

        show_head_system()

        principal_local = params['class_crop'].get_principal_local()

        print('')
        print(f'> Cultura: {params['class_crop'].get_name()}')
        print(f'> Local: {principal_local['city']} ( {principal_local['state']} )')

        calc = params['class_crop'].get_enabled_calcs(params['calc_option'])
        calc_name = calc['title'] if 'title' in calc and calc['title'].strip() != '' else 'Opção de cálculo'

        print(f'> Cálculo: {calc_name}')

        if 'required_params' not in calc or len(calc['required_params']) == 0:
            raise Exception(f'Não foi possível concluir o processo pois o cálculo "{calc['title']}" não possui os parâmetros necessários para preenchimento.')

        print('')
        print(f'> Preencha os parâmetros abaixo para que o cálculo possa ser efetuado.')

        return_method['data']['calc'] = calc
        return_method['data']['params_calc'] = []
        return_method['data']['result_calc'] = {}
        params_calc = {}
        item_count = 1

        for required_params in calc['required_params']:
            title_param = required_params['title'] if 'title' in required_params and required_params['title'].strip() != '' else f'Parâmetro {item_count}'
            note_param = f' {required_params['note']}' if 'note' in required_params and required_params['note'].strip() != '' else ''

            if 'param_name' not in required_params:
                raise Exception(f'Não foi possível concluir o processo de requisição do parâmetro "{title_param}" pois não foi definido o nome da key do parâmetro.')

            print('')
            param_input = input(f'{item_count}. {title_param}{note_param}: ')

            if 'validate' in required_params:
                while True:
                    return_validate_param = required_params['validate'](param_input)
                    if return_validate_param['status'] == False:
                        print(f'{return_validate_param['message']} Tente novamente: ', end = '')
                        param_input = input()

                    else: break
            
            item_count += 1
            
            params_calc[ required_params['param_name'] ] = param_input

            return_method['data']['params_calc'].append({
                'title': title_param,
                'param_name': required_params['param_name'],
                'param': param_input
            })

        loading('Executando cálculo, por favor aguarde...', 5, False)

        execute_calc = calc['calc'](params_calc)
        if execute_calc['status'] == False:
            raise Exception(execute_calc['message'])

        # ----------------
        # Parte 2 da etapa
        # ----------------

        show_head_system()

        print('')
        print(f'> Cultura: {params['class_crop'].get_name()}')
        print(f'> Local: {principal_local['city']} ( {principal_local['state']} )')
        print(f'> Cálculo: {calc_name}')
        print('')
        print(f'> Resultado: {execute_calc['data']['label']}')

        return_method['data']['result_calc'] = execute_calc['data']

    except Exception as error:

        return_method = {'status': False, 'message': f'{error}'}

    return return_method


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes a opção "Editar cálculo"
# ---------------------------------------------------------------------------------------------------------------

"""
Método responsável por editar dados
"""
def action_update():

    validate_exists_data()

    print('')
    id = input(f'Informe o ID do item que deseja editar: ')

    while validate_id(id) == False:
        print(f'Deve ser definido um parâmetro válido. Tente novamente: ', end = '')
        id = input()

    object_data = get_data_by_id(int(id))

    print(f'{format_data_view(id, object_data)}')

    print('')
    back_step = input(f'> Digite "-1" para voltar ao menu principal ou <enter> para continuar: ')
    if(back_step == '-1'): init_system()

    else:
        print('')
        print(f'> Preencha os parâmetros abaixo para que o cálculo possa ser efetuado e atualizado.')

        params_calc = {}
        params_calc_update = []
        item_count = 1

        for required_params in object_data['calc']['required_params']:
            title_param = required_params['title'] if 'title' in required_params and required_params['title'].strip() != '' else f'Parâmetro {item_count}'
            note_param = f' {required_params['note']}' if 'note' in required_params and required_params['note'].strip() != '' else ''

            if 'param_name' not in required_params:
                raise Exception(f'Não foi possível concluir o processo de requisição do parâmetro "{title_param}" pois não foi definido o nome da key do parâmetro.')

            print('')
            param_input = input(f'{item_count}. {title_param}{note_param}: ')

            if 'validate' in required_params:
                while True:
                    return_validate_param = required_params['validate'](param_input)
                    if return_validate_param['status'] == False:
                        print(f'{return_validate_param['message']} Tente novamente: ', end = '')
                        param_input = input()

                    else: break

            item_count += 1

            params_calc[ required_params['param_name'] ] = param_input

            params_calc_update.append({
                'title': title_param,
                'param_name': required_params['param_name'],
                'param': param_input
            })

        loading('Executando cálculo, por favor aguarde...', 5, False)

        execute_calc = object_data['calc']['calc'](params_calc)
        if execute_calc['status'] == False: raise Exception(execute_calc['message'])

        show_head_system()

        print('')
        print(f'> {object_data['class_crop'].get_name()}')
        print('')
        print(f'> {object_data['calc']['title']}')
        print('')
        print(f'> Resultado: {execute_calc['data']['label']}')

        # Processo de atualização dos parâmetros
        object_data['params_calc'] = params_calc_update
        object_data['result_calc'] = execute_calc['data']

        database_temp['data'][ int(id) ] = object_data

        export_data_to_json_file()

        input(f'\nCadastro atualizado com sucesso. Pressione <enter> para exibir a listagem atualizada.')

        action_list()


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes a opção "Excluir cálculo"
# ---------------------------------------------------------------------------------------------------------------

"""
Método responsável por excluir dados
"""
def action_delete():

    validate_exists_data()

    print('')
    id = input(f'Informe o ID do item que deseja excluir: ')

    while validate_id(id) == False:
        print(f'Deve ser definido um parâmetro válido. Tente novamente: ', end = '')
        id = input()

    get_data_by_id(int(id))

    del database_temp['data'][ int(id) ]

    export_data_to_json_file()

    input(f'\nExclusão efetuada com sucesso. Pressione <enter> para exibir a listagem atualizada.')

    action_list()


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes a opção "Visualizar cálculo"
# ---------------------------------------------------------------------------------------------------------------

"""
Método responsável por visualizar dados
"""
def action_view():

    validate_exists_data()

    print('')
    id = input(f'Informe o ID do item que deseja visualizar: ')

    while validate_id(id) == False:
        print(f'Deve ser definido um parâmetro válido. Tente novamente: ', end = '')
        id = input()

    object_data = get_data_by_id(int(id))

    print(f'{format_data_view(id, object_data)}')

    require_reload_system()


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes a opção "Executar relatório de cálculos em R"
# ---------------------------------------------------------------------------------------------------------------

def action_execute_calc_report_r():

    validate_exists_data()

    print('')

    current_dir_path = get_current_path_dir()
    r_file_name = 'report_data.R'
    full_path = f'{current_dir_path}{os.sep}{r_file_name}'

    if os.path.exists(full_path) == False:
        raise Exception('Não foi possível concluir o processo pois o arquivo informado para execução do relatório de cálculos em R não existe.')

    subprocess.run(['cmd', '/c', 'Rscript', full_path])

    require_reload_system()


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes a opção "Executar relatório meteorológico em R"
# ---------------------------------------------------------------------------------------------------------------

def action_execute_weather_report_r():

    print('')

    current_dir_path = get_current_path_dir()
    r_file_name = 'report_weather.R'
    full_path = f'{current_dir_path}{os.sep}{r_file_name}'

    if os.path.exists(full_path) == False:
        raise Exception('Não foi possível concluir o processo pois o arquivo informado para execução do relatório meteorológico em R não existe.')

    subprocess.run(['cmd', '/c', 'Rscript', full_path])

    require_reload_system()


# ---------------------------------------------------------------------------------------------------------------
# Métodos referentes a opção "Sair"
# ---------------------------------------------------------------------------------------------------------------

"""
Método responsável pela saída do sistema
"""
def exit():

    print('')
    print(f'Obrigado por utilizar o sistema.\n')


# ---------------------------------------------------------------------------------------------------------------

"""
Ação responsável por executar a inicialização do sistema
"""
if(__name__ == '__main__'):
    init_system()

