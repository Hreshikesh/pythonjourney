year=int(input("Enter the year"))
if (year%4==0) or(year%400==0 and year%100!=0):
    print(f"{year} leap year")
else:
    print(f"{year} not leap year")