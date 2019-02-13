import pandas as pd

from money import Money
from Utilities import getValidCategories

# df = pd.read_csv("expenses.csv", encoding="ISO-8859-1")
df = pd.read_csv("testWritingExpenses.csv", encoding="ISO-8859-1")

categories = getValidCategories()
months = df['Month'].unique()


def m(amount):
    return Money(amount, 'GBP').format('en_GB')


def sum(column):
    column_sum = column['Amount'].astype(float).sum(0)
    return column_sum


def getExpensesForCategoryForMonth(category, month):
    return df.loc[(df['Category'] == category) & (df['Month'] == month)]


def getExpensesForCategoryForYear(category, year):
    return df.loc[(df['Category'] == category) & (df['Year'] == year)]


def getExpensesForMonth(month):
    return df.loc[(df['Month'] == month)]


def getExpensesForCategory(category):
    return df.loc[(df['Category'] == category)]


def getExpensesForYear(year):
    return df.loc[(df['Year'] == year)]

def getExpenses():
    return df


def sumExpenseseByCategory():
    totals = {}
    for category in categories:
        column = df.loc[df['Category'] == category]
        column_sum = column['Amount'].astype(float).sum(0)
        totals.update({category: column_sum})

    return totals


totals_for_categories = sumExpenseseByCategory()

def getTotalExpenditure(totals_for_categories):
    total_expenditure = sum(totals_for_categories.values())
    return total_expenditure


def displayAccountBalance(total_expenditure):
    account_balance = round(3285.93 - 15000 - 20000 - total_expenditure, 2)
    print("Account balance is " + str(m(account_balance)))
    return account_balance


def displayNetWealth(account_balance):
    net_wealth = round(46046.61 + 20000 + account_balance, 2)
    print("Net wealth is " + str(m(net_wealth)))
    return net_wealth


# The next thing is to get monthly breakdowns.
categories_with_month = ['Month'] + categories


def calculateMonthlyBreakdownPerCategory():
    array_For_Month = []
    all_months_df = pd.DataFrame([], columns=categories_with_month)
    for month in months:
        array_For_Month.append(month)
        for category in categories:
            # For each category, go through each month..
            column = df.loc[(df['Category'] == category) & (df['Month'] == month)]
            column_sum = round(column['Amount'].astype(float).sum(0), 2)
            array_For_Month.append(column_sum)
        month_df = pd.DataFrame([array_For_Month], columns=categories_with_month)
        array_For_Month = []
        all_months_df = all_months_df.append(month_df)
    return all_months_df

monthly_breakdown = calculateMonthlyBreakdownPerCategory()


def addAverages(totals_for_categories, monthly_breakdown):
    totals = list(totals_for_categories.values())
    averageValues = [round(x / len(months), 2) for x in totals]
    average = ['Average'] + averageValues
    monthly_average = pd.DataFrame([average], columns=categories_with_month)
    monthly_breakdown = monthly_breakdown.append(monthly_average)
    return monthly_breakdown


def addTotals(totals, monthly_breakdown):
    totals_for_categories = list(totals.values())
    total = ['Total'] + totals_for_categories
    categoryTotals = pd.DataFrame([total], columns=categories_with_month)
    monthly_breakdown = monthly_breakdown.append(categoryTotals)
    return monthly_breakdown

monthly_breakdown = addAverages(totals_for_categories,monthly_breakdown)
monthly_breakdown = addTotals(totals_for_categories,monthly_breakdown)
print(monthly_breakdown.to_string(index=False))


# also all the EOM quantites (basically the 'Annual Salary' tab, which can be calculated on the fly.
# need to maybe store the remaining balance bit? and new rows can store that.


# try and make a GUI to display this info
# can do the EOM quantities. will need to add columns to the csv which can store things like (extra money)
# or however else we want to represent it on the sheet so it does it for us.


## TODO then make it possible to read certain months /or categories and all the variants like excel does