import itertools
from datetime import datetime, timedelta
from todo import Todo

INCREMENT_SIZE = 10 # minutes
READ_PAGES_PER_HOUR = 20.0
WRITE_WORDS_PER_HOUR = 200.0

SCHEDULE_FILE = "standing.txt"
TASKLIST_FILE = "tasks.txt"

class Schedule:

    def __init__(self, start, end):
        self.increments=[]
        self.tasks=[]
        self.init_increments(start, end, INCREMENT_SIZE)
        self.set_lessons(SCHEDULE_FILE)
        self.schedule_tasks(TASKLIST_FILE)

    def __repr__(self):
        return "Schedule for", date, ": ", len(self.tasks), "items"

    def get_tasks(self):
        return self.tasks

    # Initialize (empty) increment slots in schedule
    def init_increments(self, start, end, size):
        time = start
        inc = 0
        while time < end:
            self.increments.append(Increment(time))
            inc += size
            time = start + timedelta(minutes=inc)

    def set_lessons(self, schedule_file):
        with open(schedule_file, "r") as sched:
            string_sched = sched.read()[:-1] # Cuts last newline
            classes = []
            for element in string_sched.split("\n\n"):
                if datetime.now().strftime("%A").upper() in element:
                    classes = element.split("\n")[1:]
                    break

        for lesson in classes:
            class_tuple = lesson.split(", ")
            fmt = "%H:%M"
            start = datetime.strptime(class_tuple[0], fmt)
            end = datetime.strptime(class_tuple[1], fmt)
            duration = end - start
            subject = class_tuple[2]
            # location = class_tuple[3]
            is_disc = False
            if "Disc" in subject:
                category = "discussion"
            else:
                category = "lecture"
            new_class = Todo(category, duration, subject)
            self.fill_timeslot(new_class, start, end)

    def schedule_tasks(self, tasklist):
        # Initialize todos from file in schedule object
        self.set_tasks(tasklist)
        sorted_tasks = sorted(self.tasks, key=lambda x: x.priority)
        for task in sorted_tasks:
            slot_filled = self.find_and_fill_slot(task)

    # Returns tuple of start and end increments
    def find_and_fill_slot(self, task):
        try:
            days_to_deadline = int(str(task.deadline - datetime.now()).split(", ")[0].split(" ")[0])
        except: # Deadline < 24 hours away
            days_to_deadline = 1

        daily_duration = task.duration / days_to_deadline

        for increment in self.increments:
            if not increment.get_is_filled():
                start = increment.time
                end = start + timedelta(minutes=daily_duration)
                try:
                    self.fill_timeslot(task, start, end)
                    return True
                except: # increment in timeslot is already filled
                    continue

        # If no slot of sufficient size is found...
        return False

    def set_tasks(self, tasklist):
        with open(tasklist, "r") as taskfile:
            tasks = taskfile.read()[:-1].split("\n") # Cuts last newline
            for task in tasks:
                task_arr = task.split(", ")
                todo = task_arr[0]
                deadline = datetime.strptime(task_arr[1], "%d %B %Y")
                category = task_arr[3]
                duration = None
                if category == "essay":
                    if "pages" in task_arr[2]:
                        raise Exception("Check schedule.txt! Writing assignments are measured in words.")
                    duration = int(task_arr[2].split(" ")[0]) / WRITE_WORDS_PER_HOUR * 60
                elif category == "reading":
                    if "words" in task_arr[2]:
                        raise Exception("Check schedule.txt! Reading assignments are measured in pages.")
                    duration = int(task_arr[2].split(" ")[0]) / READ_PAGES_PER_HOUR * 60
                else: # Assume duration listed in minutes
                    duration = int(task_arr[2].split(" ")[0])

                priority = 1
                if len(task_arr) > 4:
                    priority = task_arr[4]

                new_task = Todo(category, duration, todo, deadline, priority)
                self.tasks.append(new_task)

    def set_timeslot(self, todo):
        if todo.get_category() == "lecture" or todo.get_category() == "discussion":
            self.fill_timeslot(todo, todo.starttime, todo.endtime)
        else:
            # Calculate necessary duration of activity for that day (based on total duration and days until deadline)
            days_to_deadline = todo.get_deadline() - now
            duration_per_day = todo.get_duration() / days_to_deadline
            slot = self.find_slot(duration_per_day)
            start = slot["start"]
            end = slot["end"]
            self.fill_timeslot(todo, start, end)

    def fill_timeslot(self, todo, start, end):
        inc = INCREMENT_SIZE
        time = start
        while time < end:
            slot = self.get_increment(time)
            time = start + timedelta(minutes=inc)
            inc += INCREMENT_SIZE
            if not slot.get_is_filled():
                slot.set_filled(todo)
            else:
                raise Exception(slot.time.time(), " is already filled!")
                break

    def get_increment(self, time):
        # Return increment at given time
        for inc in self.increments:
            if inc.time == time:
                return inc

        # If no increment for that time...
        return False


class Increment:

    def __init__(self, time, size=INCREMENT_SIZE):
        self.time = time
        self.is_filled = False
        self.size = size
        self.todo = None

    def __repr__(self):
        return "<Increment()>", self.time

    def __str__(self):
        return str(self.time.time()) + ": " + str(self.todo)

    def set_filled(self, todo):
        self.todo = todo
        self.is_filled = True

    def set_unfilled(self):
        self.is_filled = False

    def get_is_filled(self):
        return self.is_filled

    def __eq__(self, other):
        return self.time == other.time
