#### Final Project! Let's go! This is CS50p!
'''Random Gym Workout Challenge Generator!'''

import datetime
import time
import secrets
import random

class User:
    def __init__(self, name, gender, age, weight, height):
        if not name:
            raise ValueError('Missing Name')
        today = datetime.date.today()
        self.name = name
        self.gender = gender
        self.age = int(today.year)-int(age)
        self.weight = weight
        self.height = height

class Workout:
    def __init__(self, exercise, bodytype, upperlower):
        self.exercise = exercise
        self.bodytype = bodytype
        self.upperlower = upperlower

gym_exercise = [
    {'exercise':'Bench Press', 'bodytype':'bigcompound', 'upperlower':'upper', 'movement':'double'},
    {'exercise':'Squat', 'bodytype':'bigcompound', 'upperlower':'lower','movement':'double'},
    {'exercise':'Deadlift', 'bodytype':'bigcompound', 'upperlower':'lower','movement':'double'},
    {'exercise':'Military Press', 'bodytype':'compound', 'upperlower':'upper','movement':'double'},
    {'exercise':'Lateral Raise', 'bodytype':'isolated', 'upperlower':'upper','movement':'singular'},
    {'exercise':'Dumb Bell Curl', 'bodytype':'isolated', 'upperlower':'upper','movement':'singular'},

]

def main():
    user = get_user()
    print()
    print("Hello", user.name)
    print("Age:", user.age,"Gender:", user.gender,"Height:", user.height,"Weight", user.weight)
    bmi_value = bmi(user.height, user.weight)
    print("Your BMI is", bmi_value)
    print("You are in the", interpret_bmi(bmi_value), "range")
    loading(0.5)
    wo1 = random_workout()
    wo2 = random_workout()
    wo3 = random_workout()
    print("First Challenge:",wo1['exercise'], "on", round(intensity(wo1, user.gender, interpret_bmi(bmi_value))*float(user.weight)*2)/2,"KG")
    print("Second Challenge:",wo2['exercise'],"on", round(intensity(wo2, user.gender, interpret_bmi(bmi_value))*float(user.weight)*2)/2,"KG")



def get_user():
    while True:
        try:
            name = input("Name: ")
            if name == "":
                print("Please re-enter name")
                raise ValueError
            gender = input("Sex (M/F/Blank): ")
            while gender.lower() not in ['blank','','m','f']:
                try:
                    print('Please re-enter Gender (M/F/Blank)')
                    gender = input("Sex (M/F/Blank): ")
                except:
                    pass
            age = input("Year of Birth (YYYY): ")
            while len(age) != 4:
                try:
                    print('RGym Challenge is recommendated for age 15 and above. Please be between age 15-99')
                    age = input("Year of Birth (YYYY): ")
                except:
                    pass
            weight = input("Weight (KG): ")
            while round(float(weight)) < 20 or round(float(weight)) >500:
                try:
                    print('Please enter valid weight, last value was', weight)
                    weight = input("Weight (KG): ")
                except:
                    pass
            height = input("Height (CM): ")
            return User(name, gender, age, weight, height)
        except (ValueError, AttributeError):
            print('Please retry!')
            continue
        break

def interpret_bmi(bmi):
    if bmi <18.5:
        return 'Underweight'
    elif bmi <= 24.9:
        return 'Healthy Weight'
    elif bmi <=29.9:
        return 'Overweight'
    else:
        return 'Obese'



def bmi(height, weight):
    bmi_height = float(height)/100
    bmi = float(weight)/(bmi_height**2)
    return(round(bmi,2))



def random_workout():
    return(secrets.choice(gym_exercise))



def intensity(wo, g, bmi_value):
    intensity = float(0)
    if g.upper() == 'M':
        intensity = float(1)
    else:
        intensity = float(0.5)
    if wo['bodytype'] == 'bigcompound':
        intensity = intensity + round(random.uniform(0.1,0.5),2)
        if wo['upperlower'] == 'lower':
            intensity = intensity + round(random.uniform(0.1,0.3),2)
    elif wo['bodytype'] == 'compound':
        intensity = intensity + round(random.uniform(0,0.1),2)
        if wo['upperlower'] == 'lower':
            intensity = intensity + round(random.uniform(0.1,0.2),2)
    elif wo['bodytype'] == 'isolated':
        intensity = intensity/3
    if wo['movement'] == 'singular':
        intensity = intensity/2
    if bmi_value == 'Overweight':
        intensity = intensity/2
    elif bmi_value == 'Obese':
        intensity = intensity/3
    return intensity

def loading(t):
    print("Generating challenge...")
    time.sleep(t)
    print(".")
    time.sleep(t)
    print("..")
    time.sleep(t)
    print("...")

if __name__ == "__main__":
    main()


##############################################################################################################################2nd try

# import csv
# import datetime
# import time
# import secrets
# import random

# class User:
#     def __init__(self, name, gender, age, weight, height):
#         if not name:
#             raise ValueError('Missing Name')
#         today = datetime.date.today()
#         self.name = name
#         self.gender = gender
#         self.age = int(today.year)-int(age)
#         self.weight = weight
#         self.height = height

#     # def __str__(self):
#     #     return(self.gender)

#     # def intensity(self, wo):
#     #     intensity = float(0)
#     #     if self.gender == 'M':
#     #         intensity = float(1)
#     #     else:
#     #         intensity = float(0.5)
#     #     if wo['bodytype'] == 'bigcompound':
#     #         intensity + random.uniform(0.1,0.5)
#     #         if wo['upperlower'] == 'lower':
#     #             intensity + random.uniform(0.1,0.5)
#     #     elif wo['bodytype'] == 'compound':
#     #         intensity + random.uniform(0.1,0.2)
#     #         if wo['upperlower'] == 'lower':
#     #             intensity + random.uniform(0.1,0.3)
#     #     elif wo['bodytype'] == 'isolated':
#     #         intensity = intensity/3
#     #     if wo['movement'] == 'singular':
#     #         intensity = intensity/2
#     #     return intensity

# class Workout:
#     def __init__(self, exercise, bodytype, upperlower):
#         self.exercise = exercise
#         self.bodytype = bodytype
#         self.upperlower = upperlower

# gym_exercise = [
#     {'exercise':'Bench Press', 'bodytype':'bigcompound', 'upperlower':'upper', 'movement':'double'},
#     {'exercise':'Squat', 'bodytype':'bigcompound', 'upperlower':'lower','movement':'double'},
#     {'exercise':'Deadlift', 'bodytype':'bigcompound', 'upperlower':'lower','movement':'double'},
#     {'exercise':'Military Press', 'bodytype':'compound', 'upperlower':'upper','movement':'double'},
#     {'exercise':'Lateral Raise', 'bodytype':'isolated', 'upperlower':'upper','movement':'singular'},
#     {'exercise':'Dumb Bell Curl', 'bodytype':'isolated', 'upperlower':'upper','movement':'singular'},

# ]

# def main():
#     user = get_user()
#     print("User:", user.name)
#     bmi_value = bmi(user.height, user.weight)
#     print("Your BMI is", bmi_value)
#     print("You are in the", interpret_bmi(bmi_value), "range")
#     print(user.age, user.gender, user.height, user.weight)
#     # print("Generating challenge...")
#     # time.sleep(0.5)
#     # print(".")
#     # time.sleep(0.5)
#     # print("..")
#     # time.sleep(0.5)
#     # print("...")
#     wo1 = random_workout()
#     wo2 = random_workout()
#     wo3 = random_workout()
#     print("First Challenge:",wo1['exercise'], "on", round(intensity(wo1, user.gender, interpret_bmi(bmi_value))*float(user.weight)*2)/2,"KG")
#     print("Second Challenge:",wo2['exercise'],"on", round(intensity(wo2, user.gender, interpret_bmi(bmi_value))*float(user.weight)*2)/2,"KG")



# def get_user():
#     while True:
#         try:
#             name = input("Name: ")
#             if name == "":
#                 print("Please re-enter name")
#                 raise ValueError
#             gender = input("Sex (M/F/Blank): ")
#             while gender.lower() not in ['blank','','m','f']:
#                 try:
#                     print('Please re-enter Gender (M/F/Blank)')
#                     gender = input("Sex (M/F/Blank): ")
#                 except:
#                     pass
#             age = input("Year of Birth (YYYY): ")
#             while len(age) != 4:
#                 try:
#                     print('RGym Challenge is recommendated for age 15 and above. Please be between age 15-99')
#                     age = input("Year of Birth (YYYY): ")
#                 except:
#                     pass
#             weight = input("Weight (KG): ")
#             while round(float(weight)) < 20 or round(float(weight)) >500:
#                 try:
#                     print('Please enter valid weight, last value was', weight)
#                     weight = input("Weight (KG): ")
#                 except:
#                     pass
#             height = input("Height (CM): ")
#             return User(name, gender, age, weight, height)
#         except (ValueError, AttributeError):
#             print('Please retry!')
#             continue
#         break

# def interpret_bmi(bmi):
#     if bmi <18.5:
#         return 'Underweight'
#     elif bmi <= 24.9:
#         return 'Healthy Weight'
#     elif bmi <=29.9:
#         return 'Overweight'
#     else:
#         return 'Obese'



# def bmi(height, weight):
#     bmi_height = float(height)/100
#     bmi = float(weight)/(bmi_height**2)
#     return(round(bmi,2))



# def random_workout():
#     return(secrets.choice(gym_exercise))



# def intensity(wo, g, bmi_value):
#     intensity = float(0)
#     if g.upper() == 'M':
#         intensity = float(1)
#     else:
#         intensity = float(0.5)
#     if wo['bodytype'] == 'bigcompound':
#         intensity = intensity + round(random.uniform(0.1,0.5),2)
#         if wo['upperlower'] == 'lower':
#             intensity = intensity + round(random.uniform(0.1,0.3),2)
#     elif wo['bodytype'] == 'compound':
#         intensity = intensity + round(random.uniform(0,0.1),2)
#         if wo['upperlower'] == 'lower':
#             intensity = intensity + round(random.uniform(0.1,0.2),2)
#     elif wo['bodytype'] == 'isolated':
#         intensity = intensity/3
#     if wo['movement'] == 'singular':
#         intensity = intensity/2
#     if bmi_value == 'Overweight':
#         intensity = intensity/2
#     elif bmi_value == 'Obese':
#         intensity = intensity/3

#     return intensity





# if __name__ == "__main__":
#     main()


############################################################################################################################################################1st try
#     class User:
#     def __init__(self, name, gender, age, height, weight):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.height = height
#         self.weight = weight

#     @property
#     def name(self):
#         return self._name

# class Gym:
#     def __init__(self, exercise, category_body, category_ul, exercise_type):
#         self.exercise = exercise
#         self.category_body = category_body
#         self.category_ul = category_ul
#         self.exercise_type = exercise_type




# def main():
#     user = User()
#     user.name(input("Enter Name: "))
#     user.gender(input("Enter Gender: "))
#     user.age(input("Enter Age: "))
#     user.height(input("Enter Height (cm): "))
#     user.weight(input("Enter Weight (kg): "))
#     print("User:", user.name)
#     print("BMI:", user.weight/(user.height*user.height))


# def createuser():
#     user_data = {'user': user,'age':age,'height':height,'weight':weight}
#     try:
#         user = input("Your Name: ")
#         age = int(input("Your Age: "))
#         height = int(input("Your Height (cm): "))
#         weight = float(input("Your Weight (kg): "))
#         file = open(user.txt)

#     except ValueError:
#         pass




# def function_2():
#     ...



# def function_n():
#     ...



# if __name__ == "__main__":
#     main()