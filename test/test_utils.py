import os
from data.config import JSON_FILENAME
from utils import *
data_path = os.path.join("..", "data", JSON_FILENAME)


def test_load_json():
    data = load_json(data_path)
    assert type(data[0]['id']) is int
    assert data[0]['state'] == 'EXECUTED' or 'CANCELLED'



def test_get_last_five_executed_operetions():
    ...


def test_format_account_data():
    ...


def test_format_output():
    ...

