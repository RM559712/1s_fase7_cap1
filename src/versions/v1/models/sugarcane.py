from custom.helper import Helper
from models.crop import Crop

class Sugarcane(Crop):

    __code = 5
    __name = 'Cana-de-açúcar'
    __principal_local = {'state': 'SP', 'city': 'São Carlos'}
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

        self.reset_infos()

        self.append_infos({
            'code': 'ITEM_1',
            'title': 'Preparação do Solo',
            'items':[
                {
                    'code': 'ITEM_1_1', 
                    'title': 'Período', 
                    'text': 'Meses antes do plantio.'
                },{
                    'code': 'ITEM_1_2', 
                    'title': 'Ações', 
                    'text': 'Análise do solo, correção de acidez, aração, gradagem, subsolagem, revolvimento, descompactação, sulcação e adubação. Essas práticas criam condições adequadas para o estabelecimento e desenvolvimento da cana.'
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
                    'text': 'Pode ocorrer em três sistemas:',
                    'items': [
                        {
                            'code': 'ITEM_2_1_1', 
                            'title': 'Ano-e-meio (18 a 22 meses)', 
                            'text': 'Plantio entre janeiro e março.'
                        },{
                            'code': 'ITEM_2_1_2', 
                            'title': 'Ano (12 meses)', 
                            'text': 'Plantio entre setembro e novembro.'
                        },{
                            'code': 'ITEM_2_1_3', 
                            'title': 'Inverno', 
                            'text': 'Durante o período de estiagem, integrando fertirrigação.'
                        }
                    ]
                },{
                    'code': 'ITEM_2_2', 
                    'title': 'Ações', 
                    'text': 'Uso de mudas com espaçamento e profundidade corretos, geralmente 20 a 30 cm de profundidade e espaçamento de 1 a 1,8 metros.'
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
                    'text': 'Após o plantio, a cana-de-açúcar necessita de clima úmido e quente para germinar.'
                },{
                    'code': 'ITEM_3_2', 
                    'title': 'Ações', 
                    'text': 'Monitorar a umidade do solo e garantir irrigação adequada, especialmente em regiões com baixa precipitação.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_4',
            'title': 'Desenvolvimento Vegetativo',
            'items':[
                {
                    'code': 'ITEM_4_1', 
                    'title': 'Período', 
                    'text': 'Após a emergência até o início da maturação.'
                },{
                    'code': 'ITEM_4_2', 
                    'title': 'Ações', 
                    'text': 'Aplicação de herbicidas para controle de plantas daninhas, adubação de cobertura com nitrogênio e potássio, e monitoramento de pragas e doenças.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_5',
            'title': 'Maturação',
            'items':[
                {
                    'code': 'ITEM_5_1', 
                    'title': 'Período Crítico para Água', 
                    'text': 'Durante a maturação, que requer clima seco e frio para o aumento do teor de sacarose.'
                },{
                    'code': 'ITEM_5_2', 
                    'title': 'Ações', 
                    'text': 'Uso de maturadores para antecipar o acúmulo de sacarose e uniformizar a maturação.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_6',
            'title': 'Colheita',
            'items':[
                {
                    'code': 'ITEM_6_1', 
                    'title': 'Período', 
                    'text': 'Dependendo do sistema de plantio, a colheita pode ocorrer entre 12 a 22 meses após o plantio.'
                },{
                    'code': 'ITEM_6_2', 
                    'title': 'Ações', 
                    'text': 'Colher quando a cana atinge a maturidade fisiológica, garantindo a qualidade e quantidade de açúcar recuperável (ATR).'
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


