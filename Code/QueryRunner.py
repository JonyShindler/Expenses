from DataWriter import createExpenseLineForCurrentMonth
from DataWriter import writeExpenseToFile
from DataReader import getExpensesForCategoryForYear
from DataReader import getExpensesForCategoryForMonth
from DataReader import printAccountBalance
from DataReader import printNetWealth
from DataReader import sumColumn
from DataReader import printPivotChartWithAveragesAndTotals
from DataReader import m

#writeExpenseToFile(createExpenseLineForCurrentMonth(100, 'Jemma', 'blobby'))

jan19Sum = sumColumn(getExpensesForCategoryForMonth('Jemma', 'January 19'))
print("Jan 19 Jemma sum: " + str(m(jan19Sum)))

print()

jan19Expenses = getExpensesForCategoryForMonth('Jemma', 'January 19')
print(jan19Expenses.to_string(index=False))

print()

jemmaExpenses2018 = sumColumn(getExpensesForCategoryForYear('Jemma', 2018))
print("2018 Jemma sum: " + str(m(jemmaExpenses2018)))

print()

bigPurchases2018 = getExpensesForCategoryForYear('Big purchases', 2018)
print(bigPurchases2018.to_string(index=False))

print()

print("2018 BP sum: " + str(m(sumColumn(bigPurchases2018))))


print()

printAccountBalance()
printNetWealth()
# printPivotChartWithAveragesAndTotals()