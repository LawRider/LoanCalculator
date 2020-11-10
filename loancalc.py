import math
import sys
import argparse


def main():
    if len(sys.argv) < 5:
        print("Incorrect parameters")
        sys.exit()

    parser = argparse.ArgumentParser(description="Loan Calculator")
    parser.add_argument("--type", type=str, choices=["diff", "annuity"],
                        help="Type of payment: 'diff' or 'annuity'")
    parser.add_argument("--principal", type=float, help="Loan principal")
    parser.add_argument("--periods", type=int, help="Number of periods")
    parser.add_argument("--interest", type=float, help="Interest rate")
    parser.add_argument("--payment", type=float, help="Monthly payment")
    args = parser.parse_args()

    if args.type == "diff" and args.interest:
        diff_payment(args.principal, args.periods, args.interest)
    elif args.type == "annuity" and args.interest:
        if args.principal and args.periods and args.interest:
            annuity_payment(args.principal, args.periods, args.interest)
        elif args.payment and args.periods and args.interest:
            annuity_principal(args.payment, args.periods, args.interest)
        elif args.principal and args.payment and args.interest:
            annuity_periods(args.principal, args.payment, args.interest)
    else:
        print("Incorrect parameters")
        sys.exit()


def diff_payment(principal, periods, interest):
    nominal_interest_rate = (interest * 0.01) / 12
    total_payment = 0
    for period in range(1, periods + 1):
        payment = math.ceil(principal / periods + nominal_interest_rate *
                            (principal - (principal * (period - 1)) / periods))
        print("Month {}: payment is {}"
              .format(period, payment))
        total_payment += payment
    overpayment = math.ceil(total_payment - principal)
    print("\nOverpayment =", overpayment)


def annuity_payment(principal, periods, interest):
    nominal_interest_rate = (interest * 0.01) / 12
    payment = math.ceil(principal *
                        ((nominal_interest_rate * math.pow(1 + nominal_interest_rate, periods)) /
                         ((1 + nominal_interest_rate) ** periods - 1)))
    print("Your annuity payment = {}!"
          .format(payment))
    overpayment = math.ceil(payment * periods - principal)
    print("Overpayment =", overpayment)


def annuity_principal(payment, periods, interest):
    nominal_interest_rate = (interest * 0.01) / 12
    principal = payment / ((nominal_interest_rate * math.pow(1 + nominal_interest_rate, periods)) /
                           ((1 + nominal_interest_rate) ** periods - 1))
    print("Your loan principal = {}!"
          .format(int(principal)))
    overpayment = math.ceil(payment * periods - principal)
    print("Overpayment =", overpayment)


def annuity_periods(principal, payment, interest):
    nominal_interest_rate = (interest * 0.01) / 12
    periods = math.ceil(math.log(payment / (payment - nominal_interest_rate * principal),
                                 1 + nominal_interest_rate))
    if periods < 12:
        months_word = 'month' if periods == 1 else 'months'
        print("It will take {} {} to repay the loan!"
              .format(int(periods), months_word))
    elif periods % 12 == 0:
        years = periods / 12
        years_word = 'year' if periods == 1 else 'years'
        print("It will take {} {} to repay the loan!"
              .format(int(years), years_word))
    else:
        years = periods // 12
        years_word = 'year' if periods == 1 else 'years'
        periods %= 12
        months_word = 'month' if periods == 1 else 'months'
        print("It will take {} {} and {} {} to repay the loan!"
              .format(int(years), years_word, int(periods), months_word))
    overpayment = math.ceil(payment * periods - principal)
    print("Overpayment =", overpayment)


if __name__ == "__main__":
    main()
