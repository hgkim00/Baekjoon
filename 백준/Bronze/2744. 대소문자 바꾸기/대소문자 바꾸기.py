word = input()

for i in word :
  if (i.isupper()) :
    print(i.lower(), end='')
  if (i.islower()) :
    print(i.upper(), end='')

print() 