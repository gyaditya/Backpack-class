#Task 1
class Backpack:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False

    def openBag(self):
        self.open = True
        print("Backpack is now open.")

    def closeBag(self):
        self.open = False
        print("Backpack is now closed.")

    def putin(self, item):
        if self.open:
            self.items.append(item)
            print(f"{item} has been added to the backpack.")
        else:
            print("Backpack is closed. Please open it to add items.")

    def takeout(self, item):
        if self.open and item in self.items:
            self.items.remove(item)
            print(f"{item} has been taken out of the backpack.")
        else:
            print("Backpack is closed or item is not in the backpack.")



#Task 2

backpack1 = Backpack("blue", "small")
backpack2 = Backpack("red", "medium")
backpack3 = Backpack("green", "large")

#Task 3
backpack1.openBag()
backpack1.putin("lunch")
backpack1.putin("jacket")
backpack1.closeBag()
backpack1.openBag()
backpack1.takeout("jacket")
backpack1.closeBag()