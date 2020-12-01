import socket

def actor(): 
    server_ip = "192.168.88.96"
    server_port = 7000
    receiver_ip = "192.168.88.107"
    receiver_port = 7000

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    srv.bind((server_ip,server_port))
    

    while True: 
        
        srv.listen()

        connection, address = srv.accept()
        data = connection.recv(4096)
        print(f"msg from client: {data.decode()}, from {address}")


        cli.connect((receiver_ip,receiver_port))
        cli.sendall(data)
        print(f"message sent: {data}, to {receiver_ip}")
    
    srv.close()
    cli.close()

if __name__ == '__main__':
    actor()
        

