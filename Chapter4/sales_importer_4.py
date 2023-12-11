import sales

def display_title():
    print()
    print("SALES DATA IMPORTER")
    print()
    print("Enter Sales Data")

def display_total(total):
  # Display the total
    print("Total Sales")
    print()
    print(f"${total:.2f}\n")
  
def get_quarter(month):
     # Get quarter based on month
    if month >= 1 and month <= 3:
      quarter = 1
    elif month >=4 and month <=6:
      quarter = 2
    elif month >=7 and month <=9:
      quarter = 3
    elif month >=10 and month <=12:
      quarter = 4
    else:
       quarter = 0
    return quarter

def main():
    display_title()
  
  # Variable to accumulate the total sales amount
    total = 0.0
    sale_number = 1

    # Start a loop to get sales data
    again = "y"
    while again == "y":
      amount = sales.get_amount()
      year = sales.get_year()
      month = sales.get_month()
      day = sales.get_day()
      print() 

      # Add sales to total
      total += amount
      
      # Get quarter based on month
      quarter = get_quarter(month)

      # Display sales info
      print(f"{sale_number}.\t\t{year}-{month}-{day}\t",f"Quarter {quarter}\t${amount:.2f}\n")

      # Increment sales number
      sale_number += 1

      # See if user wants to enter more sales data
      again = input("Enter more sales (y/n): ").lower()
      print()

    display_total(total)
    
    print("Bye")

# If started as the main module, call the main function
main()