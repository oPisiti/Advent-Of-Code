
def timeMe(func):
    import time
    
    def wrapper(*args, **kwargs):
        init = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Δt = {(end - init):.6f} s")

    return wrapper

@timeMe
def hello():
    print("Hello")

# hello = timeMe(hello)
# hello <- wrapper
# hello/wrapper gets called
# If the original hello has arguments, but wrapper doesn't, an error is raised

if __name__ == '__main__':
    hello()