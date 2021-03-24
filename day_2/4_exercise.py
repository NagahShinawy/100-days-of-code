YEARS = 90
age = int(input("Enter Your Age:"))
left_by_years = YEARS - age
left_by_months = left_by_years * 12

left_by_weeks = left_by_years * 52

left_by_days = left_by_years * 365

print(
    f"Years:{left_by_years} , Months:{left_by_months}, weeks:{left_by_weeks}, days:{left_by_days} left"
)
