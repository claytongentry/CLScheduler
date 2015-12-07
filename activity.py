class Todo(object):

    def get_timeslot(self):
        if self.timeslot:
            return self.timeslot
        else:
            return False

class Lesson(Todo):
    def __init__(self, starttime, endtime, subject, location, duration):
        self.starttime = starttime
        self.endtime = endtime
        self.subject = subject
        self.location = location
        self.duration = self.endtime - self.starttime
        self.priority = 0 # Classes get top priority

class Task(Todo):

    def __init__(self, deadline, priority):
        self.deadline = deadline
        self.priority = priority

    def days_left(self):
        return self.deadline - current_date

class Exam(Task):

    def __init__(self, subject, required_hours):
        self.subject = subject
        self.required_hours = required_hours

    def get_required_hours(self):
        return self.required_hours

    def set_required_hours(self, rh):
        self.required_hours = rh

    def complete_hours(self, completed_hours):
        self.required_hours = self.required_hours - completed_hours

class Essay(Task):

    def __init__(self, subject, wordcount):
        self.subject = subject
        self.wordcount = wordcount
        self.words_per_hour = 150
        self.duration = self.wordcount / self.words_per_hour

    def set_words_per_hour(self, wph):
        self.words_per_hour = wph

    def get_total

class Reading(Task):

    def __init__(self, subject, title, author, total_pages):
        self.subject = subject
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.pages_read = 0

    def pages_left(self, pages, pages_read):
        return pages - pages_read
