# Expense Tracker Project

expenses = []
print("Welcome to Expense Tracker : Kharcha kam kiya karo ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2.View All Expenses")
    print("3. View Total Karcha")
    print("4. Exit")

    choice = input("Please Enter Your Choice : ")

#ADD EXPENSE
    if choice == "1":
        date= input("Kis date par kharcha kiya the?: ")
        category= input("Kis type ka kharcha kiya? (Food, Travel, Gym, Books): ")
        description= input("Aur detail dedo: ")
        amount= float(input("Enter the amount: "))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print(" Done bro. Expenses is added succesfully")

# 2. VIEW ALL EXPENSES
    elif choice == "2":
        if( len(expenses)==0):
           print("NO Expenses Added. Jao pehle kharcha karo. ")
        else:
          print("==== Ye apka sara expense ====")
          count= 1
          for eachKharcha in expenses:
               print(f"kharcha number {count}, -> {eachKharcha['date']}, {eachKharcha['category']}, {eachKharcha['description']}, {eachKharcha['amount']} ")
               count= count+1

# 3. VIEW TOTAL SPENDING
    elif choice == "3":
        total = 0
    
    
        for eachKharcha in expenses:
            total = total + eachKharcha["amount"]

        print("\nTOTAL KHARCHA = ", total)

# 4. EXIT

    elif choice == "4":
        print("Dhanyawad aapne humara system use kiya")
        break

    else:
        print("INVALID CHOICE> TRY AGAIN")


