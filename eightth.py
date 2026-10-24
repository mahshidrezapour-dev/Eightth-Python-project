# پروژه هشتم
# سیستم مدیریت کتابخانه
# رفتارها:
# add → کتاب جدید اضافه کن
# show all → همه کتاب‌ها رو نمایش بده
# search → با عنوان کتاب پیداش کن
# delete → کتاب رو حذف کن
# borrow → کتاب رو امانت بگیر؛ اگر قبلاً امانت داده شده بود، اجازه نده
# return → کتاب امانت‌گرفته‌شده رو برگردون
# exit → خروج
from datetime import datetime , timedelta


def books(title=None):
    if title is None:
        title = input("title : ")
    author = input("author : ")
    year = int(input("year of publish : "))
    available = True
    borrow_count=0
    list_of_books = {
        "title": title,
        "author": author,
        "year": year,
        "available": available,
        "borrow_count":borrow_count
    }
    return list_of_books


def borrow():
    name = input("enter your name : ")
    deadline = int(input("how many days do you want to keep this book ?  : "))
    age = int(input("enter your age : "))
    sign = input("enter your sign to ensure you will return the book on the exact time >>>> ")
    address = input("enter your address")
    phone = int(input("enter your phone number"))
    title=input("enter the book title >>> ")
    date_of_borrow = datetime.now()
    borrower = {
        "name": name,
        "deadline": deadline,
        "age": age,
        "sign": sign,
        "address": address,
        "phone": phone,
        "title":title,
        "date_of_borrow": date_of_borrow
    }
    return borrower


def return_book():
    name = input("enter your name : ")
    date_of_return = datetime.now()
    sign = input("enter your sign >>> ")
    bookname = input("enter book name")
    returner = {
        "name": name,
        "date_of_return": date_of_return,
        "sign": sign,
        "bookname": bookname
    }
    return returner
def show_history():
    print(borrow_history)
    for record in borrow_history:
        if "date_of_return" not in record:
            print("THE BOOK" , record["title"] , "HAS NOT BEEN BACK")
        else:
            print(record["title"], "has been returned")


all_books = {}
borrow_history=[]


i = int(input("enter initial quantity : "))
for count in range(i):
    library = books()
    all_books[library["title"]] = library
while True:
    behavior = input("what you ask ? >>> ")
    if behavior.lower() == "add":
        answer = input("what book do you want to add ?  enter here >>> ")
        if answer in all_books:
            print("already exists")
        else:
            print("enter informations >>>> ")
            library = books(answer)
            all_books[library["title"]] = library
    elif behavior.lower() == "show all":
        print(all_books)

    elif behavior.lower() == "search":
        question = input("based on what are you searching ? title / author / year ? ")
        found = False
        if question.lower() == "title":
            q = input("what title are you looking for ?  >>>>")
            for book in all_books:
                if all_books[book]["title"] == q:
                    print(all_books[book])
                    found = True
            if not found:
                print("THIS TITLE NOT FOUND")

        elif question.lower() == "author":
            e = input("what author areyou looking for ? >>> ")
            for book in all_books:
                if all_books[book]["author"] == e:
                    print(all_books[book])
                    found = True
            if not found:
                print("AUTHOR NOT FOUND")

        elif question.lower() == "year":
            r = int(input("what yea are you looking for? >>> "))
            for book in all_books:
                if all_books[book]["year"] == r:
                    print(all_books[book])
                    found = True
            if not found:
                print("YEAR NOT FOUND")
        else:
            print("NOT FOUND")
    elif behavior.lower() == "delete":
        v = input("what book do you want to delete ? >>> ")
        found = False
        for book in list(all_books):
            if all_books[book]["title"] == v:
                del all_books[book]
                found = True
                break
        if not found:
            print("NOT FOUND")
    elif behavior.lower() == "borrow":
        borrowing = borrow()
        eligible = False
        if borrowing["age"] >= 18 and borrowing["deadline"] <= 7 and borrowing["sign"] and borrowing["address"] and borrowing["phone"] and borrowing["name"]:
            eligible = True
            y = input("what book do you want to borrow ? >>>")
            found = False
            for book in all_books:
                
                if all_books[book]["title"] == y:
                    found = True
                    if all_books[book]["available"] == True:
                        
                        
                        print("this book is available ... ")
                        o = input("are you sure you want to borrow this book ? ")
                        if o.lower() in ["yes", "y", "yeah"]:
                            all_books[book]["borrow_count"]+=1
                            print("you should bring this book in 7 days ,otherwise you have to pay for keeping the book more than the deadline ")
                            all_books[book]["borrower"]=borrowing
                            all_books[book]["available"] = False
                            print("one book of",all_books[book]["title"], " has been lended ")
                            borrow_history.append(borrowing)
                            
                        else:
                            pass
                    else:
                        print("NOT EVAILABLE")
            if not found:
                print("NOT FOUND")
        else:
            print("NOT ELIGIBLE")
    elif behavior.lower() == "return":
        returning = return_book()
        eligible = False
        found=False 
        for book in all_books:
            if all_books[book]["title"]==returning["bookname"]:
                found=True
                if all_books[book]["available"]==True:
                    print("this book has not been borrowed")
                else:
                    borrowing=all_books[book]["borrower"]
                    deadline_date=borrowing["date_of_borrow"]+timedelta(days=borrowing["deadline"])
                    if returning["name"] == borrowing["name"] and returning["date_of_return"] <= deadline_date  and returning["sign"] == borrowing["sign"] and returning["bookname"] == borrowing["title"]:
                        eligible = True
                        all_books[book]["available"] = True
                        print("Thank you for bringing the book back")
                        borrowing["date_of_return"]=returning["date_of_return"]
                    else:
                        eligible = False
                        print("not eligible, you cannot borrow any books from now on ")
                    
        if not found:
            print("this book has not been borrowed")
    elif behavior.lower()=="history":
        show_history()
    elif behavior.lower()=="borrow count":
        k=input("for what book's history are you looking for ? >>> ")
        found=False
        for book in all_books:
            
            if all_books[book]["title"]==k:
                found=True
                print(all_books[book]["borrow_count"])   
        if not found:
            print("not found") 
    
    elif behavior.lower()=="exit":
        print("exiting...")
        break
