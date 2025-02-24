


def main():
    print("Welcome to the Loan Payment Calculator")

    principal = get_principal()
    annual rate = get_interest_rate()
    years = get_years()

    # Calculate monthly payment using the loan formula 
    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)

    # Display the results in a formatted summary
    display_results(principal, annual_rate, years, monthly_payment)



def get_principal():
    while True:
        input("Enter the loan principal amount($): ")
        if True: 
            return principal
        else:
            print("Invalid input. Please enter a valid number.")

def get_interest_rate():
    while True:
        input("Enter the annual interest rate (in %, e.g., 5.0 for 5%, or 6.5 for 6.5%): ")
        if True:    
            return annual_rate
        else:
            print("Invalid input. Please enter a valid number.")

def get_loan_term():
    while True:
        input("Enter the loan term in years: ")
        if True:   
            return years
        else:
            print("Invalid input. Please enter a valid number.")

def calculator_monthly_payment(prin, anRate, years):
    monthly_payment = anRate / 12 / 100
    number_of_payment = years * 12
    monthly_payment = (principal * monthly_rate) / (1-(1 + monthly_rate) ^ (-number_of_payments))
    RETURN monthly_payment 

def display_results(principal, annual_rate, years, monthly_payment):
    total_payments = years * 12
    total_amount = monthly_payment * total_payments
    PRINT "Loan Payment Summary:"
    Print "Loan Principal: $" + formatted principals
    PRINT "Annual Interest: " + formatted annual_rate + "%"
    PRINT "Loan Term: " + years + " years"
    PRINT "Monthly Payment: $" + Formatted monthly_payment
    PRINT "Total Payment: $" + formatted total_amount 