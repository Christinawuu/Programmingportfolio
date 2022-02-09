import random
num = random.randint(0,100)
guesses = 5

print('Welcome to the number guessing game! You have 5 guesses, good luck.')
while (guesses>=1):
  guesses=guesses-1
  test = input('input number: ') 
  if int(test)>num:
   print('you said', test, 'its too high')
  elif int(test)<num:
     print('you said',test,'its too low')
  elif int(test)==num:
   print('you win!')
else:
 print('you lose.. ')



