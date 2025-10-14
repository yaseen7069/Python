year=int(input("Enter a year:"))
if (year%4==0and year%100!=0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
