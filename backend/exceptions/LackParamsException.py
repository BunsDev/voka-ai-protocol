class LackParamsException(Exception):
    # init exception
    def __init__(self, value):
        self.value = value
    
    # explain message for exceptions
    def __str__(self):
        return "lack params exception: {}".format(repr(self.value))