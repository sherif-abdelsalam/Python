# from abc import ABC, abstractmethod

# # ✅ Abstract base class (like interface in C#/C++)
# class LibraryItem(ABC):
#     def __init__(self, title):
#         self._title = title  # protected attribute
#         self.__available = True  # private attribute

#     ## What is abstract method?
#     # An abstract method is a method that is declared but contains no implementation.
#     # Abstract methods are meant to be overridden in derived classes.
#     @abstractmethod
#     def get_info(self):
#         pass

#     @property
#     def is_available(self):
#         return self.__available

#     @is_available.setter
#     def is_available(self, status):
#         if isinstance(status, bool):
#             self.__available = status
#         else:
#             raise ValueError("Availability must be a boolean")

#     def borrow_item(self):
#         if self.__available:
#             self.__available = False
#             print(f"{self._title} has been borrowed.")
#         else:
#             print(f"{self._title} is not available.")

#     def return_item(self):
#         self.__available = True
#         print(f"{self._title} has been returned.")

# class Book(LibraryItem):
#     def __init__(self, title, author, pages):
#         super().__init__(title)
#         self.author = author
#         self.pages = pages

#     def get_info(self):
#         return f"Book: {self._title} by {self.author}, {self.pages} pages"


# class DVD(LibraryItem):
#     def __init__(self, title, duration, genre):
#         super().__init__(title)
#         self.duration = duration
#         self.genre = genre

#     def get_info(self):
#         return f"DVD: {self._title}, Duration: {self.duration} mins, Genre: {self.genre}"



# # Create objects
# book1 = Book("1984", "George Orwell", 328)
# dvd1 = DVD("Inception", 148, "Sci-Fi")

# # Display info (Polymorphism)
# print(book1.get_info())
# print(dvd1.get_info())

# # Borrow and return
# book1.borrow_item()
# book1.borrow_item()  # Should say not available

# dvd1.borrow_item()
# dvd1.return_item()

# # Using property getter
# print("Is book available?", book1.is_available)

# # Using property setter with validation
# try:
#     book1.is_available = "yes"  # ❌ Raises ValueError
# except ValueError as e:
#     print(e)

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
# my_car.get_make_model()
# my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
# your_car.get_make_model()
# your_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along..')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')


class GolfCart(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print('\n\n')

for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()