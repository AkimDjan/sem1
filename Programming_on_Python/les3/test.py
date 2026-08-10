''' from typing import Callable
#stackOverflow - ошибки гуглить

def make_counter() -> Callable[[],int]:
    counter = 0
    def count() -> int:
        nonlocal counter
        counter +=1
        return counter
    return count

counter1=make_counter()
counter2=make_counter()

for i in range(3):
    counter1()
for i in range(22):
    counter2()
print(f'counter1: {counter1()};')
print(f'counter2: {counter2()};')
'''
