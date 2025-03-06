import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))

    while True:
        print("\nMenu:")
        print("1. Echo Message")
        print("2. Perform Mathematical Operation")
        print("3. Get Date and Time")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            msg = input("Enter message to echo: ")
            client_socket.send(msg.encode())
            response = client_socket.recv(1024).decode()
            print("Server Response:", response)

        elif choice == "2":
            while True:
                print("\nOperations:")
                print("1: ADD")
                print("2: SUBTRACT")
                print("3: MULTIPLY")
                print("4: DIVISION")
                print("5: MODULUS")
                print("6: Go Back")

                operation = input("Enter operation: ")
                if operation == "6":
                    break  # Go back to the main menu
                
                num1 = input("Enter first number: ")
                num2 = input("Enter second number: ")
                client_socket.send(f"MATH:{operation}:{num1}:{num2}".encode())

                response = client_socket.recv(1024).decode()
                print("Server Response:", response)

        elif choice == "3":
            client_socket.send("DAYTIME".encode())
            response = client_socket.recv(1024).decode()
            print("Server Response:", response)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

    client_socket.close()

if __name__ == "__main__":
    main()
