from custom.helper import Helper
from models.crop import Crop

class Coffe(Crop):

    __code = 1
    __name = 'Café'
    __principal_local = {'state': 'MG', 'city': 'Patrocínio'}
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

        if(self._validate_infos(dict_info) == True):
            self.__infos.append(dict_info)


    def get_infos(self) -> list:

        return self.__infos


    def reset_infos(self):

        self.__infos = []


    def append_standard_infos(self):

        self.append_infos({
            'code': 'ITEM_1',
            'title': 'Escolha da Área',
            'items':[
                {
                    'code': 'ITEM_1_1', 
                    'title': 'Período', 
                    'text': 'Antes do plantio.'
                }, {
                    'code': 'ITEM_1_2', 
                    'title': 'Ações', 
                    'text': 'Selecionar uma área com boa drenagem, evitando terrenos propensos a ventos fortes e frios. O café se desenvolve melhor em altitudes acima de 800 metros para o café arábica.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_2',
            'title': 'Análise e Correção do Solo',
            'items':[
                {
                    'code': 'ITEM_2_1', 
                    'title': 'Período', 
                    'text': 'Antes do plantio.'
                },{
                    'code': 'ITEM_2_2', 
                    'title': 'Ações', 
                    'text': 'Realizar análise do solo para corrigir acidez e fertilidade. A correção do solo pode incluir a aplicação de calcário e adubos específicos para suprir deficiências de macro e micronutrientes.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_3',
            'title': 'Escolha da Variedade e Produção de Mudas',
            'items':[
                {
                    'code': 'ITEM_3_1', 
                    'title': 'Período', 
                    'text': 'Antes do plantio.'
                },{
                    'code': 'ITEM_3_2', 
                    'title': '', 
                    'text': 'Escolher variedades adequadas ao clima e solo da região. As mudas devem ser produzidas em viveiros e estar prontas para o plantio após cerca de 9 meses.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_4',
            'title': 'Plantio',
            'items':[
                {
                    'code': 'ITEM_4_1', 
                    'title': 'Período', 
                    'text': 'Geralmente durante a estação chuvosa para garantir umidade adequada.'
                },{
                    'code': 'ITEM_4_2', 
                    'title': 'Ações', 
                    'text': 'Plantar as mudas com espaçamento adequado, geralmente de 1,75 a 2,00 metros entre linhas e 0,5 metros entre plantas para plantio adensado.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_5',
            'title': 'Crescimento e Desenvolvimento',
            'items':[
                {
                    'code': 'ITEM_5_1', 
                    'title': 'Período', 
                    'text': 'Desde o plantio até a maturidade produtiva.'
                },{
                    'code': 'ITEM_5_2', 
                    'title': 'Ações', 
                    'text': 'Realizar adubações periódicas, controle de ervas daninhas, e monitoramento de pragas e doenças. A irrigação deve ser feita conforme necessário, evitando excesso de água.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_6',
            'title': 'Floração e Frutificação',
            'items':[
                {
                    'code': 'ITEM_6_1', 
                    'title': 'Período Crítico para Água', 
                    'text': 'Durante a floração e frutificação, é importante garantir a disponibilidade de água para o desenvolvimento dos frutos.'
                },{
                    'code': 'ITEM_6_2', 
                    'title': 'Ações', 
                    'text': 'Continuar com adubações e controle de pragas, além de monitorar a umidade do solo.'}
            ]
        })

        self.append_infos({
            'code': 'ITEM_7',
            'title': 'Colheita',
            'items':[
                {
                    'code': 'ITEM_7_1', 
                    'title': 'Período', 
                    'text': 'O café leva de 2 a 3 anos para iniciar a produção após o plantio. A colheita ocorre quando os frutos atingem a maturidade, geralmente entre maio e setembro no Brasil.'
                },{
                    'code': 'ITEM_7_2', 
                    'title': 'Ações', 
                    'text': 'A colheita pode ser manual ou mecanizada, dependendo do tamanho e condições da lavoura. A colheita manual é mais cuidadosa, enquanto a mecanizada é mais rápida e econômica.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_8',
            'title': 'Pós-Colheita',
            'items':[
                {
                    'code': 'ITEM_8_1', 
                    'title': 'Período', 
                    'text': 'Imediatamente após a colheita.'
                },{
                    'code': 'ITEM_8_2', 
                    'title': 'Ações', 
                    'text': 'Processamento dos grãos, que inclui lavagem, secagem e retirada da polpa. Essas etapas são cruciais para a qualidade final do café, influenciando sabor e aroma. O ciclo produtivo do café é longo, com plantas sendo produtivas por até 20 a 30 anos. O manejo adequado em cada etapa é essencial para garantir alta produtividade e qualidade do café.'
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


