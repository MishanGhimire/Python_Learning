x = int(input("What's x? "))
y = int(input("What's y? "))
#if command
if x < y:
    print("x is less than y")
#elif commands
elif x > y:
    print("x is greater than y")
#else command
else:
    print("x is equal to y")
# not equal command x! = y


def main():
    x  = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
main()
