from socket import *
import json

serverport = 12002
servername = "localhost"

csock = socket(AF_INET, SOCK_STREAM)
csock.connect((servername, serverport))

method = input("Wich method (random, add or subtract): ")
num1 = input("First number: ")
num2 = input("Second number: ")

json_data = {"method": method, "Num1": num1, "Num2": num2}
json_string = json.dumps(json_data)

csock.send(json_string.encode())

dataBack = csock.recv(2048)
sentenceBack = dataBack.decode()

print("Modtaget Json:", sentenceBack)
csock.close()
