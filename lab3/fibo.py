import timeit, os
from functools import lru_cache 

def save_on_disk(extension):
    def decorator(func):
        def wrapper(*args, **kwargs):
            path = "fibo."+extension
            '''
            if(os.path.isfile(path)):
                print("readed from: "+str(path))
                file = open(path, "r")
                result = file.readlines()
                print(result)
                raise Exception("file exist")
            else:'''
            result = func(*args, **kwargs)
            file = open(path, "w")
            #print("opened")
            file.write(str(result))
            #print("saved: ", kwargs['extension'])
            file.close()
            return result
        return wrapper
    return decorator

@save_on_disk("excel")
@lru_cache(maxsize = 100)
def fibo(no_elements):
    if(no_elements <=1):
        return 1
    else:
        return fibo(no_elements-2)+fibo(no_elements-1)

start = timeit.default_timer()
try:
    print(fibo(20))
except Exception:
    print("file exist")
print("time: "+str(timeit.default_timer() - start))
