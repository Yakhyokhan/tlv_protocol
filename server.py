import socket, TLVProtocol


HOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"connected by {addr}")
        data = TLVProtocol.read(conn)
        print(data)
        data = TLVProtocol.read(conn)
        print(data)
        data = TLVProtocol.read(conn)
        print(data)