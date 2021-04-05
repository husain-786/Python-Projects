"""********** Online Shopping ***********"""

cart = []
items = {}

def addToCart(item):
    cart.append(item)

def goToCart():
    if len(cart)==0:
        print("Cart is Empty!!!!!")
    else:
        print(cart)

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

# print("1.UPI\n2.credit/debit")
# mode=int(input("Select Payment Mode?"))
# if mode==1:
#  upi=input("Enter UPI")
# else:
#     cn=input("Enter Card number?")
#     cvv=input("Enter CVV?")
# print(f"{price} debited from your account!!!")
#


