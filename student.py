class Student:

    def __init__(self, first, last, slack):
        # Establish the properties of each book
        # with a default value
        self.first_name = first
        self.last_name = last
        self.slack_handle = slack
        self.student_cohort = ""
        self.exercises = []