class Publication:
    def __init__(self,title,author):
        self.__title = title
        self.__author = author
    def get_title(self):
        return self.__title
    def set_title(self):
        self.__title = title
    def get_author(self):
        return self.__author
    def set_author(self):
        self.__author = author
    def display(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")

class Book(Publication):
    def __init__(self,title,author,no_of_pages):
        super().__init__(title,author)
        self.set_no_of_pages(no_of_pages)
    def get_no_of_pages(self):
        return self.__no_of_pages
    def set_no_of_pages(self,no_of_pages):
        if no_of_pages <= 0:
            print("The number of pages must be positive.")
        else:
            self.__no_of_pages = no_of_pages
    def display(self):
        super().display()
        print(f"Number of pages: {self.__no_of_pages}")

class Magazine(Publication):
    def __init__(self, title, author, issue_no):
        super().__init__(title, author)
        self.set_issue_no(issue_no)
    def get_issue_no(self):
        return self.__issue_no
    def set_issue_no(self,issue_no):
        if issue_no <= 0:
            print("The issue number must be positive.")
        else:
            self.__issue_no = issue_no
    def display(self):
        super().display()
        print(f"Issue Number: {self.__issue_no}")

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
pub2 = Publication("Python Tutorial", "Guido Van Rossum")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("To Kill A Mockingbird", "Harper Lee", 281)
mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Rolling Stone", "Various Authors", 1416)

print("Publication Information:")
pub1.display()

print("\nPublication 2 Information:")
pub2.display()

print("\nBook Information:")
book1.display()
book1.set_no_of_pages(310)
print(book1.get_no_of_pages())

print("\nBook 2 Information:")
book2.display()

print("\nMagazine Information:")
mag1.display()
print(mag1.get_issue_no())

print("\nMagazine 2 Information:")
mag2.display()
