class Book:
    def __init__(self,title,author,price):
        self.title =title
        self.author =author
        self._price =price  

    def get_price(self):
        return self._price

    def set_price(self,new_price):
        if new_price >=0:
            self._price =new_price
        else:
            print("Price must be greater than 0.")

    "Display book information"
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self._price}")

class Ebook(Book):
    def __init__(self,title,author,price,size):
        super().__init__(title,author,price)
        self.size =size

    def display(self):
        super().display()
        print(f"File Size: {self.size} MB")

book1 =Book("Machine learning","Hour tzy",89)
book1.display()

book1.set_price(90)

book2 =Ebook("Financial","gg rolex",78,314)
book2.display()



        
    
              