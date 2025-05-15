# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.
class Book():
    def __init__(self):
        self.title = str
        self.author = str
        self.year = int
        self.numPages = int
    
    def displayDetails(self):
    

class Novel(Book):
    def __init__(self):
        self.genre = str
        self.numChapters = int

class Magazine(Book):
    def __init__(self):
        self.issueNumber = int
        self.numArticles = int
    
    def getArticleByTitle(self):