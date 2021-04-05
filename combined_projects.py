def onlineShopping():
    cart = []
    items = {}

    def addToCart(item):
        cart.append(item)

    def goToCart():
        if len(cart)==0:
            print("\n\nCart is Empty!!!!!")
        else:
            print(f"\n\n***** Cart *****\n{cart}")

    def payment(price,cashback):
        print(f"\nTotal:{price}\nOfferAmount:-{price*(cashback/100)}\nTO Pay:{price-(price*(cashback/100))}")
        price=price-(price*(cashback/100))
        print("1.UPI\n2.credit/debit")
        mode = int(input("Select Payment Mode?"))
        if mode == 1:
            upi = input("Enter UPI? ")
        elif mode==2:
            cn = input("Enter Card number?")
            cvv = input("Enter CVV?")
        else:
            print("Choose correct payment method?")
        print("***** Payment Successfull ******")
        print(f"{price} debited from your account!!!")



    print("Login First!")
    name=input("Name:")
    id=input("ID:")
    password=input("Password:")
    print(f"Welcome {name}!")

    print("\n1.Elecronics and Mobile Accessories,\n2.Men's T-shirt,\n3.Kitchen Products,\n4.Books.")
    choice=int(input("Select for Purchase?"))

    price=0
    if choice==1:
        print("\n1.Laptops And Computers,\n2.Smart Phones,\n3.Refrigerators,\n4.Others.")
        i=int(input("Select your interest?"))
        if i==1:
            cashback=10
            print("\n1.Lenovo,\n2.Redmi,\n3.Asus,\n4.Sony.")
            j=int(input("Select Brand?"))
            print("\n1.i5,7th gen,\n2.i5,9th gen,\n3.i7,7th gen,\n4.i7,9th gen.")
            k=int (input("Select Processor?"))
            if j==1 or j==2 or j==3 or j==4 and k==1:
                price=57000
                print("\nPrice=",price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l=int(input("Select?"))
                if l==1:
                    payment(price,cashback)
                else:
                    if j==1:
                        item = {}
                        item["Brand"]="Lenovo"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
                    elif j==2:
                        item = {}
                        item["Brand"]="Redmi"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
                    elif j==3:
                        item = {}
                        item["Brand"]="Asus"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
                    elif j==4:
                        item = {}
                        item["Brand"]="Sony"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
            elif j==1 or j==2 or j==3 or j==4 and k==2:
                price=62000
                print("Price=",price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l=int(input("Select"))
                if l==1:
                    payment(price,cashback)
                else:
                    if j==1:
                        item = {}
                        item["Brand"]="Lenovo"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
                    elif j==2:
                        item = {}
                        item["Brand"]="Redmi"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
                    elif j==3:
                        item = {}
                        item["Brand"]="Asus"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
                    elif j==4:
                        item = {}
                        item["Brand"]="Sony"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
            elif j==1 or j==2 or j==3 or j==4 and k==3:
                price=82000
                print("Price=",price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l=int(input("Select"))
                if l==1:
                    payment(price,cashback)
                else:
                    if j==1:
                        item = {}
                        item["Brand"]="Lenovo"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
                    elif j==2:
                        item = {}
                        item["Brand"]="Redmi"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
                    elif j==3:
                        item = {}
                        item["Brand"]="Asus"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
                    elif j==4:
                        item = {}
                        item["Brand"]="Sony"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
            elif j==1 or j==2 or j==3 or j==4 and k==4:
                price=97000
                print("Price=",price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l=int(input("Select"))
                if l==1:
                    payment(price,cashback)
                else:
                    if j==1:
                        item = {}
                        item["Brand"]="Lenovo"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
                    elif j==2:
                        item = {}
                        item["Brand"]="Redmi"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
                    elif j==3:
                        item = {}
                        item["Brand"]="Asus"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)
                    elif j==4:
                        item = {}
                        item["Brand"]="Sony"
                        item["Processor"]="i5,7th gen"
                        item["Price"]=price
                        addToCart(item)


        elif i==2:
            cashback=10
            print("\n1.Realme,\n2.Nokia,\n3.Redmi,\n4.Oppo.")
            j=int(input("Select Brand?"))
            print("1.4GB,64GB,\n2.6GB,64GB,\n3.6GB,128GB,\n4.8GB,128GB,\n5.8GB,256GB.")
            k=int (input("Select Storage?"))
            if k==1:
                    price = 11999
                    print("Price=", price)
                    print(f"Shop in 15 min and get {cashback}% instant cashback.")
                    print("1.Buy Now\n2.Add to Cart")
                    l = int(input("Select"))
                    if l == 1:
                        payment(price, cashback)
                    else:
                        if j == 1:
                            item = {}
                            item["Brand"] = "Realme"
                            item["Storage"] = "4GB,64GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 2:
                            item = {}
                            item["Brand"] = "Nokia"
                            item["Processor"] = "4GB,64GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 3:
                            item = {}
                            item["Brand"] = "Redmi"
                            item["Processor"] = "4GB,64GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 4:
                            item = {}
                            item["Brand"] = "Oppo"
                            item["Processor"] = "4GB,64GB"
                            item["Price"] = price
                            addToCart(item)
            elif k==2:
                    price = 15999
                    print("Price=", price)
                    print(f"Shop in 15 min and get {cashback}% instant cashback.")
                    print("1.Buy Now\n2.Add to Cart")
                    l = int(input("Select"))
                    if l == 1:
                        payment(price, cashback)
                    else:
                        if j == 1:
                            item = {}
                            item["Brand"] = "Realme"
                            item["Storage"] = "6GB,64GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 2:
                            item = {}
                            item["Brand"] = "Nokia"
                            item["Processor"] = "6GB,64GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 3:
                            item = {}
                            item["Brand"] = "Redmi"
                            item["Processor"] = "6GB,64GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 4:
                            item = {}
                            item["Brand"] = "Oppo"
                            item["Processor"] = "6GB,64GB"
                            item["Price"] = price
                            addToCart(item)
            elif k==3:
                    price = 18999
                    print("Price=", price)
                    print(f"Shop in 15 min and get {cashback}% instant cashback.")
                    print("1.Buy Now\n2.Add to Cart")
                    l = int(input("Select"))
                    if l == 1:
                        payment(price, cashback)
                    else:
                        if j == 1:
                            item = {}
                            item["Brand"] = "Realme"
                            item["Storage"] = "6GB,128GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 2:
                            item = {}
                            item["Brand"] = "Nokia"
                            item["Processor"] = "6GB,128GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 3:
                            item = {}
                            item["Brand"] = "Redmi"
                            item["Processor"] = "6GB,128GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 4:
                            item = {}
                            item["Brand"] = "Oppo"
                            item["Processor"] = "6GB,128GB"
                            item["Price"] = price
                            addToCart(item)

            elif k==4:
                    price = 21999
                    print("Price=", price)
                    print(f"Shop in 15 min and get {cashback}% instant cashback.")
                    print("1.Buy Now\n2.Add to Cart")
                    l = int(input("Select"))
                    if l == 1:
                        payment(price, cashback)
                    else:
                        if j == 1:
                            item = {}
                            item["Brand"] = "Realme"
                            item["Storage"] = "8GB,128GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 2:
                            item = {}
                            item["Brand"] = "Nokia"
                            item["Processor"] = "8GB,128GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 3:
                            item = {}
                            item["Brand"] = "Redmi"
                            item["Processor"] = "8GB,128GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 4:
                            item = {}
                            item["Brand"] = "Oppo"
                            item["Processor"] = "8GB,128GB"
                            item["Price"] = price
                            addToCart(item)
            elif k==5:
                    price = 24999
                    print("Price=", price)
                    print(f"Shop in 15 min and get {cashback}% instant cashback.")
                    print("1.Buy Now\n2.Add to Cart")
                    l = int(input("Select"))
                    if l == 1:
                        payment(price, cashback)
                    else:
                        if j == 1:
                            item = {}
                            item["Brand"] = "Realme"
                            item["Storage"] = "8GB,256GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 2:
                            item = {}
                            item["Brand"] = "Nokia"
                            item["Processor"] = "8GB,256GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 3:
                            item = {}
                            item["Brand"] = "Redmi"
                            item["Processor"] = "8GB,256GB"
                            item["Price"] = price
                            addToCart(item)
                        elif j == 4:
                            item = {}
                            item["Brand"] = "Oppo"
                            item["Processor"] = "8GB,256GB"
                            item["Price"] = price
                            addToCart(item)

        elif i == 3:
            cashback=15
            print("\n1.Samsung,\n2.LG,\n3.Whirpool.")
            j = int(input("Select Brand?"))
            print("1.Single Door,\n2.Double Door.")
            k = int(input("Select choice?"))
            if j == 1 and k==1:
                price = 12999
                print("Price=", price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l = int(input("Select"))
                if l == 1:
                    payment(price, cashback)
                else:
                    item = {}
                    item["Brand"] = "Samsung"
                    item["Feature"] = "Single door"
                    item["Price"] = price
                    addToCart(item)
            if j == 1 and k==2:
                price = 16999
                print("Price=", price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l = int(input("Select"))
                if l == 1:
                    payment(price, cashback)
                else:
                    item = {}
                    item["Brand"] = "Samsung"
                    item["Feature"] = "Double door"
                    item["Price"] = price
                    addToCart(item)
            if j == 2 and k==1:
                price = 11999
                print("Price=", price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l = int(input("Select"))
                if l == 1:
                    payment(price, cashback)
                else:
                    item = {}
                    item["Brand"] = "LG"
                    item["Feature"] = "Single door"
                    item["Price"] = price
                    addToCart(item)
            if j == 2 and k==2:
                price = 14999
                print("Price=", price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l = int(input("Select"))
                if l == 1:
                    payment(price, cashback)
                else:
                    item = {}
                    item["Brand"] = "LG"
                    item["Feature"] = "Single door"
                    item["Price"] = price
                    addToCart(item)
            if j == 3 and k==1:
                price = 13999
                print("Price=", price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l = int(input("Select"))
                if l == 1:
                    payment(price, cashback)
                else:
                    item = {}
                    item["Brand"] = "Whirlpool"
                    item["Feature"] = "Single door"
                    item["Price"] = price
                    addToCart(item)
            if j == 3 and k==2:
                price = 16999
                print("Price=", price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l = int(input("Select"))
                if l == 1:
                    payment(price, cashback)
                else:
                    item = {}
                    item["Brand"] = "Whirlpool"
                    item["Feature"] = "Double door"
                    item["Price"] = price
                    addToCart(item)


    if choice==2:
        cashback=0
        print("1.S\n2.L\n3.XL\n4.XXL")
        j=int(input("Select your size?"))
        if j==1:
            price=320
            print("Price=", price)
            print(f"Shop in 15 min and get {cashback}% instant cashback.")
            print("1.Buy Now\n2.Add to Cart")
            l = int(input("Select"))
            if l == 1:
                payment(price, cashback)
            else:
                item = {}
                item["Size"] = "S"
                item["Price"] = price
                addToCart(item)
        if j==2:
            price=450
            print("Price=", price)
            print(f"Shop in 15 min and get {cashback}% instant cashback.")
            print("1.Buy Now\n2.Add to Cart")
            l = int(input("Select"))
            if l == 1:
                payment(price, cashback)
            else:
                item = {}
                item["Size"] = "L"
                item["Price"] = price
                addToCart(item)
        if j==3:
            price=570
            print("Price=", price)
            print(f"Shop in 15 min and get {cashback}% instant cashback.")
            print("1.Buy Now\n2.Add to Cart")
            l = int(input("Select"))
            if l == 1:
                payment(price, cashback)
            else:
                item = {}
                item["Size"] = "XL"
                item["Price"] = price
                addToCart(item)
        if j==4:
            price=799
            print("Price=", price)
            print(f"Shop in 15 min and get {cashback}% instant cashback.")
            print("1.Buy Now\n2.Add to Cart")
            l = int(input("Select"))
            if l == 1:
                payment(price, cashback)
            else:
                item = {}
                item["Size"] = "S"
                item["Price"] = price
                addToCart(item)


    if choice==3:
        cashback=2
        print("1.Pressure Cooker\n2.Design Plate(pack of 6)\n3.Tubs")
        j=int(input("Select choice?"))
        if j==1:
            print("1.2 ltr\n2.5 ltr\n3.10ltr")
            k=int(input("Select Quantity?"))
            if k==1:
                price=2300
                print("Price:",price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l = int(input("Select"))
                if l == 1:
                    payment(price, cashback)
                else:
                    item = {}
                    item["Item"] = "Pressure Cooker"
                    item["Capacity"]="2 ltr"
                    item["Price"] = price
                    addToCart(item)
            elif k==2:
                price=3500
                print("Price:",price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l = int(input("Select"))
                if l == 1:
                    payment(price, cashback)
                else:
                    item = {}
                    item["Item"] = "Pressure Cooker"
                    item["Capacity"]="5 ltr"
                    item["Price"] = price
                    addToCart(item)
            elif k==3:
                price=6799
                print("Price:",price)
                print(f"Shop in 15 min and get {cashback}% instant cashback.")
                print("1.Buy Now\n2.Add to Cart")
                l = int(input("Select"))
                if l == 1:
                    payment(price, cashback)
                else:
                    item = {}
                    item["Item"] = "Pressure Cooker"
                    item["Capacity"]="10 ltr"
                    item["Price"] = price
                    addToCart(item)
        if j==2:
            cashback=0
            price=1200
            print("Price:",price)
            print("1.Buy Now\n2.Add to Cart")
            l = int(input("Select"))
            if l == 1:
                payment(price, cashback)
            else:
                item = {}
                item["Item"] = "Design Plates"
                item["Quantity"] = "6 pieces"
                item["Price"] = price
                addToCart(item)
        if j==3:
            cashback=0
            print("1.20 ltr\n2.25 ltr\n3.40ltr")
            k=int(input("Select Quantity?"))
            if k==1:
                price=1299
                print("Price:",price)
                print("1.Buy Now\n2.Add to Cart")
                l = int(input("Select"))
                if l == 1:
                    payment(price, cashback)
                else:
                    item = {}
                    item["Item"] = "Tub"
                    item["Quantity"] = "20 ltr"
                    item["Price"] = price
                    addToCart(item)
            if k==2:
                price=1799
                print("Price:",price)
                print("1.Buy Now\n2.Add to Cart")
                l = int(input("Select?"))
                if l == 1:
                    payment(price, cashback)
                else:
                    item = {}
                    item["Item"] = "Tub"
                    item["Quantity"] = "25 ltr"
                    item["Price"] = price
                    addToCart(item)
            if k==3:
                price=2399
                print("Price:",price)
                print("1.Buy Now\n2.Add to Cart")
                l = int(input("Select"))
                if l == 1:
                    payment(price, cashback)
                else:
                    item = {}
                    item["Item"] = "Tub"
                    item["Quantity"] = "40 ltr"
                    item["Price"] = price
                    addToCart(item)
    if choice==4:
        cashback=0
        print("1.Technical Books\n2.Sci-fi Books\n3.Novels")
        j=int(input("Select book?"))
        if j==1:
            price=3999
            print("Price:",price)
            print("1.Buy Now\n2.Add to Cart")
            l = int(input("Select"))
            if l == 1:
                payment(price, cashback)
            else:
                item = {}
                item["Item"] = "Technical Books"
                item["Price"] = price
                addToCart(item)
        if j==2:
            price=1999
            print("Price:",price)
            print("1.Buy Now\n2.Add to Cart")
            l = int(input("Select"))
            if l == 1:
                payment(price, cashback)
            else:
                item = {}
                item["Item"] = "Sci-fi Books"
                item["Price"] = price
                addToCart(item)
        if j==3:
            price=999
            print("Price:",price)
            print("1.Buy Now\n2.Add to Cart")
            l = int(input("Select"))
            if l == 1:
                payment(price, cashback)
            else:
                item = {}
                item["Item"] = "Novel Book"
                item["Price"] = price
                addToCart(item)

    print("Thanks for shopping with us!!!")
    goToCart()





import random
def tambola():
    def playersNames():
        global n
        n = int(input("Number of players to play?"))

        if n < 2 or n > 10:
            print("Invalid!!!, Number of players must be >=2 and <=10")
            playersNames()
        else:
            names = []
            for x in range(1, n + 1):
                name = input(f"Enter player {x} name?")
                names.append(name)
            return names

    def playersList():
            players = []
            for x in range(n):
                player = []
                for y in range(9):
                    player.append(random.choice(range(100)))
                print(player)
                player = list(set(player))
                players.append(player)

            return players

    def listTwenty():
        l = []
        for x in range(0, 21):
            l.append(random.choice(range(100)))
        print(l)
        return l

    def matching(names,players,l):
        a = []
        m = list(set(l))
        # print(m)
        b = 0
        for x in players:
            for y in x:
                if y in m:
                    b += 1
            a.append(b)

        print("Number of matching Digits:-")
        for x, y in zip(names, a):
            print(x, "-->", y)

        i = a.index(max(a))

        w=input("Who is Winner?")

        for j in range(len(names)):
            if i == j:
                if names[j]==w:
                    print(f"{names[j]} is the winner!!!")
                    print("Congratulations!!!")
                else:
                    print("Warning!!!, honestly write the winner name")


    name = input("Enter name?")
    print(f"Welcome {name}!!!")

    ans='yes'
    while ans=='yes' or ans=='Yes' or ans=='y' or ans=='Y':
        names=playersNames()
        # if names==0:
        #     names=playersNames()
        players=playersList()
        lt=listTwenty()
        matching(names,players,lt)

        a=input("Want to  play again?")
        if a!='yes' or a!='Yes' or a!='y' or a!='Y':
            print("thankyou for playing!!!")
            ans=a
        else:
            ans=a




import string
import random


def onlineBook():
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




print("Welcome to the 'ALL IN ONE' shopping center!!!\n")
ans='yes'
while ans=='yes' or ans=='Yes' or ans=='y' or ans=='Y':
    print("1.Online Shopping\n2.Tambola Game\n3.Online Books")
    ch=int(input("Select your choice?"))
    if ch==1:
        onlineShopping()
    elif ch==2:
        tambola()
    elif ch==3:
        onlineBook()
    else:
        print("Warning, Select a valid choice !!!")
    a=input("\n\nWant to Enjoy the 'ALL IN ONE' Service Again?")
    if a=='yes' or a=='Yes' or a=='y' or a=='Y':
        ans=a
    else:
        ans=a

