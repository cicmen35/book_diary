#Data structure used for diary 
def create_diary():
    return []

#Function for inserting information about books into the diary
def insert_book(author, title, genre, year_of_release, pages, date_of_reading, diary):
    year_of_release = int(year_of_release)
    pages = int(pages)
    if not isinstance(author, str):
        raise TypeError("Invalid author input.")
    if not isinstance(title, str):
        raise TypeError("Invalid title input")
    for genres in genre:
        if not isinstance(genres, str):
            raise TypeError("Invalid genre input.")
    if not isinstance(year_of_release, int):
        raise TypeError("Invalid year input.")
    if not isinstance(pages, int):
        raise TypeError("Invalid page input.")
    if not isinstance(date_of_reading, str):
        raise TypeError("Invalid date of reading input.")
    book = {"author": author,                                        #The information is stored in a dictionary
            "title": title,                                          #The name of the variable is not that important so every book will be named just "book"
            "genres": genre,
            "year of release": year_of_release,
            "pages": pages,
            "date of reading": date_of_reading
    }
    if len(diary) != 0:
        for dict in diary:
            for info in dict.values():
                if info == title:                                            #Checking if the book we want to add isn't already in the diary 
                    print(f"The book {title} is already in the diary.")    
                    break
            else:
                diary.append(book)
                print(f"The book {title} has been added into the diary.")
                break
    else:
        diary.append(book)
        print(f"The book {title} has been added into the diary.")

#Function for searching for book in a diary
def search_book(author, title, diary):
    for book in diary:
        if book["author"] == author and book["title"] == title:
            print("The information about the book:")                            
            for key, value in book.items():
                print(f"{key}: {value}", end="\n")
            break
    else:
        raise KeyError("Author or title not found.")

#Function for deletion of book from the diary
def delete_book(author, title, diary):
    for book in diary:
        if book["author"] == author and book["title"] == title:
            print(f"The book {title} has been removed from the diary.")
            diary.remove(book)
            break
    else:
        raise KeyError("Author or title not found.")

#Function for deleting all books from the diary
def delete_record(diary):
    if len(diary) == 0:
        raise ValueError("The diary is empty.")
    else:
        diary.clear()
        print("The contents of the diary have been removed.")


'''
USER INTERFACE
'''

dennik = None
print("1. Create a reading diary.")
print("2. Add a book to the diary.")
print("3. Search a book in the diary.")
print("4. Delete a book from the diary.")
print("5. Delete the whole diary.")
print("6. Exit the program.")
while True:
    try:
        choice = input("Choose an action from 1-6: ")
        if choice == "1":
            if dennik is not None:
                print("Diary already exists.")
            else:
                dennik = create_diary()
                print("Diary created successfully.")
        elif choice == "2":
            if dennik is None:
                print("You need to create a diary first.")
            else:
                author = input("Name of the author: ")
                title = input("Title of the book: ")
                genres = input("Genre/s of the book: ").split(",")
                release_year = input("Release year of the book: ")
                page_count = input("Number of pages: ")
                read_date = input("Date of reading(dd/mm/yyyy): ")
                insert_book(author, title, genres, release_year, page_count, read_date, dennik)
        elif choice == "3":
            if dennik is None:
                print("You need to create a diary first.")
            else:
                author = input("Name of the author: ")
                title = input("Title of the book: ")
                search_book(author, title, dennik)
        elif choice == "4":
            if dennik is None:
                print("You need to create a diary first.")
            else:
                author = input("Name of the author: ")
                title = input("Title of the book: ")
                delete_book(author, title, dennik)
        elif choice == "5":
            if dennik is None:
                print("You need to create a diary first.")
            else:
                delete_record(dennik)
        elif choice == "6":
            print("Exiting diary program.")
            break
        else:
            print("Invalid choice.")
    except TypeError as e:
        print("Exception of TypeError has occured.")
        print(e)
    except KeyError as e:
        print("Exception of KeyError has occured.")
        print(e)
    except ValueError as e:
        print("Exception of ValueError has occured.")
        print(e)
