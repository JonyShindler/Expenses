from Utilities import getValidCategories

# Month, year, amount, category, description
from datetime import datetime


def createExpenseLine(month, year, amount, category, description):
    if category not in categories:
        raise ValueError('Category is not valid')

    return month + ' ' + str(year)[2:] + ',' \
            + str(year) + ',' \
            + str(amount) + ',' \
            + category + ',' \
            + description


def createExpenseLineForCurrentMonth(amount, category, description):
    return createExpenseLine(currentMonth, currentYear, amount, category, description)


def writeExpenseToFile(expense):
    with open('testWritingExpenses.csv', 'a', encoding='utf-8-sig', newline='') as f:
        f.write(str(expense))
        f.write('\n')
        print('Written expense to csv: ' + expense)


currentMonth = datetime.now().strftime('%B')
currentYear = datetime.now().year

categories = getValidCategories()

line = createExpenseLine(currentMonth, currentYear, 100, 'Jemma', 'blobby')
writeExpenseToFile(line)

# TODO maybe store remaining balance as it makes debugging easier.

