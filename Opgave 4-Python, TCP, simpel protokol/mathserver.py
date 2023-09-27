from socket import *
from threading import *
import random
import json

serverPort = 12001
serverRunning = True


def handleClient(clientSocket, addr):
    sentence = clientSocket.recv(2048).decode()
    splittetText = sentence.split()
    Text = ""
    if splittetText[0].lower() == "random":
        talx = int(splittetText[1])
        taly = int(splittetText[2])
        random_num = random.randint(talx, taly)
        Text = f"Random number between {talx} & {taly} = {random_num}"
    elif splittetText[0].lower() == "add":
        talx = int(splittetText[1])
        taly = int(splittetText[2])
        Text = f"Summen af de 2 tal {talx} + {taly} = {(talx+taly)}"
    elif splittetText[0].lower() == "subtract":
        talx = int(splittetText[1])
        taly = int(splittetText[2])
        Text = f"{talx} - {taly} = {(talx-taly)}"
    else:
        Text = f"understøtter ikke metoden {splittetText[0]}"

    clientSocket.send(Text.encode())
    clientSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The server is up and running on port", serverPort)

while 1:
    connectionSocket, addr = serverSocket.accept()
    print("Connected from", addr)
    Thread(target=handleClient, args=(connectionSocket, addr)).start()
