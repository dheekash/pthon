def dec_fun(func):
    def wrapper_fun():
        print("Wrapper worked")
        return func()
    print("decoratoer function worked")
    return wrapper_fun()
def show():
    print("Show worked")

print(dec_fun(show))
