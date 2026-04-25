from abc import ABC , abstractmethod

class LibraryItems(ABC):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def get_detials(self):
        pass 

class Book(LibraryItems):

    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def get_detials(self):
        return f"Book {self.title} by {self.author}"
    
class Magazine(LibraryItems):

    def __init__(self, title, issue):
        super().__init__(title)
        self.issue = issue 

    def get_detials(self):
        return f"Magazine: {self.title} Issue {self.issue}"
    


    
