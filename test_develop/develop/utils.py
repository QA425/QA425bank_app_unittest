import json
from datetime import datetime

import requests


def get_operations_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "INFO: Данные получены успешно!\n"
        return None, f"INFO: Ошибка status_code {response.status_code}\n"
    except requests.exceptions.ConnectionError:
        return None, "INFO: Ошибка status_code requests.exceptions.ConnectionError"
    except requests.exceptions.JSONDecodeError:
        return None, "INFO: Ошибка status_code requests.exceptions.JSONDecodeError"
    return


def write_requested_data(filename, data):
    with open(fr'transactions\{filename}.json', 'w', encoding='utf-8') as file:
        json_data = json.dumps(data, ensure_ascii=False, indent=4)
        file.write(json_data)
    return f'Данные записаны успешно!', fr'transactions\{filename}.json'


def get_local_operations(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as fp:
            all_operations = json.load(fp)
    except FileNotFoundError:
        print('Файл не найден')
        return 'Файл не найден'
    return all_operations


def get_operations_executed(all_operations):
    operations_executed = []
    for operation in all_operations:
        if 'state' in operation:
            if operation['state'] == 'EXECUTED':
                operations_executed.append(operation)
    return operations_executed


def get_operations_with_from(operations_executed):
    operations_with_from = []
    for operation in operations_executed:
        if 'from' in operation:
            operations_with_from.append(operation)
    return operations_with_from


def get_last_num_of_operations(operations_with_from, num_of_operations=5, order="прямая"):
    if order == "прямая":
        param = False
    else:
        param = True
    operations_sort = sorted(operations_with_from, key=lambda operation: operation['date'], reverse=param)
    last_num_of_operations = operations_sort[0:num_of_operations]
    return last_num_of_operations


def get_formatted_operations(last_num_of_operations):
    operations_formatted = []
    for operation in last_num_of_operations:
        date = datetime.strptime(operation['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')
        description = operation['description']
        payer = operation['from'].split()
        payment_method = payer.pop(-1)
        if payer[0] == 'Счет':
            payment_method_from = f'**{payment_method[-4:]}'
        else:
            payment_method_from = f'{payment_method[:4]} {payment_method[4:6]}** **** {payment_method[-4:]}'
        payer_info = ' '.join(payer)
        recipient = f'{operation['to'].split()[0]} **{operation['to'][-4:]}'
        operation_amount = f"{operation['operationAmount']["amount"]} {operation['operationAmount']["currency"]["name"]}"
        operations_formatted.append(
            f"{date} {description}\n{payer_info} {payment_method_from}->{recipient}\n{operation_amount}"
        )
    return operations_formatted
