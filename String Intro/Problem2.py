# Write a python program to fill in a letter template given below with name and date.

letter = '''Dear <|Name|>,
  You are selected! 
  <|Date|>'''
print(letter.replace("<|Name|>", "Sujita Singh").replace("<|Date|>", "15th June 2026"))