def main():
    a = int(input("Enter a number for a: ")) # e.g. a = 1
    b = int(input("Enter a number for b: ")) # e.g. b = 2

    print(f"Before swap: a = {a}, and b = {b}")
    print("Let's swap a to b:")

    print(swap(a, b))


def swap(a, b):
    temp = a # e.g. temp = a --> temp = 1
    a = b # e.g. a = b --> a = 2 ('a' is overwritten)
    b = temp # e.g. b = temp --> b = 1 ('b' is overwritten by te 'temp' var, assigned with a's value)
    return f"After swap: a = {a}, and b = {b}"

if __name__ == "__main__":
    main()