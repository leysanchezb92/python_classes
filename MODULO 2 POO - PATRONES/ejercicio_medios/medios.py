from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date

    @abstractmethod
    def describe(self):
        return f" Media title: {self.title} by {self.author}, published on {self.publication_date}"

class Book(Media):
    def __init__(self, title, author, publication_date, number_pages, gender):
        super().__init__(title, author, publication_date)
        self.number_pages = number_pages
        self.gender = gender

    def describe(self):
        return f" Book title: {self.title} by {self.author}, published on {self.publication_date}, {self.number_pages} pages, Genre: {self.gender}"

class Magazine(Media):
    def __init__(self, title, author, publication_date, topic, frequency):
        super().__init__(title, author, publication_date)
        self.topic = topic
        self.frequency = frequency

    def describe(self):
        return f" Magazine title: {self.title} by {self.author}, published on {self.publication_date}, Topic: {self.topic}, Frequency: {self.frequency}"

class Newspaper(Media):
    def __init__(self, title, author, publication_date):
        super().__init__(title, author, publication_date)

    def describe(self):
        return f" Newspaper title: {self.title} by {self.author}, published on {self.publication_date}" 
    

# List of media data
media_data = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", "1925", 180, "Novel"),
    Book("1984", "George Orwell", "1949", 328, "Dystopian"),
    Book("One Hundred Years of Solitude", "Gabriel García Márquez", "1967", 417, "Magical Realism"),
    Book("Brave New World", "Aldous Huxley", "1932", 268, "Science Fiction"),
    Magazine("National Geographic", "Various", "2023-09", "Science and Nature", "Monthly"),
    Magazine("Time", "Various", "2023-10", "Current Events", "Weekly"),
    Magazine("Scientific American", "Various", "2023-08", "Science", "Monthly"),
    Magazine("The New Yorker", "Various", "2023-11", "Culture", "Weekly"),
    Newspaper("The New York Times", "Various", "2023-10-01"),
    Newspaper("The Guardian", "Various", "2023-10-02"),
    Newspaper("El País", "Various", "2023-10-01"),
    Newspaper("Le Monde", "Various", "2023-09-30")
]
    
for media in media_data:
    print(media.describe())