monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

monthly_Savings = float(monthly_income) - float(monthly_expenses)

print(f"Your monthly savings are ${monthly_Savings:.0f}.")
annual_interest_rate = monthly_Savings * 12 * 0.05

Projected_Savings = monthly_Savings * 12 + int(annual_interest_rate)
print(f"Projected savings after one year, with interest, is: ${Projected_Savings:.0f}.")