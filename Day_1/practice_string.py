# name = input("Enter the number: ")
# print(f"Good afternoon dear {name}")
letter ='''Dear <|Name|>,
You are selected !
for role of <|Role|>
from <|Date|>'''
print(letter.replace("<|Name|>","Shaurya").replace("<|Date|>","20:novmber:2025").replace("<|Role|>","Data analytics"))