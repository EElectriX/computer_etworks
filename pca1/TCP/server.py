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

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} established.")
        
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            print(f"Received: {data}")
            
            if data == "DAYTIME":
                response = f"{get_greeting()}, the current date and time is: {datetime.datetime.now()}"
            elif data.startswith("MATH:"):
                _, operation, num1, num2 = data.split(":")
                response = str(perform_operation(operation, num1, num2))
            else:
                response = f"Echo: {data}"
            
            client_socket.send(response.encode())
            print(f"Sent: {response}")
        
        client_socket.close()
        print("Client disconnected.")

if __name__ == "__main__":
    start_server()
