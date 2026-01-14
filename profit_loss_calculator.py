invested = float(input("How much did you invest? $"))
current = float(input("What is it worth now? $"))

difference = current - invested 

if difference > 0:
  print("Profit: $" + str(round(abs(difference), 2)))
elif difference < 0:
  print("Loss: $" + str(round(abs(difference), 2)))
else:
  print("Break even: $0.00")  
