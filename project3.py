"""name

min players 2  show 2 list  unique values
max players 10  ,, 10 ,,  ,,


will show 9digit

want to play?
   then will show 20 random numbers
"""

import random

name=input("Enter name?")
print(f"Welcome {name}!!!")


ans='yes'
while ans=='yes' or ans=='Yes' or ans=='y' or ans=='Y':
     n=int(input("Number of players to play?"))

     if n<2 or n>10:
         print("Invalid!!!, Number of players must be >=2 and <=10")
         continue

     names=[]
     for x in range(1,n+1):
         name=input(f"Enter player {x} name?")
         names.append(name)

     players=[]
     for x in range(n):
        player=[]
        for y in range(9):
           player.append(random.choice(range(100)))
        print(player)
        player=list(set(player))
        players.append(player)

     l=[]
     for x in range(1,20):
         l.append(random.choice(range(100)))
     print(l)

     a=[]
     m=list(set(l))
     # print(m)
     b=0
     for x in players:
         for y in x:
             if y in m:
                 b+=1
         a.append(b)

     print("Number of matching Digits:-")
     for x,y in zip(names,a):
         print(x,"-->",y)

     i=a.index(max(a))

     w=input("Who is winner?")
     for j in range(len(names)):
         if i==j:
             if(w==names[j]):
                 print(f"Congratulations {names[j]}!!!, you are the winner!!!")
             else:
                 print(f"Warning!!!, honestly choose the winner name!!! Winner is {names[j]}!!!")

     ans=input("Want to play again?")
     if ans != 'yes' or ans != 'Yes' or ans != 'y' or ans != 'Y':
         print("thankyou for playing!!!")
     a.clear()
     l.clear()
     names.clear()
