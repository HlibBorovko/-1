class HomeLibrary():

    def __init__(self,author, publication,genre):
        self.author = author
        self.publication = publication
        self.genre = genre
        print("Книга выбрана")


my_book = HomeLibrary("Alan Glynn",2011,"novel")
my_preferences = HomeLibrary("Arthur Conan Doyle",1877,"adventure detective")
print(my_book.publication)
print(my_preferences.author)
print(my_preferences.genre)