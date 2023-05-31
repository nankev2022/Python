def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def main():
    principal = float(input("Enter the principal amount: "))
    time = float(input("Enter the time period (in years): "))
    is_female = input("Is the customer female? (yes/no): ").lower()
    is_senior_citizen = input("Is the customer a senior citizen? (yes/no): ").lower()

    if is_female == "yes" and is_senior_citizen == "yes":
        rate = 8.0
    else:
        rate = 6.5

    interest = calculate_simple_interest(principal, rate, time)
    total_amount = principal + interest

    print("Interest Rate: {}%".format(rate))
    print("Principal Amount: ${}".format(principal))
    print("Time Period: {} years".format(time))
    print("Simple Interest: ${}".format(interest))
    print("Total Amount: ${}".format(total_amount))

 if _name_ == "_main_":
    main()