import math
import argparse


# converts the given month into years and month
def convert_months_years(months):
    if months > 11:
        years = months // 12
        months = months % 12
        if years > 1:
            year_string = f"{years} years"
        else:
            year_string = f"{years} year"

        if months == 0:
            return year_string
        elif months > 1:
            return f"{year_string} and {months} months"
        return f"{year_string} and {months} month"
    else:
        if months > 1:
            return f"{months} months"
        return f"{months} month"


# method for type "n" for number of monthly payments
def calculate_months(loan_amount, monthly_payment, loan_interest):
    loan_amount = loan_amount if loan_amount else int(input("Enter the loan principal:"))
    monthly_payment = monthly_payment if monthly_payment else int(input("Enter the monthly payment:"))
    loan_interest = loan_interest if loan_interest else float(input("Enter the loan interest:"))

    i = loan_interest / (12 * 100)
    base = 1 + i
    x = (monthly_payment / (monthly_payment - i * loan_amount))
    n = math.ceil(math.log(x, base))
    print(f"It will take {convert_months_years(n)} to repay this loan!")


# method for type "a" for annuity monthly payment amount
def calculate_monthly_amount(loan_amount, months_count, loan_interest):
    loan_amount = loan_amount if loan_amount else int(input("Enter the loan principal:"))
    months_count = months_count if months_count else int(input("Enter the number of periods:"))
    loan_interest = loan_interest if loan_interest else float(input("Enter the loan interest:"))
    i = loan_interest / 100 / 12

    c = pow((1 + i), months_count)
    a = loan_amount * (i * c) / (c - 1)

    payment = math.ceil(a)

    print(f"Your monthly payment = {payment}!")


# method for type "p" for loan principal
def loan_principal(annuity_payment, periods, loan_interest):
    payment = annuity_payment if annuity_payment else float(input("Enter the annuity payment:"))
    periods = periods if periods else int(input("Enter the number of periods:"))
    loan_interest = loan_interest if loan_interest else float(input("Enter the loan interest:"))
    i = loan_interest / 100 / 12

    c = pow((1 + i), periods)
    p = payment / ((i * c) / (c - 1))  # derived principal

    p = math.ceil(p)
    print(f"Your loan principal = {p}!")


def calculate_diff(principal, periods, interest):
    i = interest / (12 * 100)
    sum_ = 0
    for m in range(1, periods + 1):
        D = principal / periods + i * (principal - ((principal * (m - 1)) / periods))
        sum_ += math.ceil(D)
        print(f"Month {m}: payment is {math.ceil(D)}")

    print(f"\nOverpayment = {sum_ - principal}")


def calculate_annuity(principal, payment, periods, interest):
    i = interest / (12 * 100)
    sum_ = 0
    overpayment = 0
    if principal > 0 and payment > 0:
        # principal, payment, interest
        period_count = math.ceil(principal / payment)

        pow((1 + i), periods) = (principal * i * principal * pow((1 + i), periods) + payment) / payment

        overpayment = sum_ - principal

        print(f"It will take {convert_months_years(period_count)} to repay this loan!")
    elif principal > 0 and periods > 0:
        c = pow((1 + i), periods)
        a = principal * (i * c) / (c - 1)
        print(f"Your annuity payment = {a}!")
        overpayment = periods * a - principal
    else:
        # payment, periods, interest
        c = pow((1 + i), periods)
        calculated_principal = (payment * (c -1)) / (i * c)
        overpayment = (periods * payment) - calculated_principal
        print(f"Your loan principal = {calculated_principal}!")

    print(f"Overpayment = {overpayment}")


parser = argparse.ArgumentParser()
parser.add_argument("--type", "-t", choices=["annuity", "diff"],
                    required=True, help="the type of payment")
#
parser.add_argument("--payment",
                    help="monthly payment amount")
# is used for calculations of both types of payment.
# You can get its value if you know the interest, annuity payment, and number of months.
parser.add_argument("-p", "--principal",
                    help="used for calculations of both types of payment")
# denotes the number of months needed to repay the loan.
# It's calculated based on the interest, annuity payment, and principal.
parser.add_argument("-P", "--periods",
                    help="denotes the number of months needed to repay the loan")
#  is specified without a percent sign. Note that it can accept a floating-point value.
#  Our loan calculator can't calculate the interest, so it must always be provided.
parser.add_argument("-i", "--interest", required=True,
                    help="is specified without a percent sign")

args = parser.parse_args()

principal_argument = int(args.principal) if args.principal else 0
periods_argument = int(args.periods) if args.periods else 0
interest_argument = float(args.interest) if args.interest else 0
payment_argument = int(args.payment) if args.payment else 0

if not args.type or not args.interest or args.type == "diff" and args.payment:
    print("Incorrect parameters")
elif principal_argument < 0 or periods_argument < 0 or interest_argument < 0 or payment_argument < 0:
    print("Incorrect parameters")
elif args.type == "diff":
    calculate_diff(principal_argument, periods_argument, interest_argument)
else:
    calculate_annuity(principal_argument, payment_argument, periods_argument, interest_argument)

# calculation_type = None
# while calculation_type is None:
#     calculation_type = input("""What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:""")
#     if len(calculation_type) > 1 or calculation_type != "n" and calculation_type != "p" and calculation_type != "a":
#         print("unknown calculation type!")
#         calculation_type = None

# if calculation_type == "n":
#     calculate_months()
# elif calculation_type == "a":
#     calculate_monthly_amount()
# elif calculation_type == "p":
#    loan_principal()
