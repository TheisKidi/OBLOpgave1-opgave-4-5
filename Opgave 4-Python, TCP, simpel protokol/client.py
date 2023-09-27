from socket import *

serverName = "localhost"
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

function = input("Indtast funktion (Random, Add eller Subtract): ")
tal1 = int(input("Indtast tal1: "))
tal2 = int(input("Indtast tal2: "))

kommando = f"{function} {tal1} {tal2}"

clientSocket.send(kommando.encode())

response = clientSocket.recv(2048).decode()
print("Svar fra serveren:", response)

clientSocket.close()
