class Todo(object):

    def __init__(self, category, duration, task, deadline=None, priority=1, timeslot=[]):
        self.category = category
        if self.category == "lecture" or self.category == "discussion":
            self.priority = 0
        else:
            self.priority = priority
        self.duration = duration
        self.deadline = deadline
        self.task = task

    def __repr__(self):
        return "<Todo Object: " + self.task + ">"

    def increment_priority(self):
        self.priority += 1

    def decrement_priority(self):
        self.priority -= 1

    def get_category(self):
        return self.category

    def get_task(self):
        return self.task
