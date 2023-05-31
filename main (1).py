def calculate_simple_interest(principal, time):
    rate = 0.06  # 6% interest rate
    interest = (principal * rate * time) / 100
    return interest

gender = input("Enter gender (M/F): ")
is_senior_citizen = input("Are you a senior citizen? (Y/N): ")
principal = float(input("Enter principal amount: "))
time = float(input("Enter time in years: "))

if gender.upper() == 'F' and is_senior_citizen.upper() == 'N':
    interest = calculate_simple_interest(principal, time)
    print("Simple interest:", interest)
else:
    print("No interest is applicable for the given criteria.")