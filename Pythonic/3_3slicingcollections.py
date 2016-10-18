from Slicesupport import session_factory, Measurement

def main():

    nums = fibonacci(200)
    print("All nums")
    print(nums)

    print("First 5 nums")
    first_five = nums[:5]
    print(first_five)

    print("2->7 nums")
    print(nums[2:8])

    print("last 3 nums (pythonic)")
    print(nums[-3:])

    print("Top measurements from the database")
    session = session_factory()
    query = session.query(Measurement).filter(Measurement.value > .9).order_by(Measurement.value.desc()).all()

    print(query)

def fibonacci(limit):
    numbers = []
    current, nxt = 0, 1

    while current < limit:
        current,nxt = nxt, nxt + current
        numbers.append(current)
    return numbers


main()