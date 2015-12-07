from datetime import datetime
from schedule import Schedule, Increment

DAY_BEGIN = "8:00"
DAY_END = "18:00"

# Print schedule object nicely
def print_schedule(schedule):
    tmp = None
    day_fmt = "%A, %B %d, %Y"
    print "\nAgenda for " + str(datetime.strftime(datetime.today(), day_fmt))
    print "------------------------------------"
    for increment in schedule.increments:
        if increment.todo != tmp:
            timestring = format_hour(increment.time.time())
            try:
                print timestring + ":\t", increment.todo.task
            except: # It's a Nonetype object (no task), so you're free
                print "Free"
        tmp = increment.todo
    print "\n"


def format_hour(time):
    time_string = str(time)[:-3]
    hour = int(time_string[:2])
    if hour > 12:
        hour %= 12
    new_time = str(hour) + ":" + time_string[3:]
    return new_time


if __name__ == "__main__":
    fmt = "%H:%M"
    start = datetime.strptime(DAY_BEGIN, fmt)
    end = datetime.strptime(DAY_END, fmt)
    schedule = Schedule(start, end)
    print_schedule(schedule)
