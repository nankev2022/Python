def calculate_simple_interest(principal, time, gender, senior_citizen):
    rate = 7 if gender.lower() == "male" and senior_citizen else 5
    interest = (principal * rate * time) / 100
    return interest

# Get input from the user
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time period (in years): "))
gender = input("Enter the gender (Male/Female): ")
senior_citizen = input("Is the customer a senior citizen? (Yes/No): ")

# Calculate the simple interest
interest = calculate_simple_interest(principal, time, gender, senior_citizen)

# Display the result
print("The simple interest is:", interest)