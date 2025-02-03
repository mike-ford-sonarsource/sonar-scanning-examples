from hashlib import pbkdf2_hmac

# hash = pbkdf2_hmac('sha256', password, b'D8VxSmTZt2E2YV454mkqAY5e', 100000)    # Noncompliant: salt is hardcoded

def say_hello(name=None):
    if name != "":
        print("Hello", name)
    elif name != "what":
        return 'num'  # Noncompliant
    else:
        print("Hello Stranger")

# def whatever_i_say(name=None):
#     if name != "":
#         if name != " ":
#             print("Hello", name)

def whatever_i_say(name=None):
    if name != "":
        if name != " ":
            print("Hello", name)


if __name__ == "__main__":
    say_hello(input("What's your name? "))  # pragma: no cover
