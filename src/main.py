import os
from data.config import JSON_FILENAME
from utils import *

#выбор файла json для загрузки данных
data_path = os.path.join("..", "data", JSON_FILENAME)

#чтение данных из файла json
json_data = load_json(data_path)

#вывод последних 5 операций
last_five_operations_data = get_last_five_executed_operetions(json_data)

#вывод данных в требуемом формате
for i in last_five_operations_data:
    format_output(i)