from socket import *
import json
import threading
import random

serverport = 12002


def handleClient(clientSocket, address):
    print("Adresse: ", addr)

    sentence = clientSocket.recv(2048).decode()
    json_data = json.loads(sentence)

    method = json_data.get("method")

    response = {"method": method}

    if method == "random":
        num1 = int(json_data.get("Num1", 0))
        num2 = int(json_data.get("Num2", 0))
        result = random.randint(num1, num2)
        response["num1"] = num1
        response["num2"] = num2
        response["result"] = result
    elif method == "add":
        num1 = int(json_data.get("Num1", 0))
        num2 = int(json_data.get("Num2", 0))
        result = num1 + num2
        response["num1"] = num1
        response["num2"] = num2
        response["result"] = result
    elif method == "subtract":
        num1 = int(json_data.get("Num1", 0))
        num2 = int(json_data.get("Num2", 0))
        result = num1 - num2
        response["num1"] = num1
        response["num2"] = num2
        response["result"] = result
    else:
        response = {"Unsupported method": method}

    response_json = json.dumps(response)
    clientSocket.send(response_json.encode())
    clientSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverport))
serverSocket.listen(1)
print("Server is ready to work for you")

while 1:
    csock, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(csock, addr)).start()
