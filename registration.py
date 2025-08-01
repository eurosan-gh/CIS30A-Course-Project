#registration
class Student():
    class_list=[]

    def __init__(self):
        print("\nCan't wait to see you at the Smiski Yoga Studio!\n")

    def main():
        pass

    if __name__ == "__main__":
       main()

class Classes(Student):

    def __init__(self):
        super().__init__()
        try:
            self.name=str(input('Enter your name: '))
            assert self.name.isalpha()
     
        except:
            raise ValueError("Name has numbers. Re-enter name.")

        else:
            print("Name: ",self.name)

        try:
            self.phone=str(input("Enter a 10 digit phone number: "))
            assert self.phone.isnumeric()
            assert len(self.phone)==10
        except:
            raise ValueError("Enter 10 valid numbers only.")
        else:
            print("Phone Number: ",self.phone)
        
    def register(self):
        num=int(input("\nHow many classes are you registering for? (1-6): "))
        self.addClass(num) 

    def addClass(self,num):
        for i in range(num):
            course=input("\nName of class you want to add (enter as written in class schedule): ")
            self.class_list.append(course)

    def printClass(self):
        print("\nClasses you are enrolled in: ")
        for i in self.class_list:
            print(i,"class")

    def price(self):
        num=int(input("\nPlease re-enter number of courses you are signed up for: "))
        cost=num*25.99
        print("Total cost of registered classes: ",cost)


            
