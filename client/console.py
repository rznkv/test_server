from client.client import APIClient
from shared.models import MathRequest

print("Test Server Console")
print("V1.0 - Local server")


def main():
    client = APIClient()

    while True:
        command = input("Command:")
        if command == "exit":
            break
        elif command == "root":
            print(client.get_root())
        elif command == "client":
            print(client.client_check())
        elif command == "square":
            input_number = int(input("Input number:"))
            print(client.number_square(input_number))


def console_test():
    client = APIClient()


    while True:
        print(client.get_root())
        print(client.client_check())
        print(client.number_square(2))
        print(client.calculate(MathRequest(digits = [4, 2], action ='+')))
        print(client.calculate(MathRequest(digits = [100, 150], action ='-')))
        break


if __name__ == "__main__":
    # main()
    console_test()
