def get_amount() -> float:
  """
  Gets a sales amount from the user, converts it to a
  float value, and returns the float value
  """
  amount = float(input("Amount:" + " "*10))
  return amount

def get_month() -> int:
  """
  Gets a month from the user, converts it to a
  int value, and returns the int value
  """
  month = int(input("Month:" + " "*10))
  return month

def get_day() -> int:
  """
  Gets a day from the user, converts it to a
  int value, and returns the int value
  """
  day = int(input("Day:" + " "*10))
  return day

def get_year() -> int:
  """
  Gets a year from the user, converts it to a
  int value, and returns the int value
  """
  year = int(input("Year:" + " "*10))
  return year