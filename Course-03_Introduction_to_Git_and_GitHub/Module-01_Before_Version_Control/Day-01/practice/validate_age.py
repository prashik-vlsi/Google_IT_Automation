def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    assert isinstance(age, int), "Age must be an integer"
    return True

try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Valid age:", age)
except ValueError as error:
    print("Error:", error)
