from random import randint
from time import sleep, asctime

# Create the decorator with default parameters and an optional max_delay parameter
def backoff(initial_delay: float = 0.01, backoff_factor: float = 2.0, max_delay: float = None) -> callable:

    # Create the callable decorate function
    def decorate(func: callable) -> callable:

        # Initialize delay
        delay = initial_delay

        # Create the inner function that will be called by the decorated function
        # (For some reason this only works if I seperate the inner function from the decorate function)
        # (I have no idea why as I coded this at like 2 AM last night off of 3 red bulls and now I'm trying to
        # decipher my mad ramblings - easy comment for whoever reads this can you tell me how this could be simpler?)

        def inner(*args, **kwargs):

            nonlocal delay

            while True:
                # Print the current time, name of function, and delay used
                print(f"{asctime()}: will be calling {func.__name__} after {delay:.2f} sec delay")

                # Call the shaky function
                result = func(*args, **kwargs)
                print(result)

                # If the shaky function returns true, reset delay and return the result
                if (result != False) and (result != None):
                    delay = 0
                    return result

                # If the delay is 0, set it to the initial delay
                if delay == 0:
                    delay = initial_delay
                # Ensure the delay does not exceed the maximum delay
                elif delay >= max_delay or (delay * backoff_factor) > max_delay:
                    delay = max_delay
                # Otherwise, multiply delay by backoff factor
                else:
                    delay *= backoff_factor

                sleep(delay)

        return inner
    return decorate

# Create the shaky function with my own decorated parameters
@backoff(initial_delay=0.05, backoff_factor=1.25, max_delay=10)
def call_shaky_service():
    return 6 == randint(1, 6)

while True:
    print(call_shaky_service())