print()
print("SALES DATA IMPORTER")

print()
print("Enter Sales Data")

# Variable to accumulate the total sales amount
total = 0.0
sale_number = 1

# Start a loop to get sales data
again = "y"
while again == "y":
  amount = float(input("Amount:" + " "*5))
  year = int(input("Year:" + " "*5))
  month = int(input("Month:" + " "*5))
  day = int(input("Day:" + " "*5))
  print() 

  # Add sales to total
  total += amount

  # Get quarter based on month
  if month >= 1 and month <= 3:
    quarter = 1
  elif month >=4 and month <=6:
    quarter = 2
  elif month >=7 and month <=9:
    quarter = 3
  elif month >=10 and month <=12:
    quarter = 4

  # Display sales info
  print(f"{sale_number}.\t\t{year}-{month}-{day}\t",f"Quarter {quarter}\t${amount}\n")

  # Increment sales number
  sale_number += 1

  # See if user wants to enter more sales data
  again = input("Enter more sales (y/n): ").lower()
  print()

# Display the total
print("Total Sales")
print()
print(f"${total}\n")

print("Bye")