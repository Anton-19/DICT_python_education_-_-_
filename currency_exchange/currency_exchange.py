import requests
from json import JSONDecodeError


def get_rates(base_currency):
    url = f"http://www.floatrates.com/daily/{base_currency}.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.RequestException, JSONDecodeError):
        return None


def ask_for_valid_base_currency():
    while True:
        base_currency = input("Enter the currency you have (e.g., USD, EUR, ILS): > ").strip().lower()
        exchange_data = get_rates(base_currency)
        if exchange_data:
            return base_currency, exchange_data
        else:
            print("Error fetching exchange rates. Please enter a valid base currency.")


def prepare_cache(exchange_data):
    return {cur: exchange_data[cur]["rate"] for cur in ["usd", "eur"] if cur in exchange_data}


def ask_for_target_currency():
    return input("Enter the currency you want to exchange to (or press Enter to exit): > ").strip().lower()


def ask_for_amount():
    while True:
        try:
            return float(input("Enter the amount you want to exchange: > "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def check_cache(cache, target_currency, exchange_data):
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
    received_amount = amount * rate
    print(f"You received {received_amount:.2f} {target_currency.upper()}.")


def main():
    base_currency, exchange_data = ask_for_valid_base_currency()
    cache = prepare_cache(exchange_data)

    while True:
        target_currency = ask_for_target_currency()
        if not target_currency:
            break

        amount = ask_for_amount()
        rate = check_cache(cache, target_currency, exchange_data)
        if rate:
            convert_currency(amount, rate, target_currency)


if __name__ == "__main__":
    main()

