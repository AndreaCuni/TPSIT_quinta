import socket

ipServer='127.0.0.1'
porta = 5000

def main ():
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipServer, porta))
    body = "username=Cuniberti_Andrea&password=mi_piacciono_le_auto"
    msg = f"POST http://127.0.0.1:5000/index/ HTTP/1.1\n" \
          f"Host: http://127.0.0.1:5000/index.html/ \n" \
          f"Content-Length: {len(body)}\n" \
          f"Content-Type: application/x-www-form-urlencoded\n" \
          f"\n" \
          f"{body}"
    print(msg)
    client.sendall(msg.encode())
    data = (client.recv(4096)).decode()
    print(data)


if __name__ == '__main__':
    main()