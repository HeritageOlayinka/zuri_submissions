class Student:
    #[assignment] Skeleton class. Add your code here
    def __init__(self,name, age, tracks,score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        pass
    
    def change_name(self,new_name):
        self.name = new_name

    def change_age(self,new_age):
            self.age = new_age

    def add_track(self, track):
        self.tracks.append(track)

    def get_score(self):
        if  isinstance(self.age,int):
            print("The student's new name is ", self.name)
            print("The student's new age is ", self.age)
            print("The student's new tracks are ", self.tracks)
            print("The student's score is ", self.score)
        else:
            print('Age must be int. Try again!')
 

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
