from abc import ABC, abstractmethod
from custom.helper import Helper

class Crop(ABC):

    def __init__(self):
        
        pass


    @abstractmethod
    def get_code(self):

        pass


    @abstractmethod
    def get_name(self):

        pass


    @abstractmethod
    def get_principal_local(self):

        pass


    @abstractmethod
    def append_infos(self):

        pass


    @abstractmethod
    def get_infos(self):

        pass


    @abstractmethod
    def reset_infos(self):

        pass


    @abstractmethod
    def get_enabled_calcs(self):

        pass


    def _validate_infos(self, dict_info: dict = {}):

        if type(dict_info) != dict: return False

        #...

        return True


    @staticmethod
    def _validate_plants_lenght(value_validate: float = 0.00) -> dict:

        return_method = {'status': True}

        try:

            if value_validate.strip() == '':
                raise Exception('Deve ser definido um valor válido de.')

            if Helper.is_int(value_validate) == False and Helper.is_float(value_validate) == False:
                raise Exception('O valor informado deve ser inteiro ou decimal.')

            if float(value_validate) <= 0:
                raise Exception('O valor informado deve ser maior que zero.')

            # Demais validações específicas para este tipo de parâmetro...

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    @staticmethod
    def _validate_spacing_between_plants(value_validate: float = 0.00) -> dict:

        return_method = {'status': True}

        try:

            if value_validate.strip() == '':
                raise Exception('Deve ser definido um valor válido.')

            if Helper.is_int(value_validate) == False and Helper.is_float(value_validate) == False:
                raise Exception('O valor informado deve ser inteiro ou decimal.')

            if float(value_validate) <= 0:
                raise Exception('O valor informado deve ser maior que zero.')

            # Demais validações específicas para este tipo de parâmetro...

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    @staticmethod
    def _validate_spacing_between_streets(value_validate: float = 0.00) -> dict:

        return_method = {'status': True}

        try:

            if value_validate.strip() == '':
                raise Exception('Deve ser definido um valor válido.')

            if Helper.is_int(value_validate) == False and Helper.is_float(value_validate) == False:
                raise Exception('O valor informado deve ser inteiro ou decimal.')

            if float(value_validate) <= 0:
                raise Exception('O valor informado deve ser maior que zero.')

            # Demais validações específicas para este tipo de parâmetro...

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    @staticmethod
    def _validate_density(value_validate: float = 0.00) -> dict:

        return_method = {'status': True}

        try:

            if value_validate.strip() == '':
                raise Exception('Deve ser definido um valor válido.')

            if Helper.is_int(value_validate) == False and Helper.is_float(value_validate) == False:
                raise Exception('O valor informado deve ser inteiro ou decimal.')

            if float(value_validate) <= 0:
                raise Exception('O valor informado deve ser maior que zero.')

            # Demais validações específicas para este tipo de parâmetro...

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    @staticmethod
    def _validate_total_area(value_validate: float = 0.00) -> dict:

        return_method = {'status': True}

        try:

            if value_validate.strip() == '':
                raise Exception('Deve ser definido um valor válido.')

            if Helper.is_int(value_validate) == False and Helper.is_float(value_validate) == False:
                raise Exception('O valor informado deve ser inteiro ou decimal.')

            if float(value_validate) <= 0:
                raise Exception('O valor informado deve ser maior que zero.')

            # Demais validações específicas para este tipo de parâmetro...

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    @staticmethod
    def _validate_street_length(value_validate: float = 0.00) -> dict:

        return_method = {'status': True}

        try:

            if value_validate.strip() == '':
                raise Exception('Deve ser definido um valor válido.')

            if Helper.is_int(value_validate) == False and Helper.is_float(value_validate) == False:
                raise Exception('O valor informado deve ser inteiro ou decimal.')

            if float(value_validate) <= 0:
                raise Exception('O valor informado deve ser maior que zero.')

            # Demais validações específicas para este tipo de parâmetro...

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    @staticmethod
    def _validate_width_streets(value_validate: float = 0.00) -> dict:

        return_method = {'status': True}

        try:

            if value_validate.strip() == '':
                raise Exception('Deve ser definido um valor válido.')

            if Helper.is_int(value_validate) == False and Helper.is_float(value_validate) == False:
                raise Exception('O valor informado deve ser inteiro ou decimal.')

            if float(value_validate) <= 0:
                raise Exception('O valor informado deve ser maior que zero.')

            # Demais validações específicas para este tipo de parâmetro...

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    @staticmethod
    def _validate_input_rate(value_validate: float = 0.00) -> dict:

        return_method = {'status': True}

        try:

            if value_validate.strip() == '':
                raise Exception('Deve ser definido um valor válido.')

            if Helper.is_int(value_validate) == False and Helper.is_float(value_validate) == False:
                raise Exception('O valor informado deve ser inteiro ou decimal.')

            if float(value_validate) <= 0:
                raise Exception('O valor informado deve ser maior que zero.')

            # Demais validações específicas para este tipo de parâmetro...

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    @staticmethod
    def _validate_application_rate(value_validate: float = 0.00) -> dict:

        return_method = {'status': True}

        try:

            if value_validate.strip() == '':
                raise Exception('Deve ser definido um valor válido.')

            if Helper.is_int(value_validate) == False and Helper.is_float(value_validate) == False:
                raise Exception('O valor informado deve ser inteiro ou decimal.')

            if float(value_validate) <= 0:
                raise Exception('O valor informado deve ser maior que zero.')

            # Demais validações específicas para este tipo de parâmetro...

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    def calc_area_by_spacing(self, params: dict = {}) -> dict:

        return_method = {'status': True, 'data': {}}

        try:

            return_validate_plants_lenght = self._validate_plants_lenght(params['plants_lenght'])
            if return_validate_plants_lenght['status'] == False:
                raise Exception(return_validate_plants_lenght['message'])
            
            return_validate_spacing_between_plants = self._validate_spacing_between_plants(params['spacing_between_plants'])
            if return_validate_spacing_between_plants['status'] == False:
                raise Exception(return_validate_spacing_between_plants['message'])
            
            return_validate_spacing_between_plants = self._validate_spacing_between_plants(params['spacing_between_streets'])
            if return_validate_spacing_between_plants['status'] == False:
                raise Exception(return_validate_spacing_between_plants['message'])

            total_area_m2 = (float(params['plants_lenght']) * float(params['spacing_between_plants']) * float(params['spacing_between_streets']))

            return_method['data']['total_area_m2'] = total_area_m2
            return_method['data']['label'] = f'Área total em metros quadrados: {Helper.format_float(total_area_m2)} m2.'

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    def calc_area_by_density(self, params: dict = {}) -> dict:

        return_method = {'status': True, 'data': {}}

        try:

            return_validate_plants_lenght = self._validate_plants_lenght(params['plants_lenght'])
            if return_validate_plants_lenght['status'] == False:
                raise Exception(return_validate_plants_lenght['message'])

            return_validate_density = self._validate_density(params['density'])
            if return_validate_density['status'] == False:
                raise Exception(return_validate_density['message'])

            total_area_hectares = (float(params['plants_lenght']) / float(params['density']))
            total_area_m2 = (total_area_hectares * 10000)

            return_method['data']['total_area_hectares'] = total_area_hectares
            return_method['data']['total_area_m2'] = total_area_m2
            return_method['data']['label'] = f'Área total em hectares: {Helper.format_float(total_area_hectares)}; Área total em metros quadrados: {Helper.format_float(total_area_m2)} m2.'

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    def calc_street_length_by_planting_area(self, params: dict = {}) -> dict:

        return_method = {'status': True, 'data': {}}

        try:

            return_validate_total_area = self._validate_total_area(params['total_area'])
            if return_validate_total_area['status'] == False:
                raise Exception(return_validate_total_area['message'])

            return_validate_street_length = self._validate_street_length(params['street_length'])
            if return_validate_street_length['status'] == False:
                raise Exception(return_validate_street_length['message'])

            return_validate_spacing_between_streets = self._validate_spacing_between_streets(params['spacing_between_streets'])
            if return_validate_spacing_between_streets['status'] == False:
                raise Exception(return_validate_spacing_between_streets['message'])

            return_validate_width_streets = self._validate_width_streets(params['width_streets'])
            if return_validate_width_streets['status'] == False:
                raise Exception(return_validate_width_streets['message'])

            width = (float(params['total_area']) / float(params['street_length']))
            number_streets = (width / (float(params['spacing_between_streets']) * float(params['width_streets'])))

            return_method['data']['number_streets'] = number_streets
            return_method['data']['label'] = f'Quantidade total de ruas: {Helper.format_float(number_streets)}.'

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    def calc_plants_length_by_street_length(self, params: dict = {}) -> dict:

        return_method = {'status': True, 'data': {}}

        try:

            return_validate_street_length = self._validate_street_length(params['street_length'])
            if return_validate_street_length['status'] == False:
                raise Exception(return_validate_street_length['message'])

            return_validate_spacing_between_plants = self._validate_spacing_between_plants(params['spacing_between_plants'])
            if return_validate_spacing_between_plants['status'] == False:
                raise Exception(return_validate_spacing_between_plants['message'])

            number_plants = (float(params['street_length']) / float(params['spacing_between_plants']))

            return_method['data']['number_plants'] = number_plants
            return_method['data']['label'] = f'Quantidade total de plantas: {Helper.format_float(number_plants)}.'

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    def calc_input_length_by_street_length(self, params: dict = {}) -> dict:

        return_method = {'status': True, 'data': {}}

        try:

            return_validate_street_length = self._validate_street_length(params['street_length'])
            if return_validate_street_length['status'] == False:
                raise Exception(return_validate_street_length['message'])

            return_validate_width_streets = self._validate_width_streets(params['width_streets'])
            if return_validate_width_streets['status'] == False:
                raise Exception(return_validate_width_streets['message'])

            return_validate_input_rate = self._validate_input_rate(params['input_rate'])
            if return_validate_input_rate['status'] == False:
                raise Exception(return_validate_input_rate['message'])

            street_area = (float(params['street_length']) * float(params['width_streets']))
            number_input_street = (street_area * float(params['input_rate']))

            return_method['data']['number_input_street'] = number_input_street
            return_method['data']['label'] = f'Quantidade total de insumos por rua: {Helper.format_float(number_input_street)}.'

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


    def calc_inpu_length_by_rate_meter(self, params: dict = {}) -> dict:

        return_method = {'status': True, 'data': {}}

        try:

            return_validate_total_area = self._validate_total_area(params['total_area'])
            if return_validate_total_area['status'] == False:
                raise Exception(return_validate_total_area['message'])

            return_validate_street_length = self._validate_street_length(params['street_length'])
            if return_validate_street_length['status'] == False:
                raise Exception(return_validate_street_length['message'])

            return_validate_width_streets = self._validate_width_streets(params['width_streets'])
            if return_validate_width_streets['status'] == False:
                raise Exception(return_validate_width_streets['message'])

            return_validate_application_rate = self._validate_application_rate(params['application_rate'])
            if return_validate_application_rate['status'] == False:
                raise Exception(return_validate_application_rate['message'])

            number_input_street = (float(params['street_length']) * float(params['application_rate']))
            street_area = (float(params['street_length']) * float(params['width_streets']))
            number_streets = (float(params['total_area']) / street_area)
            total_input = (number_input_street * number_streets)

            return_method['data']['total_input'] = total_input
            return_method['data']['label'] = f'Quantidade total de insumos: {Helper.format_float(total_input)}.'

        except Exception as error:

            return_method = {'status': False, 'message': f'{error}'}

        return return_method


