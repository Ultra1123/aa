import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("127.0.0.1", 6060))

message = clientSocket.recv(256).decode ("utf-8")
firstNumber = input(message)
clientSocket.send(bytes(firstNumber, "utf-8"))

message = clientSocket.recv(256).decode("utf-8")
secondNumber = input(message)
clientSocket.send(bytes(secondNumber, "utf-8"))

result = clientSocket.recv(256).decode("utf-8")
print("Result is: ", result)