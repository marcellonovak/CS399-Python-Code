def my_deco(func: callable) -> callable:
    def inner():
        print("before")
        func()
        print("after")

    return inner

@my_deco
def foo():
    print("during")

foo()

# Caching Strategies
# FIFO: Evicts the oldest entries - newer entries are most likely to be reused
# LIFO: Evicts the latest entries - older entries are most likely to be reused
# LRU: Evicts the least recently used entries - recent entries are most likely to be reused
# MRU: Evicts the most recently used entries - least recently used entries are most likely to be reused
# LFU Evicts the least frequently used entries - entries with a lot of hits are more likely to be reused


from time import process_time as time
from functools import lru_cache

@lru_cache(maxsize=128)
def fibo(n: int) -> int:
    return n if n < 2 else fibo(n-1) + fibo(n-2)

t0 = time()
result = fibo(100)
dt = time() - t0

print(f'{dt:0.8f}s fibo(100) -> {result}')


