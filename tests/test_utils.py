from src.main import data_path
from src.utils import *

json_data = load_json(data_path)
def test_load_json():
    assert type(json_data[0]['id']) is int
    for item in json_data:
        assert isinstance(item, dict)  # Ожидаем, что каждый элемент списка является словарем
        assert 'id' in item and isinstance(item['id'], int)  # Ожидаем, что 'id' это число
        assert 'state' in item and item['state'] in ['EXECUTED','CANCELLED']  # Ожидаем 'state' из определенных значений
        assert len(item) == 7  # Ожидаем, что словарь содержит 7 ключей


def test_get_last_five_executed_operetions():
    last_five_operations = get_last_five_executed_operations(json_data)
    assert isinstance(last_five_operations, list)  # Ожидаем список
    assert len(last_five_operations) <= 5  # Ожидаем не более 5 элементов
    for operation in last_five_operations:
        assert operation['state'] == 'EXECUTED'  # Ожидаем, что каждая операция имеет статус 'EXECUTED'


def test_format_account_data():
    # Тест для счёта
    account_data = 'Счет 64686473678894779589'
    formatted_data = format_account_data(account_data)
    assert formatted_data == 'Счет **9589' #Ожидаем маску в таком виде

    # Тест для номера карты
    card_data = 'Maestro 1596837868705199'
    formatted_data = format_account_data(card_data)
    assert formatted_data == 'Maestro 1596 83** **** 5199' #Ожидаем маску в таком виде


def test_format_output(capsys):
    #Тест для вводных данных на примере одного из словарей
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

    # Вызываем функцию format_output с тестовыми данными
    format_output(test_data)

    # Перехватываем вывод функции в captured
    captured = capsys.readouterr()

    # Ожидаемый вывод после форматирования
    expected_output = (
        '\n26.08.2019 Перевод организации\n'
        'Maestro 1596 83** **** 5199 -> Счет **9589\n'
        '31957.58 руб.\n'
    )

    # Проверяем, что фактический вывод совпадает с ожидаемым выводом
    assert captured.out == expected_output

