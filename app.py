import json

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their books."""
    
    def __init__(self):
        """Initializa a new book collection with an empty list and set up file storage.""" 
        self.book_list = []
        self.storage__file = "books_data.json"
        self.read_from_file()
        
    def read_from_file(self):
        """"Load save books from a JSON file into memory.
        If the file doesn't exit or is corrupted,start with an empty collection. """   
        try:
            with open(self.storage__file,"r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) : 
            self.book_list = []
         
    def save_to_file(self):
        """"Store the current book collection to a JSON file for permanent storage"""
        with open(self.storage__file,"w") as file:
            json.dump(self.book_list, file, indent=4)
            
    def create_new_book(self):
        """"Add a new book to the collection by gathering information from the user"""  
        book_title = input("Enter Book Title: ")   
        book_author = input("Enter author: ")
        publication_year = input("Enter publication year: ")
        book_genre = input("Enter book genre: ")
        is_book_read = (
            input("Have you read this Book? (yes/no): ").strip().lower() == "yes"
        ) 
        new_book = {
           "title" : book_title,
           "author" : book_author,
           "year" : publication_year,
           "genre" : book_genre,
           "read" : is_book_read,
        } 
        
        self.book_list.append(new_book)
        self.save_to_file()
        print("\nBook Added Successfully\n\n")
        
    def delete_book(self):
        """"Remove a Book from a collection using its title."""
        book_title = input("Enter the title of the book to remove: ")  
        
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("\nBook removed Successfully\n\n")
                return
        print("\nBook Not Found.\n\n")    
        
    def find_book(self):
        """"Search for books in the collection by title or author""" 
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your Choice: ")
        search_text = input("Enter Search Term: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]    
        
        if found_books:
            print("Matching Books...")
            for index,book in enumerate(found_books,1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"\n{index}.{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}\n\n"
                )
        else:
            print("\nNo Matching Books Found.\n\n")
            
    
    def update_book (self) :
        """"Modify the details of an existing book in the collection."""   
        book_title = input("Enter the Title of the Book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("leave Blank to keep existing value.")
                book["title"] = input(f"New title ({book["title"]}): ") or book["title"]
                book["author"] = (
                    input(f"New author ({book["author"]}): ") or book["author"]
                    )
                book["year"] = input(f"New year ({book["year"]}): ") or book["year"]
                book["genre"] = input(f"New genre ({book["genre"]}): ") or book["genre"]
                book["read"] = (
                    input("Have you read this Book? (yes/no): ").strip().lower() == "yes"
                    )
                
                self.save_to_file()
                print("\nBook Updated Successfully.\n\n")
               
                return
            
            print("\nBook Not Found.\n\n")
            
    def show_all_books (self) : 
        """"Display all books in the collection with their details.""" 
        if not self.book_list:
            print("\nYour collection is empty\n") 
            return
        
        print("Your Book Collection: \n")
        for index,book in enumerate(self.book_list,1):
            reading_status = "Read" if book ["read"] else "Unread"  
            print(f"\n{index}.{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}\n")
        print()  
        
        
    def show_reading_progress(self):
        """"Calculate and display statistics about your readung projects."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0
        )  
        print(f"\nTotal Books in collection: {total_books}\n")
        print(f"Reading Progress: {completion_rate:.2f}%\n")
                
                
    def start_application(self):
        """"Run the main application loop with a user_friendly menu interface."""
        while True:
            print("Welcome to the Book Collection Manager")
            print("1. Add a new Book.")  
            print("2. Remove a Book.")
            print("3. Search for Books.")
            print("4. Update Book details.")
            print("5. View all Books.")
            print("6. View reading Books.")  
            print("7. Exit")  
            
            user_choice = input("Please choose an option (1-7): ")  
            
            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()    
            elif user_choice == "3": 
                self.find_book()   
            elif user_choice == "4":
                self.update_book()    
            elif user_choice == "5": 
                self.show_all_books()   
            elif user_choice == "6":  
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("Thank You for using Book Collection Manager.GoodBye!.")  
                break  
            else:
                print("Invalid Choice.Please Try Again.")
                

if __name__ == "__main__":
    book_manager = BookCollection()   
    book_manager.start_application()           
                
             
                            
            
             
        
        
                       