class MultiplyTable():
    description="Generates Multiplication table"
    def table(n):
        for i in range(1,val+1): # For every number between 2 and n
            print("\nMultiplication table for %d\n"%i)
            for j in range(1,11):
                print("%d x %d = %d"%(i,j,i*j))

print()
print("=============================================")
print("| Welcome to Multiplication Table Generator |")
print("|          created by Snehal Suman          |")
print("|       of Lovely Professional University   |")
print("|                Section: K22FG             |")
print("|              Roll No: RK22FGA61           |")
print("=============================================")
print()
while True:
      n=int(input("Press 1 to generate story and 2 to exit: "))
      print()
      if n == 1:
        val=int(input("Enter the value for the table : "))
        print(" ------------------------ ")
        print("|  Multiplication Table  |")
        print(" ------------------------ ")
        MultiplyTable.table(val)
        print()
      elif n==2:
        print("Thank you for using Multiplication Table Generator Have a nice day.")
        print()
        break
      else:
        print("Invalid Input! Try again.")
        print()




