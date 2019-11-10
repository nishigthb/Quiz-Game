#Quiz Game
import time
score=0
total_q=10
print('Welcome!')
print( "\n ************************* GAME HELP *************************\nThere will be a total of 10 questions.\nYou will be given 4 options and you have to press a,b,c or d for the anwser\nEach question will carry 1 point");  print("*******************************************************")
name=input("Enter your name:")
print ("OK  " +  name +",lets start with the game.")
time.sleep(2)
ans=input('1.What is capital of Queensland?\n(a.)Townsville\n(b.)Brisbane\n(c.)Noosa\n(d.)None of the above\n')
if ans.lower()=='b':
  score=score+ 1
  print('Correct answer')
else: print("InCorrect!The answer is Brisbane ")
ans=input('\n2.Who was the first president of USA?\n(a.)Thomas Jefferson\n(b.)William Henry Harrison\n(c.)John Adams\n(d.)G.Washington\n')
if ans.lower()=='d':
  score=score+ 1
  print('Correct answer')
else:
   print('InCorrect!The is anwer is G.Washington')
ans=input('\n3.Which day is observed as the World Standards Day?\n(a.)June 26\n(b.)Oct 14\n(c.)Nov 15\n(d.)Dec 2\n')
if ans.lower()=='b':
    score=score+ 1
    print('Correct answer')
else:
   print('InCorrect!The answer is Oct 14')

ans=input('\n4.Which express train  run by the Indian Railways turned 50 in 2019?\n(a.)Shatabdi Express \n(b.)Rajdhani Express\n(c.)Duronto express \n(d.)Sampoorn Kanti Express\n') 
if ans.lower()=='b':
    score=score+ 1
    print('Correct answer')
else:
    print('InCorrect!\nThe answer is Rajdhani Express')
ans=input('\n5.Which book has been printed in the maximum number of languages?\n(a.)The Bible\n(b.)The Super book\n(c.)Hiraka Sutra\n(d.)None of these\n')
if ans.lower()=='a':
    score=score+ 1
    print('Correct answer')
else:
    print('InCorrect!The answer is The Bible')

ans=input('\n6.Whichof these comic  book characters wears a pagdi  ?\n(a.) Billu\n(b.)Chacha Choudhary \n(c.)Sabu \n(d.)Raka\n')
if ans.lower()=='b':
    score=score+ 1
    print('Correct answer')
else:
    print('InCorrect!The answer is Chacha Choudhary ')

ans=input('\n7.Which of these cricket umpires is also a qualifes FIFA referee?\n(a.)Ian Robin\n(b.)Steve Bucknor\n(c).Steve Dunne\n(d.)Darell Hair\n')
if ans.lower()=='b':
    score=score+ 1
    print('Correct answer')
else:
    print('InCorrect!The answer is Steve Bucknor')

ans=input('\n8.Which of the game can also be described as hockey on horseback?\n(a.)Ice hockey\n(b.)Charoit Racing\n(c.)Water Polo \n(d.)Polo\n')
if ans.lower()=='d':
    score=score+ 1
    print('Correct answer')
else:
    print('InCorrect!The answer is Polo')

ans=input('\n9.In India which case was heard by the largest ever Constitution bench of 13 Supreme Court judges  ?\n(a.Golaknath Case\n(b.)Ashoka Kumar  Thakur Case\n(c.)Sah Bano Case\n(d.)Kesavananada Bharti Case\n')
if ans.lower()=='d':
    score=score+ 1
    print('Correct answer')
else:
    print('InCorrect!The answer is Kesavananada Bharti Case ')
ans=input('\n10.With refrencre to time what does GMT stands for?\n(a.)GreenLand Mean Time \n(b.)General Middle Time\n(c.Geographic Middle Time\n(d.)Greenwich Mean Time\n')
if ans.lower()=='d':
    score=score+ 1
    print('Correct answer')
else:
    print('InCorrect!The answer is Greenwich Mean Time')

print ("\nYour game is  finished, " + name +". \nYou got",score, "out of 10  correct.\n")
if(score>=8) : print("+name+" ,"you played well")
else :
  print("Your score was satisfying")
print ("\nTHANK YOU !" )

