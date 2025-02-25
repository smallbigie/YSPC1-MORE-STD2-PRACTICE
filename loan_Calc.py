def main():
    print("Loan Calculator\n------------------")
    principal = get_principal()
    annual_rate = get_interest_rate()
    years = get_loan_term()
    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
    display_results(principal, annual_rate, years, monthly_payment)

def get_principal():
    while True:
        try:
            principal = float(input("Enter the loan principal amount ($): "))
            if principal > 0:
                return principal
            else:
                print("Error: Please enter a positive number.")
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value.")

def get_interest_rate():
    while True:
        try:
            annual_rate = float(input("Enter the annual interest rate (in %, e.g., 5.0 for 5%): "))
            if annual_rate > 0:
                return annual_rate
            else:
                print("Error: Please enter a positive number.")
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value.")

def get_loan_term():
    while True:
        try:
            years = int(input("Enter the loan term in years: "))
            if years > 0:
                return years
            else:
                print("Error: Please enter a positive integer.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer value.")

def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    number_of_payments = years * 12
    if monthly_rate == 0:
        return principal / number_of_payments
    return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)

def display_results(principal, annual_rate, years, monthly_payment):
    total_payments = years * 12
    total_amount = monthly_payment * total_payments
    print("\nLoan Payment Summary:")
    print(f"Loan Principal: ${principal:,.2f}")
    print(f"Annual Interest Rate: {annual_rate:.2f}%")
    print(f"Loan Term: {years} years")
    print(f"Monthly Payment: ${monthly_payment:,.2f}")
    print(f"Total Payment: ${total_amount:,.2f}")


if __name__ == "__main__":
    main()


