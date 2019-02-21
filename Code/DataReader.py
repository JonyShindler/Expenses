import pandas as pd

from money import Money
from Utilities import getValidCategories

# df = pd.read_csv("expenses.csv", encoding="ISO-8859-1")
df = pd.read_csv("testWritingExpenses.csv", encoding="ISO-8859-1")

categories = getValidCategories()
months = df['Month'].unique()

# The next thing is to get monthly breakdowns.
categories_with_month = ['Month'] + categories

def m(amount):
    return Money(amount, 'GBP').format('en_GB')


def sumColumn(column):
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

def getAllExpenses():
    return df

#  TODO maybe we can add averages and totals for the expense retriever.

#TODO find x most expensive entries for a category for example.
#TODO find most expsenses for most expensive motnh for category?

#this will take a dataframe from above for example and sort it out.
def highestXExpenses(dataFrame, n):
    return 0

def sumExpenseseByCategory(dataFrame):
    totals = {}
    for category in categories:
        column = dataFrame.loc[dataFrame['Category'] == category]
        column_sum = column['Amount'].astype(float).sum(0)
        totals.update({category: column_sum})

    return totals



##TODO desired pattern; getAllExpenses().addAverages().addTotals().print
##TODO desired pattern; getExpensesForCategoryForMonth(Jemma, January 19).addTotals().print

totals_for_categories = sumExpenseseByCategory(getAllExpenses())

def getTotalExpenditure():
    total_expenditure = sumColumn(getAllExpenses())
    return total_expenditure


def calculateAccountBalance():
    account_balance = round(3285.93 - 15000 - 20000 - getTotalExpenditure(), 2)
    return account_balance


def calculateNetWealth():
    net_wealth = round(46046.61 + 20000 + 12000 + calculateAccountBalance(), 2)
    return net_wealth


def addAveragesForDataFrame(dataFrame):
    return dataFrame


#Note how a monthlyBreakdown is ready to print, whereas a dataFrame is just a limited view of the original csv.
def addAverages(totals_for_categories, monthly_breakdown):
    totals = list(totals_for_categories.values())
    averageValues = [round(x / len(months), 2) for x in totals]
    average = ['Average'] + averageValues
    monthly_average = pd.DataFrame([average], columns=categories_with_month)
    mb = monthly_breakdown.append(monthly_average)
    return mb


def addTotals(totals_for_categories, monthly_breakdown):
    totals = list(totals_for_categories.values())
    total = ['Total'] + totals
    categoryTotals = pd.DataFrame([total], columns=categories_with_month)
    mb = monthly_breakdown.append(categoryTotals)
    return mb

def calculateMonthlyBreakdownPerCategory(dataFrame, addAverage, addTotal):
    array_For_Month = []
    all_months_df = pd.DataFrame([], columns=categories_with_month)
    for month in months:
        array_For_Month.append(month)
        for category in categories:
            # For each category, go through each month..
            column = dataFrame.loc[(dataFrame['Category'] == category) & (dataFrame['Month'] == month)]
            column_sum = round(column['Amount'].astype(float).sum(0), 2)
            array_For_Month.append(column_sum)
        month_df = pd.DataFrame([array_For_Month], columns=categories_with_month)
        array_For_Month = []
        all_months_df = all_months_df.append(month_df)

    if addAverage:
        all_months_df = addAverages(totals_for_categories, all_months_df)
    if addTotal:
        all_months_df = addTotals(totals_for_categories, all_months_df)
    return all_months_df

def printAccountBalance():
    print("Account balance is " + str(m(calculateAccountBalance())))


def printNetWealth():
    print("Net wealth is " + str(m(calculateNetWealth())))

def printPivotChartWithAveragesAndTotals():
    pivotChart = calculateMonthlyBreakdownPerCategory(getAllExpenses(), True, True)
    print(pivotChart.to_string(index=False))

# also all the EOM quantites (basically the 'Annual Salary' tab, which can be calculated on the fly.
# need to maybe store the remaining balance bit? and new rows can store that.


# try and make a GUI to display this info
# can do the EOM quantities. will need to add columns to the csv which can store things like (extra money)
# or however else we want to represent it on the sheet so it does it for us.


## TODO then make it possible to read certain months /or categories and all the variants like excel does