import pandas as pd
import os

FILE = "expenses.csv"
print("===================================")
print("      Welcome to Expense Tracker")
print("===================================")

if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE, index=False)


def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    amount = float(input("Amount: "))

    df = pd.read_csv(FILE)

    new = pd.DataFrame({
        "Date":[date],
        "Category":[category],
        "Amount":[amount]
    })

    df = pd.concat([df,new],ignore_index=True)

    df.to_csv(FILE,index=False)

    print("Expense Added")


def view_expense(): 
    df = pd.read_csv(FILE)
    print(df)


def total():
    df = pd.read_csv(FILE)
    print("Total =",df["Amount"].sum())


def delete():
    df = pd.read_csv(FILE)

    print(df)

    index = int(input("Enter index to delete: "))

    df = df.drop(index)

    df.to_csv(FILE,index=False)

    print("Deleted")


while True:

    print("\n1.Add")
    print("2.View")
    print("3.Total")
    print("4.Delete")
    print("5.Exit")

    choice=input("Choice:")

    if choice=="1":
        add_expense()

    elif choice=="2":
        view_expense()

    elif choice=="3":
        total()

    elif choice=="4":
        delete()

    elif choice=="5":
        break

    else:
        print("Invalid")