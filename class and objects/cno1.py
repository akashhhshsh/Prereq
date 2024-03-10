class instructor:
    def  __init__(self,instructor_name,address,followers):
        self.name=instructor_name
        self.address=address
        self.followers=0
        # print('creating a new object')

instructor_1 = instructor('Akash','Delhi',100)
# instructor_1.name = "Akash"
# instructor_1.address = 'Delhi'
print(instructor_1.name)
print(instructor_1.followers)

#print(type(instructor_1))

instructor_2 = instructor('Arrya','Mumbai')
# instructor_2.name = "Arrya"
# instructor_2.address = 'Mumbai'
print(instructor_2.name)