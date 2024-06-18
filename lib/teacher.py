#!/usr/bin/env python

from user import User

import random

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge=knowledge):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        return random.choice(self.knowledge)
    
# Create a new Teacher instance with the first name "John" and last name "Doe"
teacher = Teacher("Daniel", "Beyene")

# Access the teacher's first name, last name, and knowledge
print(teacher.first_name)  
print(teacher.last_name)   
print(teacher.knowledge)   