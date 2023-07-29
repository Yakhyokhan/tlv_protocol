import socket, TLVProtocol as pr

json = pr.TLVData(pr.DataTypes.JSON, {"name":"Ahmad", "age": 19})
bson = pr.TLVData(pr.DataTypes.BSON, {"name":"Ahmad", "age": 19})
string = pr.TLVData(pr.DataTypes.STRING, '{"name": "Ahmad", "age": 19}')

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    pr.write(s, json)
    pr.write(s, bson)
    pr.write(s, string)

