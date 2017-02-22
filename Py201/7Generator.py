# generator = coroutine
# call a function and yield a series of values
# generator requires yield

def generator():
    yield " This "
    yield " yields"
    yield " a lot"

gen = generator()
for item in gen:
    print(item)

