import json
import boto3
import os

def lambda_handler(dict_event, context):

    dict_return = {'status': True, 'dict_data': {}}

    try:

        if 'body' not in dict_event or not dict_event['body']:
            raise Exception(f'Não foi possível concluir o processo pois nenhum conteúdo foi recebido.')  

        dict_params = json.loads(dict_event['body'])

        pln_id = dict_params.get('pln_id')
        if not pln_id:
            raise Exception(f'Não foi possível concluir o processo pois não foi definida nenhuma referência de plantação.')  

        pln_name = dict_params.get('pln_name')
        if not pln_name:
            raise Exception(f'Não foi possível concluir o processo pois não foi definido o nome da plantação.')

        irg_end_date = dict_params.get('irg_end_date')
        if not irg_end_date:
            raise Exception(f'Não foi possível concluir o processo pois não foi definida a data e hora de finalização da irrigação.')

        str_message = f'A irrigação da plantação "{pln_name}" foi finalizada com sucesso em {irg_end_date}.'

        object_sns_client = boto3.client('sns', region_name = 'us-east-1')
        object_response = object_sns_client.publish(
            TopicArn = os.getenv('SNS_TOPIC_ARN'),
            Message = str_message,
            Subject = 'Finalização de irrigação'
        )

        dict_return['dict_data'] = {
            'dict_params': dict_params,
            'str_message': str_message
        }

    except Exception as error:

        dict_return = {'status': False, 'message': error}

    return dict_return