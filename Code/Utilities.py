def getValidCategories():
    with open('categories.txt', encoding='utf-8-sig') as f:
        return f.read().splitlines()