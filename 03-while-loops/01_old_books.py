book = input() #търсената книга
command = input() #No more books and books' titles
count_books = 0 # counter for books
is_found = False #boolen

while command != "No More Books": #докато командата е различна от "Няма повече книги"
    current_book = command # настоящата книга е равна на командата
    if current_book == book: #ако нястоящата книга съвпада с търсената:
        is_found = True # фактът, че сме я намерили става верен и прекратяваме търсенето
        break

    count_books += 1 # броят на взетите книги се увеличава
    command = input() #въвеждаме ново заглавие

if not is_found: #ако е вярно, че не сме я намерили, принтираме
    print("The book you search is not here!")
    print(f"You checked {count_books} books.")
else:
    print(f"You checked {count_books} books and found it.")