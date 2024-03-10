class instructor:
    follower=0 #class object variable
    def  __init__(self,name,address):
        self.name=name
        self.address=address
        #self.followers=0
    def display(self):
        print('Hi')
        
instructor_1=instructor('Akash','Delhi')
print(instructor_1.name)
print(instructor_1.display())
instructor_2 = instructor('Arrya','Mumbai')
print(instructor_2.follower)