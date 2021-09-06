import socket
import sys

class colors:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE = '\33[94m'

def client():
    '''
    Create TCP/IP socket
    Connect to host on specified port
    Send messages to the server.
    '''
    if len(sys.argv) != 3:
        print("\tUsage: python3 echo_client.py [hostname] [port]")
        return 0
        
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = (sys.argv[1], int(sys.argv[2]))

    print(colors.GREEN + "[!]Connecting to %s on port %s" + colors.STOP, server_addr)
    sock.connect(server_addr)

    try:
        while True:
            message = input("$> ")
            if message == "exit()":
                raise Exception
            print(colors.GREEN + "[!]Sending Message..." + colors.STOP)
            sock.sendall(message.encode())

            amount_expected = len(message)
            amount_recieved = 0

            while amount_expected > amount_recieved:
                data = sock.recv(1024)
                amount_recieved += len(data)
                print(colors.BLUE + "[+]Message From Server: ", data.decode() + colors.STOP)
    except Exception as ex:
        print(colors.RED + "[!]Closing Connection with server" + colors.STOP)
    finally:
        print(colors.GREEN + "[+]Socket Closed" + colors.STOP)
        sock.close()

if __name__ == '__main__':
    client()
