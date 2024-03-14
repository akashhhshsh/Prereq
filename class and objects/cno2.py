class instructor:
    #followers=0 #class object variable

    def  __init__(self,name,address):
        self.name  = name
        self.address = address
        self.followers = 0
    
    def display(self,subject_name):
        #self.subject=subject_name
        print(f'Hi I am {self.name} and I teach {subject_name}')
        
    def update_followers(self,follower_name):
        self.followers +=1
        
instructor_1=instructor('Akash','Delhi')
print(instructor_1.name)
instructor_1.display('Python')
instructor_2 = instructor('Arrya','Mumbai')
#print(instructor_2.follower)

instructor_1.update_followers('Arrya')
instructor_2.update_followers('Akash')
print(instructor_1.followers)
print(instructor_2.followers)