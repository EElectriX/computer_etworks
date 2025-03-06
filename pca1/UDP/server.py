import socket
import datetime

def get_greeting():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

def perform_operation(operation, num1, num2):
    try:
        num1, num2 = float(num1), float(num2)
        if operation == "1":
            return num1 + num2
        elif operation == "2":
            return num1 - num2
        elif operation == "3":
            return num1 * num2
        elif operation == "4":
            return num1 / num2 if num2 != 0 else "Error: Division by zero"
        elif operation == "5":
            return num1 % num2 if num2 != 0 else "Error: Modulus by zero"
        else:
            return "Invalid Operation"
    except ValueError:
        return "Invalid Numbers"

def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("0.0.0.0", 12345))
    print("UDP Server is listening on port 12345...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Received from {client_address}: {message}")

        if message == "DAYTIME":
            response = f"{get_greeting()}, the current date and time is: {datetime.datetime.now()}"
        elif message.startswith("MATH:"):
            _, operation, num1, num2 = message.split(":")
            response = str(perform_operation(operation, num1, num2))
        else:
            response = f"Echo: {message}"

        server_socket.sendto(response.encode(), client_address)
        print(f"Sent to {client_address}: {response}")

if __name__ == "__main__":
    start_udp_server()
