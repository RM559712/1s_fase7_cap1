class Helper:

    def __init__(self):
        pass

    @staticmethod
    def is_int(value):

        try:

            value_int = int(value)

            return True

        except Exception as error:

            return False

    @staticmethod
    def is_float(value):

        try:

            value_float = float(value)

            return True

        except Exception as error:

            return False

    @staticmethod
    def format_float(value):

        value = f'{value:_.2f}'
        value = value.replace('.',',').replace('_','.')
        return value