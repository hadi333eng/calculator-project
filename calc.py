import math
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        raise ValueError("Can't divide by 0")
    return x / y
def square_root(x):
    if x < 0:
        raise ValueError("Cannot square root negative number")
    return math.sqrt(x)

def main():
    while True:
        print("Select an operation:")
        print()
        print("1.Add")
        print()
        print("2.Subtract")
        print()
        print("3.Multiply")
        print()
        print("4.Divide")
        print()
        print("5.Square Root")
        print()
        print("6. Exit")
        print()
        choice = input("Pick one (1,2,3,4,5,6): ")
        print()

        if choice in ['1', '2', '3', '4']:
            try:
                print()
                n1 = float(input("Enter first number: "))
                print()
                n2 = float(input("Enter second number: "))
                print()
                if choice == '1':
                    print(f"Result: {add(n1, n2)}")
                    print()
                elif choice == '2':
                    print(f"Result: {subtract(n1, n2)}")
                    print()
                elif choice == '3':
                    print(f"Result: {multiply(n1, n2)}")
                    print()
                elif choice == '4':     
                    print(f"Result: {divide(n1, n2)}")
                    print()
            except ValueError:
                print("Invalid input: ")
                print()
                continue

        elif choice == '5':
            try:
                print()
                n1 = float(input("Enter number: "))
                print()
            except ValueError:
                print("Invalid input: ")
                print()
                continue
            print(f"Result: {square_root(n1)} ")
            print()

        elif choice == '6':
            print("Bye")
            print()
            break

main()

