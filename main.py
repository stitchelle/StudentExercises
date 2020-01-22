from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

# exercises

random_numbers = Exercise("Random Numbers", "Python")
planet_list = Exercise("Planet List", "Python")
dictionary_of_words = Exercise("Distionary of Words", "Python")
english_idioms = Exercise("English Idioms", "Python")

# cohorts

evening_cohort_six = Cohort("Evening Cohort 6")
day_cohort_two_six = Cohort("Day Cohort 26")
day_cohort_three_six = Cohort("Day Cohort 36")

# students

lauren = Student("Lauren","Riddle","LaurenRiddle")
christian = Student("Christian","Pippin","ChristianPippin")
michelle = Student("Michelle", "Johnson", "MichelleJohnson")
devin = Student("Devin", "Li", "DevinLi")

# assign cohort to students

lauren.student_cohort = day_cohort_three_six
christian.student_cohort = day_cohort_three_six
michelle.student_cohort = evening_cohort_six
devin.student_cohort = day_cohort_two_six

# Instructor

joe = Instructor("Joe","Sheppard","JoeShep", "Funny References")
jisie = Instructor("Jisie", "Davis", "JisieDavis", "Ignore Julian")
robert = Instructor("Robert", "Johnson", "RoJoIII", "Messing with People")

# assign cohort to instructor

joe.instructor_cohort = day_cohort_three_six
jisie.instructor_cohort = day_cohort_three_six
robert.instructor_cohort = evening_cohort_six

# assign exercises to students

lauren.exercises.append(random_numbers)
lauren.exercises.append(dictionary_of_words)

christian.exercises.append(planet_list)
christian.exercises.append(english_idioms)

michelle.exercises.append(random_numbers)
michelle.exercises.append(planet_list)

devin.exercises.append(planet_list)
devin.exercises.append(english_idioms)

# assign students to cohort

day_cohort_three_six.students.append(lauren)
day_cohort_three_six.students.append(christian)
day_cohort_two_six.students.append(devin)
evening_cohort_six.students.append(michelle)

# assign instructor to cohort

day_cohort_three_six.instructors.append(joe)
day_cohort_two_six.instructors.append(jisie)
evening_cohort_six.instructors.append(robert) 