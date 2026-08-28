miles_per_day = float(input("How many miles do you drive per day? "))
mpg = float(input("What is your vehicle's MPG? "))
gas_price = float(input("What is the current gas price per gallon? "))
days_per_week = int(input("How many days per week do you commute? "))

gallons_per_day = miles_per_day / mpg
daily_cost = gallons_per_day * gas_price
weekly_cost = daily_cost * days_per_week
monthly_cost = weekly_cost * 4.33
yearly_cost = weekly_cost * 52

print("\n--- Commute Cost Summary ---")
print(f"Daily fuel cost: ${daily_cost:.2f}")
print(f"Weekly fuel cost: ${weekly_cost:.2f}")
print(f"Monthly fuel cost: ${monthly_cost:.2f}")
print(f"Yearly fuel cost: ${yearly_cost:.2f}")