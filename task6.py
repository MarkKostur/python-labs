import datetime 
info_about_func = []

def get_log():
    for obj in info_about_func:
        yield obj.__str__()

class FileMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class File(metaclass=FileMeta):
    def __init__(self, file_name):
        self.file_name = file_name
    
    def write_in_file(self, log):
        with open(self.file_name, 'a') as file:
            file.write(f'{log}\n')

    def delete_content(self):
        with open(self.file_name, "w") as f:
            f.truncate(0) 

immediately_invoked_function = (lambda: File('./lab6/logs.txt').delete_content())()

class Information:
    def __init__(self, args, return_value, func_name, time_call, error='no errors'):
        self.args = args
        self.return_value = return_value
        self.func_name = func_name
        self.time_call = time_call
        self.error = error
    
    def __str__(self):
        keys_func = self.__dict__.keys()
        list_keys = list(keys_func)
        str_info_func = f"{list_keys[2]} {self.func_name}, {list_keys[0]}, {self.args}, {list_keys[1]}, {self.return_value}, {list_keys[3]}, {self.time_call}, {list_keys[4]} {self.error}"
        print(str_info_func)
        file = File('./lab6/logs.txt')
        file.write_in_file(str_info_func)

def logger(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        func_name = func.__name__
        time_call = datetime.datetime.now().strftime("%H:%M:%S")
        error_msg = None
        if len(args) < 2: error_msg = f'Not having arguments in {func_name} function'
        info_about_func.append(Information(args, return_value, func_name, time_call, error_msg))
    return wrapper

@logger
def multiply(first_num=10, second_num=10, *args):
    if len(args) < 2: return 'This function doens`nt have arguments'
    return first_num * second_num

multiply(10, 2)
multiply(3, 4)
multiply()

res = get_log()

for run_info in info_about_func:
    print(next(res))