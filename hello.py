# ask use for their name
"""
name = input("what's your name?").strip().title()
first, last = name.split(" ")
print(f"hello, {first} ")
"""


def main():
    name = input("What is your name? ")
    hello(name)



def hello(to="world"):
    print("Hello,",to)

main()
