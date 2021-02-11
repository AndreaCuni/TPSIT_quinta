import socket

def actor(): 
    server_ip = "192.168.0.122"
    server_port = 7000
    receiver_ip = "192.168.0.129"
    receiver_port = 7000

    srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    srv.bind((server_ip,server_port))

    while True: 

        data, address = srv.recvfrom(4096)
        print(f"msg from client: {data.decode()}, from {address}")

        cli.sendto(data,(receiver_ip,receiver_port))
        print(f"message sent: {data}, to {receiver_ip}")
    
    srv.close()
    cli.close()
    

if __name__ == '__main__':
    actor()
    