# # Complete the function so it returns a function
# def create_quad_func(a, b, c):
#     '''return function f(x) = ax^2 + bx + c'''
#     return lambda x: a * x ** 2 + b * x + c

# # f = create_quad_func(2, 4, 6)
# g = create_quad_func(1, 2, 3)
# # print(f(2))
# print(g(2))


# print('Lambdas Exercise')


# signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
# print(sorted(signups)) # Lexicographic sort
# #write sorting by integer
# # print(sorted(signups, key=lambda x: int(x[3:]))) # Integer sort

# print('Lambdas Exercise')

# class Player:
#    def __init__(self, name, score):
#        self.name = name
#        self.score =  score

# Eric = Player('Eric', 116700)
# John = Player('John', 24327)
# Terry = Player('Terry', 150000)
# player_list = [Eric, John, Terry]


# #Exercise: Sort this by score using lambda!
# #write code here
# player_list.sort(key=lambda player: player.score, reverse=True)
# print([player.name for player in player_list])


#EXERCISE ON RAGNDOMNESS
#RAFFLE PRICE PICKER

#ASK HOW MANY PEOPLE RE ENTERING THE RAFFLE(AT LEAST THREE NAMES)
# use a loop to collect their names into a list
# ask for exactly three prize names into a lsit
# randomly pick 3 different winners from the participant list
# print out who wins which prize and make sure the final list is clearly marked as the grand prize

# hint use loop lists and  a tool that picks random items without repeats


# # name = input('enter names of people participating in the raffle draw(min:3): ')

# import random

# while True:
#     n_participant = int(input('number of people to participate? '))
#     if n_participant <= 3:
#         print('enter values > 3')
#         break
#     # if n_participant >= 3:
#     #     print("")

#     participants = []
#     for i in range(n_participant):
#         name = input(f'enter name{i + 1}; ').strip()

        
#     prizes = []
#     print("Enter eaxctly three prize names")
#     for i in range(3):
#             prize = input(f"enter prizes{i + 1} name: ").strip()

# winner = random.sample(participants, k=3)
# print("\n ---RAFFLE DRAW---")
# print(f"1st winner : {winner[0]} wins {prize[0]}")
# print(f"2nd winner : {winner[1]} wins {prize[1]}")
# print(f"GRAND PRICE winner : {winner[2]} wins {prize[2]}")


#student management system 
#1.add a student...input
#2.view all the student in the system
#3.search for a student by his id
#4.delete a student from the system
#5.update a student details
#6.quit the system
#a 'class' of student should have the following attributes: name, age, 1(id), multiple(course), gender and multiple(score)
# validations:
    # an age cannot be negative
    # score must be between zero and 100
    # student id must be unique
    # a name cannot be empty
class student:
    def __init__(self, name, age, student_id, courses, gender, scores):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = courses
        self.gender = gender
        self.scores = scores

    def __str__(self):
        return(f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"ID: {self.student_id}\n"
                f"Courses: {', '.join(self.courses)}\n"
                f"Gender: {self.gender}\n"
                f"Scores: {', '.join(self.scores)}\n")
students = []   
while True:
    print('STUDENT MANAGEMENT SYSTEM')
    print('1. Add a student')
    print('2. View all students')
    print('3. Search for a student by ID')
    print('4. Delete a student from the system')
    print('5. Update a student details')
    print('6. Quit the system')

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        student_name = input("Enter student name: ")
        student_age = int(input("Enter student age: "))
        student_id = input("Enter student ID: ")
        courses = input("Enter student courses (comma-separated): ").split(",")
        gender = input("Enter student gender: ")
        scores = input("Enter student scores (comma-separated): ").split(",")

        new_Student = student(student_name,student_age,student_id,courses,gender,scores)
        students.append(new_Student)

  
        print(new_Student)

    