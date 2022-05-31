import sys
sys.path.append('../entity')
from LoginEntity import LoginRequest

def exceptionHandler(exc_type, exc_value, exc_traceback):
    # if issubclass(exc_type, KeyboardInterrupt):
    print("catch exception")
        # sys.__excepthook__(exc_type, exc_value, exc_traceback)
        # return

sys.excepthook = exceptionHandler

d = {"username": "123"}

a = LoginRequest(d)
print(a.username)
print(a.password)