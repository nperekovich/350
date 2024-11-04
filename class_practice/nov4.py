def main():
  
  INT = 133 #constant per-day for international travel
  DOM = 54 #constant per-day for domestic travel

  
  print("Domestic (1) or International (2)? Defaults to Domestic if left empty or is not 1 or 2.")
  multiple = int(input("Enter individual region code: #"))

  cost = DOM #defaulting behaviour

  if multiple == 2 : #change cost to international
    cost = INT
  
  if multiple != 1 | 2:
    multiple = 1 #clean the input for text output

  print("")
  days = int(input("How many days of travel? Defaults to 5 if left empty."))

  total = days*cost
  
  print("")
  print("You are spending "+ str(days) + " days in cost area " + str(multiple)+ " for a total cost of $"+str(total))


main()
