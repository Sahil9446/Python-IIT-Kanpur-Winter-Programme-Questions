#Question description
"""
Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}
"""

#Solution
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)


