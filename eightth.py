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
        title = input("title : ").strip().casefold()
        while not title:
            print("title cannot be empty")
            title=input("title:").strip().casefold()
    author = input("author : ").strip().casefold()
    while True:
        try:
            year = int(input("year of publish : "))
            if 0<year<=datetime.now().year:
                break
            print("please enter a valid publication year")
        except ValueError:
            print("please enter a valid integer")
    available = True
    borrow_count=0.strip().casefold()
    list_of_books = {
        "title": title,
        "author": author,
        "year": year,
        "available": available,
        "borrow_count":borrow_count
    }
    return list_of_books


def borrow():
    name = input("enter your name : ").strip()
    while True:
        try:
            deadline = int(input("how many days do you want to keep this book ?  : "))
            if 1<=deadline<=7:
                break
            print("the borrowing period must be between 1 and 7 days")
        except ValueError:
            print("please enter a valid integer")
    while True:
        try:
            age = int(input("enter your age : "))
            if age>=18:
                break
            print("you must be at least 18 years old")
        except ValueError:
            print("please enter a valid integer")
            
    sign = input("enter your sign to ensure you will return the book on the exact time >>>> ").strip()
    address = input("enter your address").strip()
    phone = input("enter your phone number").strip()
    date_of_borrow = datetime.now()
    borrower = {
        "name": name,
        "deadline": deadline,
        "age": age,
        "sign": sign,
        "address": address,
        "phone": phone,
        "date_of_borrow": date_of_borrow
    }
    return borrower


def return_book():
    name = input("enter your name : ").strip()
    date_of_return = datetime.now()
    sign = input("enter your sign >>> ").strip()
    bookname = input("enter book name").strip().casefold()
    returner = {
        "name": name,
        "date_of_return": date_of_return,
        "sign": sign,
        "bookname": bookname
    }
    return returner
def show_history():
    if not borrow_history:
        print("no borrowing history")
    return
    for record in borrow_history:
        print("-"*30)
        print("book : ", record["title"])
        print("borrow : ", record["name"])
        print("borrow at : ", record["date_of_borrow"].strftime("%Y-%m-%d-%H:%M"))
        if "date_of_return" in record:
            print("returned at : ", record["date_of_return"].strftime("%Y-%m-%d-%H:%M))
        else:
            print("status : not returned")   
    print("-"*30)

all_books = {}
borrow_history=[]

while True:
    try:
        i = int(input("enter initial quantity : "))
        if i >=0:
            break
        print("quantity cannot be negative")
    except ValueError:
        print("please enter a valid integer")
for count in range(i):
    library = books()
    while library["title"] in all_books:
        print("this titla already exists")
        library=books()
    all_books[library["title"]] = library
while True:
    behavior = input("what you ask ? >>> ").strip().casefold()
    if behavior == "add":
        answer = input("what book do you want to add ?  enter here >>> ").strip().casefold()
        if answer in all_books:
            print("already exists")
        else:
            library = books(answer)
            all_books[library["title"]] = library
    elif behavior== "show all":
        print(all_books)

    elif behavior.lower() == "search":
        question = input("based on what are you searching ? title / author / year ? ").strip().casefold()
        found = False
        if question.lower()== "title":
            q = input("what title are you looking for ?  >>>>").strip().casefold()
            if q in all_books:
                    print(all_books[q])
                    found = True

        elif question.lower()== "author":
            e = input("what author areyou looking for ? >>> ").strip().casefold()
            for book in all_books.values:
                if book["author"].strip().casefold() == e:
                    print(book)
                    found = True
        elif question.lower() == "year":
            try:
                r = int(input("what yea are you looking for? >>> "))
                for book in all_books:
                    if book["year"] == r:
                        print(book)
                        found = True
            except ValueError:
                print("please enter a valid year")
                found=True
        else:
            print("invalid search option")
            found=True
        if not foud:
            print("no matching books found")
    elif behavior== "delete":
        v = input("what book do you want to delete ? >>> ").strip().casefold()
        if v not in all_books:
            print("book not found")
        elif not all_books[v]["available"]:
            print("this book is currently borrowed and cannot be deleted")
        else:
            delall_books[v]
            print("book deleted successfully")
    elif behavior== "borrow":
        borrowing = borrow()
        if not borrowing["name"] or not borrowing["sign"] or not borrowing["address"] or not borrowing["phone"]:
            print("all borrower information is required")
            continue
            y = input("what book do you want to borrow ? >>>").strip().casefold()
            if y not in all_books:
                print("book not found")
            elif not all_books[y]["available"]:
                print("this book is not available")
            else:
                o = input("are you sure you want to borrow this book ? ").strip().casefold()
                    if o in ["yes", "y", "yeah"]:
                        borrowing["title"]=y
                        all_books[y]["borrow_count"]+=1
                        all_books[y]["borrower"]=borrowing
                        all_books[y]["available"]=False
                        borrow_history.append(borrowing)
                        print("you should return this book within",borrowing["deadline"], "days")
                        print("the book ",y,"has been borrowed")
                    else:
                        print("borrowing cancelled")
    elif behavior== "return":
        returning = return_book()
        bookname=returning["bookname]
        if bookname not in all_books:
            print("book not found")
            continue
        book=all_books["bookname"]
        if book["available"]:
            print("this book has not been borrowed")
            continue
        borrowing=book["borrower"]
        if( returning["name"].casefold() == borrowing["name"].casefold() and  and returning["sign"] == borrowing["sign"] ):
            deadline_date= returning["date_of_return"]+ timedelta(days=borrowing["deadline"])  
            late_days=max(0,(returning["date_of_return"].date()-deadline_date.date()).days)
            book["available"] = True
            borrowing["date_of_return"]=returning["date_of_return"]
            del book["borrower"]
            print("Thank you for returning the book")
            if late_days>0:
                print("the book was returened",late_days,"day(s) later")
            else:
                print("the book was returend on time")
        else:
            print("borrow information does not match")
    elif behavior=="history":
        show_history()
    elif behavior=="borrow count":
        k=input("for what book's history are you looking for ? >>> ")
        found=False
        for book in all_books:
            
            if all_books[book]["title"]==k:
                found=True
                print(all_books[book]["borrow_count"])   
        if not found:
            print("not found") 
    
    elif behavior=="exit":
        print("exiting...")
        break
