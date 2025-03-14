import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 4000     # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(100)
            if not data:
                break
            print(f"Received data: {data.decode()}")
            response = "ACK\n"
            conn.sendall(response.encode())
