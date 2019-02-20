from DataWriter import createExpenseLineForCurrentMonth
from DataWriter import writeExpenseToFile
from DataReader import getExpensesForCategoryForYear
from DataReader import getExpensesForCategoryForMonth
from DataReader import displayNetWealth
from DataReader import sumColumn

writeExpenseToFile(createExpenseLineForCurrentMonth(100, 'Jemma', 'blobby'))

jan19Sum = sumColumn(getExpensesForCategoryForMonth('Jemma', 'January 19'))
print("Jan 19 Jemma sum: " + str(jan19Sum))

jan19Expenses = getExpensesForCategoryForMonth('Jemma', 'January 19')
print(jan19Expenses.to_string(index=False))

jemmaExpenses2018 = sumColumn(getExpensesForCategoryForYear('Jemma', 2018))
print("2018 Jemma sum: " + str(jemmaExpenses2018))

displayNetWealth()
