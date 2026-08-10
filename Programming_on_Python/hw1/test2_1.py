from cache import lru_cache


@lru_cache(capacity=2)
def get_greeting(name: str) -> str:
    greeting = f"Hello, {name}!"
    print(f"call func for name: {name}")

    return greeting


print(get_greeting("Mr.White"))
print(get_greeting("Mike"))
print(get_greeting("Mr.White"))
print(get_greeting("Saul Goodman"))
print(get_greeting("Mr.White"))
print(get_greeting("Mike"))