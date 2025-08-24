class library:
    def __init__(self,title,author,stock):
        self.title=title
        self.author=author
        self.stock=stock
class borrow(library):
    def borrow(self,title,author,n):
        if self.stock<0:
            print("not available")
        else:
            self.stock-=n
            print(f"{title} by {author} is borrowed . Available stock is {self.stock}")
class retur(borrow):
    def returned(self,title,author,n):
        self.stock+=n
        print(f"{title} by {author} is returned . Available stock is {self.stock}")
obj=retur("h","k",3)
obj.returned("abc","him",10)
obj.borrow("def","her",3)