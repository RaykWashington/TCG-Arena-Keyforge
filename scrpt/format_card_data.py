import jmespath
import json
import requests


data_path = ''
card_data = ''

with open(data_path, 'r') as file:
    card_data = file.read

