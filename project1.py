"""********** online library/story book **********"""

import string
import random

def content(np):
    l=[]
    for x in range(np):
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.ascii_lowercase, k=200))
        l.insert(x,res)

    return l


def storyBooks(name):
    global bName
    global book
    global n
    n = 1

    print("\n1.The story of my life.\n2.Invisible man\n3.Harry Potter")

    ch=int(input("Select the book you want to read?"))
    if ch==1:
        np=320
        book=content(np)
        bName="The story of my life."
        print(f"The book 'The story of my life' has {np} pages!!!")
        ans=input("Want to start?")
        if ans=='yes' or ans=='Yes' or ans=='y' or ans=='Y':
            print("Let's start.\n")
            print(f"page no:{n}")
            print(book[n])
            a='yes'
            while a=='yes' or a=='Yes' or a=='y' or a=='Y':
                print("1.Next Page\n2.Exit")
                b=int(input('Select?'))
                if b==1:
                    a='yes'
                    n+=1
                    print(f"page no:{n}")
                    print(book[n])
                else:
                    print(f"You was reading the page number {n}!!!")
                    print("Thanks for reading, visit again!!!!")
                    a='no'
        else:
            c=input("Want to read another book?")
            if c=='yes' or c=='Yes' or c=='y' or c=='Y':
                storyBooks()
            else:
                print("Thankyou, visit again!!!")

    elif ch==2:
        np=420
        book=content(np)
        bName="Invisible man"
        print(f"The book 'Invisible man' has {np} pages!!!")
        ans=input("Want to start?")
        if ans=='yes' or ans=='Yes' or ans=='y' or ans=='Y':
            print("Let's start.\n")
            print(f"page no:{n}")
            print(book[n])
            a='yes'
            while a=='yes' or a=='Yes' or a=='y' or a=='Y':
                print("1.Next Page\n2.Exit")
                b=int(input('Select?'))
                if b==1:
                    a='yes'
                    n+=1
                    print(f"page no:{n}")
                    print(book[n])
                else:
                    print(f"You was reading the page number {n}!!!")
                    print("Thanks for reading, visit again!!!!")
                    a='no'
        else:
            c=input("Want to read another book?")
            if c=='yes' or c=='Yes' or c=='y' or c=='Y':
                storyBooks()
            else:
                print("Thankyou, visit again!!!")

    elif ch==3:
        np=820
        book=content(np)
        bName='Harry Potter'
        print(f"The book 'Harry Potter' has {np} pages!!!")
        ans=input("Want to start?")

        book=content(np)

        if ans=='yes' or ans=='Yes' or ans=='y' or ans=='Y':
            print("Let's start.\n")
            print(f"page no:{n}")
            print(book[n])
            a='yes'
            while a=='yes' or a=='Yes' or a=='y' or a=='Y':
                print("1.Next Page\n2.Exit")
                b=int(input('Select?'))
                if b==1:
                    a='yes'
                    n+=1
                    print(f"page no:{n}")
                    print(book[n])
                else:
                    print(f"You was reading the page number {n}!!!")
                    print("Thanks for reading, visit again!!!!")
                    a='no'
        else:
            c=input("Want to read another book?")
            if c=='yes' or c=='Yes' or c=='y' or c=='Y':
                storyBooks()
            else:
                print("Thankyou, visit again!!!")


def nextDay(name):
    global bName
    global book
    global n
    print(f"\nWelcome again {name} to the story Books!!!")
    print(f"You was reading the book '{bName}' at page number {n}!!!")
    a=input("Do you want to continue at which you left?")
    if a=='yes' or a=='Yes' or a=='y' or a=='Y':
        p=input("Do you remember page number you was reading yesterday?")
        if p == 'yes' or p == 'Yes' or p == 'y' or p == 'Y':
            chance=0
            while chance<3:
                d=int(input("Enter Page Number?"))
                if d==n:
                    # chance=4
                    n+=1
                    print(f"Awesome,continue reading you are at page number {n}")
                    print(f"page no:{n}")
                    print(book[n])
                    a = 'yes'
                    while a == 'yes' or a == 'Yes' or a == 'y' or a == 'Y':
                        print("1.Next Page\n2.Exit")
                        b = int(input('Select?'))
                        if b == 1:
                            a = 'yes'
                            n += 1
                            print(f"page no:{n}")
                            print(book[n])
                            continue
                        else:
                            print(f"You was reading the page number {n}!!!")
                            print("Thanks for reading, visit again!!!!")
                            a = 'no'
                            chance=4
                            return
                else:
                    print("Sorry, your given page number didnot match with the yesterday history!!!")
                    chance+=1

            else:
                e=input("Do you remember any specific word at the page you were reading?")
                if e == 'yes' or e == 'Yes' or e == 'y' or e == 'Y':
                    f=input("Enter the word you remember?")
                    satisfied=False
                    while satisfied==False:
                        n1=n
                        print(f"page no:{n1}")
                        print(book[n1])
                        n1+=1
                        stfd=input("This is the result according to your word, are you satisfied?")

                        # print(f"page no:{n}")
                        # print(book[n])

                        if stfd == 'yes' or stfd == 'Yes' or stfd == 'y' or stfd == 'Y':
                            print("Enjoy Reading")
                            n+=1
                            print(f"page no:{n}")
                            print(book[n])
                            a = 'yes'
                            while a == 'yes' or a == 'Yes' or a == 'y' or a == 'Y':
                                print("1.Next Page\n2.Exit")
                                b = int(input('Select?'))
                                if b == 1:
                                    a = 'yes'
                                    n += 1
                                    print(f"page no:{n}")
                                    print(book[n])
                                else:
                                    print(f"You was reading the page number {n}!!!")
                                    print("Thanks for reading, visit again!!!!")
                                    a = 'no'

                            satisfied=True
                        else:
                            satisfied=False
                else:
                    print("Sorry, Send request to the team!!!")

        else:
            e = input("Do you remember any specific word at the page you were reading?")
            if e == 'yes' or e == 'Yes' or e == 'y' or e == 'Y':
                f = input("Enter the word you remember?")
                satisfied = False
                while satisfied == False:
                    stfd = input("This is the result according to your word, are you satisfied?")
                    if stfd == 'yes' or stfd == 'Yes' or stfd == 'y' or stfd == 'Y':
                        print("Enjoy Reading")
                        n += 1
                        print(f"page no:{n}")
                        print(book[n])
                        a = 'yes'
                        while a == 'yes' or a == 'Yes' or a == 'y' or a == 'Y':
                            print("1.Next Page\n2.Exit")
                            b = int(input('Select?'))
                            if b == 1:
                                a = 'yes'
                                n += 1
                                print(f"page no:{n}")
                                print(book[n])
                            else:
                                print(f"You was reading the page number {n}!!!")
                                print("Thanks for reading, visit again!!!!")
                                a = 'no'
                        satisfied = True
                    else:
                        satisfied = False
            else:
                print("Sorry, Send request to the team!!!")

    else:
        print("Thankyou, visit again!!!")



name=input("Enter your name?")
print(f"Welcome '{name}' to the story books!!!")
storyBooks(name)
nextDay(name)
