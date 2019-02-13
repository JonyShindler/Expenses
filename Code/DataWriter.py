from Utilities import getValidCategories

# Month, year, amount, category, description
from datetime import datetime


def createExpenseLine(month, year, amount, category, description):
    if category not in getValidCategories():
        raise ValueError('Category is not valid')

    return month + ' ' + str(year)[2:] + ',' \
            + str(year) + ',' \
            + str(amount) + ',' \
            + category + ',' \
            + description


def createExpenseLineForCurrentMonth(amount, category, description):
    return createExpenseLine(datetime.now().strftime('%B'), datetime.now().year, amount, category, description)


def writeExpenseToFile(expense):
    with open('testWritingExpenses.csv', 'a', encoding='utf-8-sig', newline='') as f:
        f.write(str(expense))
        f.write('\n')
        print('Written expense to csv: ' + expense)
