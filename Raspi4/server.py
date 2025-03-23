import socket
from time import sleep
import pandas as pd




HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 4000  # Port to listen on

cars_number = 10

# Un tableau de tableaux, chaque tableau correspond à une voiture, avec ses données à l'intérieur de celui ci
Data = [[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[]]]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        # MA VERSION 
        # while True:
        #     data = conn.recv(50)
        #     if not data:
        #         break
        #     print(f"Received data: {data.decode()}")
        #     response = "ACK\n"
        #     conn.sendall(response.encode())

        # VERSION AVEC NOUVEAU FORMAT POUR TRAITEMENT DONNEES
        while True:
            data = conn.recv(1024).decode()
            if data:
                parts = data.strip().split(',')
                if len(parts) == 3:
                    ID_Voiture, Time, Capteur = map(int, parts)
                    print(ID_Voiture, Time, Capteur)
                    response = "ACK\n"
                    conn.sendall(response.encode())

                    # On traite les données ensuite
                    Data[ID_Voiture-1][0].append(Time)
                    Data[ID_Voiture-1][1].append(Capteur)
                    print(Data)
                    # Création du DataFrame
                    df = pd.DataFrame(Data, columns=["Temps", "Capteur"])
                    print(df)
            else:
                break