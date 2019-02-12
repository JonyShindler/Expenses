from DataWriter import createExpenseLine
from DataWriter import writeExpenseToFile

writeExpenseToFile(createExpenseLine(100, 'Jemma', 'blobby'))

df = pd.read_csv("testWritingExpenses.csv", encoding="ISO-8859-1")
