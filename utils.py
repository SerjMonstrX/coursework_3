import json
from datetime import datetime


def load_json(data_path):
    '''
    Функция для чтения JSON файла,
    возвращает список словарей с операциями.
    '''
    with open(data_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_last_five_executed_operetions(operations):
    '''
    Функция для получения всех операций со статусом executed,
    возвращает 5 последних операций, или все операции, если их меньше 5.
    '''
    # фильтрация операций по статусу "EXECUTED", формирование нового списка с помощью генератора списков
    executed_operations = [operation for operation in operations if operation.get('state') == "EXECUTED"]
    # сортировка словарей в списке по ключу date, ключи получаем из списка операций через лямбда-функцию
    sorted_executed_operations = sorted(executed_operations, key=lambda op: op['date'], reverse=True)
    # возвращает последние 5 успешных операций
    return sorted_executed_operations[:5] if len(sorted_executed_operations) >= 5 else sorted_executed_operations


def format_account_data(payment_data):
    '''
    Функция принимает строку с видом оплаты и номером карты/счета,
    возвращает отформатированный результат с частично скрытым номером и названием вида оплаты.
    '''
    #Если есть слово "Счет", то возвращает ** и последние 4 цифры счета
    if 'Счет' in payment_data or 'Счёт' in payment_data:
        hidden_account_number = '**' + payment_data.split()[1][-4:]
        formatted_payment_data = " ".join([payment_data.split()[0], hidden_account_number])
    # иначе возвращает номер карты со скрытыми цифрами в середине
    else:
        new_card_data = payment_data.rsplit(' ', 1)
        card_name = new_card_data[0]
        card_number = new_card_data[1]
        hidden_card_number = card_number[0:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
        formatted_payment_data = " ".join([card_name, hidden_card_number])
    return formatted_payment_data


def format_output(data):
    '''
    Функция принимает операцию в виде словаря
    возвращает финальный отформатированный результат для пользователя
    '''
    #Приведение даты к нужному формату
    formatted_date = datetime.fromisoformat(data['date']).strftime("%d.%m.%Y")

    print(f"\n{formatted_date} {data['description']}")
    print(f"{format_account_data(data['from']) if 'from' in data else ''} -> {format_account_data(data['to'])}")
    print(f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']} ")

