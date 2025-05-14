import json
import boto3
import os

def lambda_handler(dict_event, context):

    dict_return = {'status': True, 'dict_data': {}}

    try:

        if 'body' not in dict_event or not dict_event['body']:
            raise Exception(f'Não foi possível concluir o processo pois nenhum conteúdo foi recebido.')

        dict_params = json.loads(dict_event['body'])

        msm_id = dict_params.get('msm_id')
        if not msm_id:
            raise Exception(f'Não foi possível concluir o processo pois não foi definida a referência da medição.')

        sns_name = dict_params.get('sns_name')
        if not sns_name:
            raise Exception(f'Não foi possível concluir o processo pois não foi definido o nome do sensor.')

        pln_name = dict_params.get('pln_name')
        if not pln_name:
            raise Exception(f'Não foi possível concluir o processo pois não foi definido o nome da plantação.')

        msm_value = dict_params.get('msm_value')
        if not msm_value:
            raise Exception(f'Não foi possível concluir o processo pois não foi definido o valor da medição.')

        msm_insert_date = dict_params.get('msm_insert_date')
        if not msm_insert_date:
            raise Exception(f'Não foi possível concluir o processo pois não foi definida a data e hora da medição.')

        str_message = f'Uma medição foi cadastrada a partir do sensor "{sns_name}" na plantação "{pln_name}" com o valor de {msm_value} em {msm_insert_date}.'

        object_sns_client = boto3.client('sns', region_name = 'us-east-1')
        object_response = object_sns_client.publish(
            TopicArn = os.getenv('SNS_TOPIC_ARN'),
            Message = str_message,
            Subject = 'Cadastro de medição'
        )

        dict_return['dict_data'] = {
            'dict_params': dict_params,
            'str_message': str_message
        }

    except Exception as error:

        dict_return = {'status': False, 'message': error}

    return dict_return