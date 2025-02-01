import requests
from datetime import datetime
import locale
import time

try:
    locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
except locale.Error:
    print("Локаль 'ru_RU.UTF-8' не поддерживается этой системой.")

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

usd_params = {"DT": "", "val_id": "R01235", "_": str(int(time.time() * 1000))}
eur_params = {"DT": "", "val_id": "R01239", "_": str(int(time.time() * 1000))}
cny_params = {"DT": "", "val_id": "R01375", "_": str(int(time.time() * 1000))}

url = "https://www.cbr.ru/cursonweek/"

for curs, currency in zip([usd_params, eur_params, cny_params], ["USD", "EUR", "CNY"]):
    print(currency)
    try:
        response = requests.get(url=url, headers=headers, params=curs)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        continue

    for el in data:
        date_str = el.get("data", "").split("T")[0]
        try:
            data_obj = datetime.strptime(date_str, "%Y-%m-%d")
            date = data_obj.strftime("%d %B %Y г.")
            rate = round(el.get("curs", 0), 2)
            print(f"Дата: {date} | Курс: {rate} руб.")
        except ValueError:
            print(f"Ошибка в формате даты: {date_str}")
    print("-" * 15)
