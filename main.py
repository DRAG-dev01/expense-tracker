from database import init_db, view_expenses, add_expense

init_db()

while True:

    print("""
welcome to expense app
options:
1(add expense)
2(view expense)
3(exit)
""")

    txt = int(input("choose an option: "))

    if txt == 1:
        date = input("type your date: ")
        amount = int(input("type your amount: "))
        description = input("type your description: ")
        category = input("type your category: ")
        add_expense(date, amount, description, category)
    elif txt == 2:
        print(view_expenses())

    elif txt == 3:
        break

    else:
        print("enter a number between 1 to 3 !")


