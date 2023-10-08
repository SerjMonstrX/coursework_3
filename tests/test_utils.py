from src.main import data_path
from src.utils import *

json_data = load_json(data_path)
def test_load_json():
    assert type(json_data[0]['id']) is int
    assert isinstance(json_data, list)
    assert json_data[0]['state'] == 'EXECUTED' or 'CANCELLED'
    assert len(json_data[0]) == 7


def test_get_last_five_executed_operetions():
    last_five_operations = get_last_five_executed_operetions(json_data)
    assert isinstance(last_five_operations, list)
    assert len(last_five_operations) <= 5 #Проверка длины, должны быть не более последних 5 успешных операций.
    for operation in last_five_operations:
        assert operation['state'] == 'EXECUTED'


def test_format_account_data():
    # Тест для счёта
    account_data = 'Счет 64686473678894779589'
    formatted_data = format_account_data(account_data)
    assert formatted_data == 'Счет **9589'

    # Тест для номера карты
    card_data = 'Maestro 1596837868705199'
    formatted_data = format_account_data(card_data)
    assert formatted_data == 'Maestro 1596 83** **** 5199'


def test_format_output(capsys):
    #Тест для вводных данных на примере одного словаря
    test_data = {
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
    }

    format_output(test_data)

    captured = capsys.readouterr()

    expected_output = (
        '\n26.08.2019 Перевод организации\n'
        'Maestro 1596 83** **** 5199 -> Счет **9589\n'
        '31957.58 руб.\n'
    )

    assert captured.out == expected_output

