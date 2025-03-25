import requests


def get_rates(base_currency):
    # Отримує курси валют із FloatRates для заданої базової валюти
    url = f"http://www.floatrates.com/daily/{base_currency}.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Error fetching exchange rates.")
        return {}


def check_cache(cache, target_currency, exchange_data):
    # Перевіряє наявність валюти в кеші, якщо нема — додає її
    print("Checking the cache...")
    if target_currency in cache:
        print("It is in the cache!")
        return cache[target_currency]
    else:
        print("Sorry, but it is not in the cache!")
        if target_currency in exchange_data:
            rate = exchange_data[target_currency]["rate"]
            cache[target_currency] = rate
            return rate
        else:
            print("Exchange rate not found.")
            return None


def convert_currency(amount, rate, target_currency):
    # Розраховує суму та виводить результат.
    received_amount = amount * rate
    print(f"You received {received_amount:.2f} {target_currency.upper()}.")


def main():
    # Головна функція
    base_currency = input("Enter the currency you have (e.g., USD, EUR, ILS): > ").strip().lower()
    exchange_data = get_rates(base_currency)
    cache = {cur: exchange_data[cur]["rate"] for cur in ["usd", "eur"] if cur in exchange_data}

    while True:
        target_currency = input("Enter the currency you want to exchange to (or press Enter to exit): > ").strip().lower()
        if not target_currency:
            break

        amount = float(input("Enter the amount you want to exchange: > "))
        rate = check_cache(cache, target_currency, exchange_data)

        if rate:
            convert_currency(amount, rate, target_currency)


if __name__ == "__main__":
    main()
