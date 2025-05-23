from custom.helper import Helper
from models.crop import Crop

class Soy(Crop):

    __code = 4
    __name = 'Soja'
    __principal_local = {'state': 'MT', 'city': 'Sorriso'}
    __infos = []


    def __init__(self):

        super().__init__()


    def get_code(self) -> int:

        return self.__code


    def get_name(self) -> str:

        return self.__name


    def get_principal_local(self) -> dict:

        return self.__principal_local


    def append_infos(self, dict_info: dict = {}):

        if(type(dict_info) == dict):
            self.__infos.append(dict_info)


    def get_infos(self) -> list:

        return self.__infos


    def reset_infos(self):

        self.__infos = []


    def append_standard_infos(self):

        self.append_infos({
            'code': 'ITEM_1',
            'title': 'Preparação do Solo',
            'items':[
                {
                    'code': 'ITEM_1_1', 
                    'title': 'Período', 
                    'text': 'Antes do plantio.'
                },{
                    'code': 'ITEM_1_2', 
                    'title': 'Ações', 
                    'text': 'Análise do solo, correção de acidez com calcário, e preparo do solo para semeadura.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_2',
            'title': 'Semeadura',
            'items':[
                {
                    'code': 'ITEM_2_1', 
                    'title': 'Período', 
                    'text': 'Geralmente de outubro a dezembro, dependendo da região.'
                },{
                    'code': 'ITEM_2_2', 
                    'title': 'Ações', 
                    'text': 'Semeadura direta é recomendada. As sementes devem ser plantadas a uma profundidade de 2 a 4 cm e cobertas levemente com terra.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_3',
            'title': 'Germinação e Emergência',
            'items':[
                {
                    'code': 'ITEM_3_1', 
                    'title': 'Período Crítico para Água', 
                    'text': 'Após o plantio, a semente precisa absorver cerca de 50% de sua massa em água para germinar adequadamente.'
                },{
                    'code': 'ITEM_3_2', 
                    'title': 'Ações', 
                    'text': 'Monitorar a umidade do solo para garantir a germinação uniforme.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_4',
            'title': 'Controle de Plantas Daninhas',
            'items':[
                {
                    'code': 'ITEM_4_1', 
                    'title': 'Período', 
                    'text': 'Cerca de 25 dias após a emergência.'
                },{
                    'code': 'ITEM_4_2', 
                    'title': 'Ações', 
                    'text': 'Aplicação de herbicidas pré e pós-emergentes para controlar plantas daninhas.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_5',
            'title': 'Desenvolvimento Vegetativo',
            'items':[
                {
                    'code': 'ITEM_5_1', 
                    'title': 'Período', 
                    'text': 'Após a emergência até o início da floração.'
                },{
                    'code': 'ITEM_5_2', 
                    'title': 'Ações', 
                    'text': 'Monitorar pragas e doenças, aplicar fungicidas preventivos se necessário.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_6',
            'title': 'Floração e Enchimento de Grãos',
            'items':[
                {
                    'code': 'ITEM_6_1', 
                    'title': 'Período Crítico para Água', 
                    'text': 'Durante a floração e enchimento de grãos, a disponibilidade de água é crucial para a produtividade.'
                },{
                    'code': 'ITEM_6_2', 
                    'title': 'Ações', 
                    'text': 'Garantir irrigação adequada ou dependência de chuvas.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_7',
            'title': 'Maturação',
            'items':[
                {
                    'code': 'ITEM_7_1', 
                    'title': 'Período', 
                    'text': 'Aproximadamente 90 a 120 dias após o plantio, dependendo da cultivar e condições climáticas.'
                },{
                    'code': 'ITEM_7_2', 
                    'title': 'Ações', 
                    'text': 'Monitorar o teor de umidade dos grãos. Aplicar dessecantes para uniformizar a maturação se necessário.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_8',
            'title': 'Colheita',
            'items':[
                {
                    'code': 'ITEM_8_1', 
                    'title': 'Período', 
                    'text': 'Quando a soja atinge a maturidade fisiológica, geralmente entre fevereiro e abril.'
                },{
                    'code': 'ITEM_8_2', 
                    'title': 'Ações', 
                    'text': 'Colher quando a umidade dos grãos estiver entre 13% e 15% para evitar perdas. O ciclo completo da soja, do plantio à colheita, dura entre 90 a 120 dias, dependendo da variedade e das condições climáticas. É importante ajustar o manejo de insumos e água conforme as necessidades específicas da cultura e as condições locais para otimizar a produtividade.'
                }
            ]
        })


    def get_enabled_calcs(self, code: int = 0) -> list | dict:

        # Regras: Caso seja necessário adicionar ou remover algum cálculo específico dessa classe, basta alterar o retorno do array abaixo
        list_calcs = [
            {
                'code': 1, 
                'title': 'Cálculo para área de plantio baseado em espaçamentos',
                'calc': self.calc_area_by_spacing,
                'required_params': [
                    {
                        'title': 'Número de plantas',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'plants_lenght',
                        'validate': self._validate_plants_lenght
                    },{
                        'title': 'Espaçamento entre plantas em metro',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'spacing_between_plants',
                        'validate': self._validate_spacing_between_plants
                    },{
                        'title': 'Espaçamento entre ruas em metro',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'spacing_between_streets',
                        'validate': self._validate_spacing_between_streets
                    }
                ]
            },{
                'code': 2,
                'title': 'Cálculo para área de plantio baseado em densidade',
                'calc': self.calc_area_by_density,
                'required_params': [
                    {
                        'title': 'Número de plantas',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'plants_lenght',
                        'validate': self._validate_plants_lenght
                    },{
                        'title': 'Densidade do plantio ( plantas por hectare )',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'density',
                        'validate': self._validate_density
                    }
                ]
            },{
                'code': 3,
                'title': 'Cálculo para quantidade de ruas baseado em área de plantio',
                'calc': self.calc_street_length_by_planting_area,
                'required_params': [
                    {
                        'title': 'Área total em metros quadrados',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'total_area',
                        'validate': self._validate_total_area
                    },{
                        'title': 'Comprimento da rua em metros',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'street_length',
                        'validate': self._validate_street_length
                    },{
                        'title': 'Espaçamento entre ruas em metros',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'spacing_between_streets',
                        'validate': self._validate_spacing_between_streets
                    },{
                        'title': 'Largura da rua em metros',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'width_streets',
                        'validate': self._validate_width_streets
                    }
                ]
            },{
                'code': 4,
                'title': 'Cálculo para quantidade de plantas baseado em quantidade de ruas',
                'calc': self.calc_plants_length_by_street_length,
                'required_params': [
                    {
                        'title': 'Comprimento da rua em metros',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'street_length',
                        'validate': self._validate_street_length
                    },{
                        'title': 'Espaçamento entre plantas em metro',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'spacing_between_plants',
                        'validate': self._validate_spacing_between_plants
                    }
                ]
            },{
                'code': 5,
                'title': 'Cálculo para quantidade de insumos baseado em quantidade de ruas',
                'calc': self.calc_input_length_by_street_length,
                'required_params': [
                    {
                        'title': 'Comprimento da rua em metros',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'street_length',
                        'validate': self._validate_street_length
                    },{
                        'title': 'Largura da rua em metros',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'width_streets',
                        'validate': self._validate_width_streets
                    },{
                        'title': 'Taxa de insumo por unidade de área ( ex.: 1kg/m2, 5l/m2, etc. )',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'input_rate',
                        'validate': self._validate_input_rate
                    }
                ]
            },{
                'code': 6,
                'title': 'Cálculo para quantidade de insumos baseado em taxa de aplicação',
                'calc': self.calc_inpu_length_by_rate_meter,
                'required_params': [
                    {
                        'title': 'Área total em metros quadrados',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'total_area',
                        'validate': self._validate_total_area
                    },{
                        'title': 'Comprimento da rua em metros',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'street_length',
                        'validate': self._validate_street_length
                    },{
                        'title': 'Largura da rua em metros',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'width_streets',
                        'validate': self._validate_width_streets
                    },{
                        'title': 'Taxa de aplicação de insumo por metro',
                        'note': '( apenas números inteiros ou decimal, por exemplo: 12345.67 [12.345,67] )',
                        'param_name': 'application_rate',
                        'validate': self._validate_application_rate
                    }
                ]
            }
        ]

        if Helper.is_int(code) == True and code > 0:
            calc_specific = {}

            for calc in list_calcs:
                if calc['code'] == code:
                    calc_specific = calc
                    break

            return calc_specific

        return list_calcs


