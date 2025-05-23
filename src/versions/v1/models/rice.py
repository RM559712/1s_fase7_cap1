from custom.helper import Helper
from models.crop import Crop

class Rice(Crop):

    __code = 3
    __name = 'Arroz'
    __principal_local = {'state': 'RS', 'city': 'Cerro Uruguaiana'}
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
            'title': 'Escolha do Local',
            'items':[
                {
                    'code': 'ITEM_1_1', 
                    'title': 'Período', 
                    'text': 'Antes do plantio.'
                },{
                    'code': 'ITEM_1_2', 
                    'title': 'Ações', 
                    'text': 'Escolher locais planos ou com leve declive para evitar encharcamentos. O solo deve ser úmido, bem drenado, rico em nutrientes e com pH entre 5,5 e 6,5.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_2',
            'title': 'Preparo do Solo',
            'items':[
                {
                    'code': 'ITEM_2_1', 
                    'title': 'Período', 
                    'text': '30 a 45 dias antes do plantio.'
                },{
                    'code': 'ITEM_2_2', 
                    'title': 'Ações', 
                    'text': 'Arar e nivelar a terra. Em áreas de cultivo contínuo, realizar rotação de culturas para evitar pragas e doenças.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_3',
            'title': 'Escolha da Variedade',
            'items':[
                {
                    'code': 'ITEM_3_1', 
                    'title': 'Período', 
                    'text': 'Antes do plantio.'
                },{
                    'code': 'ITEM_3_2', 
                    'title': 'Ações', 
                    'text': 'Escolher variedades adaptadas ao tipo de cultivo (irrigado ou sequeiro) e à região. Variedades resistentes à seca são preferíveis para arroz de sequeiro.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_4',
            'title': 'Plantio',
            'items':[
                {
                    'code': 'ITEM_4_1', 
                    'title': 'Período Arroz Irrigado', 
                    'text': 'Entre julho e agosto, ou entre outubro e janeiro, dependendo da região.'
                },{
                    'code': 'ITEM_4_2', 
                    'title': 'Arroz de Sequeiro', 
                    'text': 'Entre outubro e dezembro, podendo se estender até janeiro.'
                },{
                    'code': 'ITEM_4_3', 
                    'title': 'Ações', 
                    'text': 'Plantar sementes bem formadas e livres de doenças. O arroz irrigado requer inundação dos campos, enquanto o arroz de sequeiro depende da umidade natural do solo.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_5',
            'title': 'Manejo da Água',
            'items':[
                {
                    'code': 'ITEM_5_1', 
                    'title': 'Período Crítico para Água', 
                    'text': 'Durante todo o ciclo de cultivo para arroz irrigado.'
                },{
                    'code': 'ITEM_5_2', 
                    'title': 'Ações', 
                    'text': 'Manter os campos inundados por pelo menos 10 semanas durante a estação de crescimento, drenando a água apenas para a colheita.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_6',
            'title': 'Controle de Plantas Daninhas e Pragas',
            'items':[
                {
                    'code': 'ITEM_6_1', 
                    'title': 'Período', 
                    'text': 'Durante o ciclo de crescimento.'
                },{
                    'code': 'ITEM_6_2', 
                    'title': 'Ações', 
                    'text': 'Aplicação de herbicidas e pesticidas conforme necessário. O controle de ervas daninhas pode ser auxiliado pela lâmina de água no arroz irrigado.'
                }
            ]
        })

        self.append_infos({
            'code': 'ITEM_7',
            'title': 'Desenvolvimento Vegetativo e Reprodutivo',
            'items':[
                {
                    'code': 'ITEM_7_1', 
                    'title': 'Período', 
                    'text': 'O ciclo completo varia de 100 a 155 dias, dependendo do sistema de cultivo e da cultivar.'
                },{
                    'code': 'ITEM_7_2', 
                    'title': 'Ações', 
                    'text': 'Monitorar a saúde das plantas e aplicar fertilizantes conforme necessário para garantir um bom desenvolvimento.'
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
                    'text': 'Entre 100 e 140 dias para arroz irrigado, e entre 110 e 155 dias para arroz de sequeiro.'
                },{
                    'code': 'ITEM_8_2', 
                    'title': 'Ações', 
                    'text': 'Colher os grãos quando atingirem a maturidade, preferencialmente em períodos secos para evitar perdas por umidade. O manejo adequado em cada etapa é essencial para garantir alta produtividade e qualidade do arroz. O planejamento do plantio deve considerar o zoneamento agrícola da região e as condições climáticas para otimizar a colheita.'
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


