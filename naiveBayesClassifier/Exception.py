class Notseen(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Token '{}' is never seen in the training set.".format(self.value)