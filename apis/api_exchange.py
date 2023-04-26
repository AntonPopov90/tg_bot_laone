import requests
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path("..") / ".env"
load_dotenv(dotenv_path=env_path)
EXCHANGE_KEY: str = os.getenv('EXCHANGE_KEY')


def get_exchange_rate(data: dict) -> dict:
    """Depending on the chosen currency,get data from exchangerate-api and returns dict with another currencies,
    multiplied on digit from user. It is possible to add another currencies"""
    currency = data['currency']
    value = data['currency_value']
    exchange_dict = {}
    if data['currency'] == 'USD':
        url = f'https://v6.exchangerate-api.com/v6/90cd4bc120e7308f4948572f/latest/{currency}'
        response = requests.get(url)
        exchange_data = response.json()
        rub = round(exchange_data['conversion_rates']['RUB']*float(value), 2)
        eur = round(exchange_data['conversion_rates']['EUR']*float(value), 2)
        exchange_dict = {f'{currency}': f'{value}', 'результат': {'Рублей РФ': rub, 'Евро': eur}}

    elif currency == 'RUB':
        url = f'https://v6.exchangerate-api.com/v6/90cd4bc120e7308f4948572f/latest/{currency}'
        response = requests.get(url)
        exchange_data = response.json()
        usd = round(exchange_data['conversion_rates']['USD']*float(value), 2)
        eur = round(exchange_data['conversion_rates']['EUR']*float(value), 2)
        exchange_dict = {f'{currency}': f'{value}', 'результат': {'Долларов США': usd, 'Евро': eur}}

    elif currency == 'EUR':
        url = f'https://v6.exchangerate-api.com/v6/90cd4bc120e7308f4948572f/latest/{currency}'
        response = requests.get(url)
        exchange_data = response.json()
        rub = round(exchange_data['conversion_rates']['RUB']*float(value), 2)
        usd = round(exchange_data['conversion_rates']['USD']*float(value), 2)
        exchange_dict = {f'{currency}': f'{value}', 'результат': {'Рублей РФ:': rub, 'Долларов США:': usd}}
    return exchange_dict
