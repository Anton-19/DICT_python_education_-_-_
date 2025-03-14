import math
import argparse


# Обчислення диференційованих платежів
def diff_payments(principal, periods, interest):
    nominal_interest = interest / (12 * 100)
    total_payment = 0

    for m in range(1, periods + 1):
        diff_payment = math.ceil(
            (principal / periods) + nominal_interest * (principal - (principal * (m - 1) / periods)))
        total_payment += diff_payment
        print(f"Month {m}: payment is {diff_payment}")

    print(f"Overpayment = {total_payment - principal}")


# Обчислення ануїтетного платежу
def annuity_payment(principal, periods, interest):
    nominal_interest = interest / (12 * 100)
    payment = math.ceil(
        principal * (nominal_interest * (1 + nominal_interest) ** periods) / ((1 + nominal_interest) ** periods - 1))
    print(f"Your annuity payment = {payment}!")
    print(f"Overpayment = {(payment * periods) - principal}")


# Обчислення суми кредиту
def loan_principal(payment, periods, interest):
    nominal_interest = interest / (12 * 100)
    principal = math.floor(
        payment / ((nominal_interest * (1 + nominal_interest) ** periods) / ((1 + nominal_interest) ** periods - 1)))
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {(payment * periods) - principal}")


# Обчислення кількості місяців для погашення кредиту
def months_to_repay(principal, payment, interest):
    nominal_interest = interest / (12 * 100)
    periods = math.ceil(math.log(payment / (payment - nominal_interest * principal), 1 + nominal_interest))
    years, months = divmod(periods, 12)
    print(f"It will take {years} years and {months} months to repay this loan!" if years and months else
          f"It will take {years} years to repay this loan!" if years else
          f"It will take {months} months to repay this loan!")
    print(f"Overpayment = {(payment * periods) - principal}")


# Перевірка коректності введених параметрів
def check_params(args):
    if args.interest is None or args.interest <= 0:
        return False

    if args.type == "diff":
        return args.principal is not None and args.periods is not None and args.payment is None

    if args.type == "annuity":
        params = [args.principal, args.payment, args.periods]
        return params.count(None) == 1

    return False


# Головна функція
def main():
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", choices=["annuity", "diff"], required=True, help="Type of loan payment")
    parser.add_argument("--principal", type=float, help="Loan principal")
    parser.add_argument("--payment", type=float, help="Monthly payment (for annuity only)")
    parser.add_argument("--periods", type=int, help="Number of months")
    parser.add_argument("--interest", type=float, help="Loan interest (without % sign)")

    args = parser.parse_args()

    if not check_params(args):
        print("Incorrect parameters.")
        return

    if args.type == "diff":
        diff_payments(args.principal, args.periods, args.interest)
    elif args.type == "annuity":
        if args.payment is None:
            annuity_payment(args.principal, args.periods, args.interest)
        elif args.principal is None:
            loan_principal(args.payment, args.periods, args.interest)
        elif args.periods is None:
            months_to_repay(args.principal, args.payment, args.interest)


if __name__ == "__main__":
    main()


'''
Для перевірки
python credit_calculator/credit_calculator.py --type=annuity --principal=1000000 --payment=104000 --interest=10
python credit_calculator/credit_calculator.py --type=annuity --principal=1000000 --periods=60 --interest=10
python credit_calculator/credit_calculator.py --type=diff --principal=1000000 --payment=104000
python credit_calculator/credit_calculator.py --type=diff --principal=500000 --periods=8 --interest=7.8
python credit_calculator/credit_calculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6
python credit_calculator/credit_calculator.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
python credit_calculator/credit_calculator.py --type=diff --principal=1000000 --periods=10 --interest=10

'''
