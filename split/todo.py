class Todo:

    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def __str__(self):
        return "<Todo: " + self.description + ">"

    def __repr__(self):
        return __str__(self)
