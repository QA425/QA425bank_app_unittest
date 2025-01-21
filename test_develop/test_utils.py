import unittest

from develop import utils


class TestUtils(unittest.TestCase):
    correct_url = "https://www.jsonkeeper.com/b/VK9M"
    incorrect_url = "https://www.jsonkeeper.com/b/VK11M"
    correct_filename = r'transactions\wrote_test_transactions.json'
    incorrect_filename = 'no_transactions.json'
    operations = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2001-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2023-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 142264268,
            "state": "CANCELLED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]

    def test_01_get_operations_url(self):
        self.assertGreater(len(utils.get_operations_url(self.correct_url)[0]), 0)
        self.assertEqual(utils.get_operations_url(self.correct_url)[1], 'INFO: Данные получены успешно!\n')
        self.assertEqual(utils.get_operations_url(self.incorrect_url), (None, 'INFO: Ошибка status_code 404\n'))

    def test_02_write_requested_data(self):
        # data = utils.get_operations_url(self.correct_url)[0]
        data = utils.get_local_operations(r'transactions\my_transactions.json')
        self.assertEqual(utils.write_requested_data('wrote_test_transactions', data),
                         ('Данные записаны успешно!', 'transactions\\wrote_test_transactions.json'))

    def test_03_get_local_operations(self):
        self.assertGreater(len(utils.get_local_operations(self.correct_filename)), 0)
        self.assertEqual(utils.get_local_operations(self.correct_filename)[0]['id'], 441945886)
        self.assertEqual(utils.get_local_operations(self.incorrect_filename), 'Файл не найден')

    def test_04_get_operations_executed(self):
        self.assertEqual(len(utils.get_operations_executed(self.operations)), 4)

    def test_05_get_operations_with_from(self):
        self.assertEqual(len(utils.get_operations_with_from(self.operations)), 4)

    def test_06_get_last_num_of_operations(self):
        self.assertEqual(len(utils.get_last_num_of_operations(self.operations, 2)), 2)
        self.assertEqual(utils.get_last_num_of_operations(self.operations, 1, 'прямая')[0]['date'],
                         '2001-07-03T18:35:29.512364')
        self.assertEqual(utils.get_last_num_of_operations(self.operations, 1, 'обратная')[0]['date'],
                         '2023-06-30T02:08:58.425572')

    def test_07_get_formatted_operations(self):
        data_to_format = utils.get_operations_with_from(self.operations)
        self.assertEqual(utils.get_formatted_operations(data_to_format)[0], """26.08.2019 Перевод организации
Maestro 1596 83** **** 5199->Счет **9589
31957.58 руб.""")
        self.assertEqual(utils.get_formatted_operations(data_to_format)[2], """30.06.2023 Перевод организации
Счет **6952->Счет **6702
9824.07 USD""")
