# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.
class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def displayDetails(self):
        print(f"Book: {self.title}")
        print(f"Author: {self.author}")
class Novel(Book):
    def __init__(self, title, author, year, genre, numChapters):
        super().__init__(title, author, year)
        self.genre = genre
        self.numChapters = numChapters

    def displayDetails(self):
        print(f"{self.title} by {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Chapters: {self.numChapters}")

class Magazine(Book):
    def __init__(self, title, author, year, issueNumber, numArticles):
        super().__init__(title, author, year)
        self.issueNumber = issueNumber
        self.numArticles = numArticles

    def getArticleByTitle(self):
        pass


#main (polymorphism)
library = [
    Book("The Hobbit", "J.R.R. Tolkien", 1937),
    Novel("The Adventures of Captain Underpants", "Dav Pilkey", 1997, "Fiction", 12),
]

for item in library:
    item.displayDetails()  # Display details of each item in library
    print("•")