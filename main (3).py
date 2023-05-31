def calculate_simple_interest(principal, time):
    rate = 5  # 5% interest rate for male non-senior citizens
    interest = (principal * rate * time) / 100
    return interest

# Example usage
principal_amount = float(input("Enter the principal amount: "))
time_period = float(input("Enter the time period (in years): "))

simple_interest = calculate_simple_interest(principal_amount, time_period)
total_amount = principal_amount + simple_interest

print("Simple Interest:", simple_interest)
print("Total Amount:", total_amount)