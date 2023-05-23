import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 6060))
serverSocket.listen()

clientSocket, addr =serverSocket.accept()
clientSocket.send(b"Enter first number: ")
firstNumber = clientSocket.recv(32).decore("utf-8")
firstNumber = int(firstNumber)

clientSocket.send(b"Enter second number: ")
secondNumber = clientSocket.recv(32).decore("utf-8")
secondNumber = int(secondNumber)

result = format(firstNumber + secondNumber)

clientSocket.send(bytes(result, "utf-8"))
