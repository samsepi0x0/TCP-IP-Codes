import socket
import sys

class colors:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE = '\33[94m'

def server():
    '''
    Create a TCP/IP socket
    Bind Socket to port
    Listen for incoming connections
    Print out incoming connections and data
    Choose which messages to echo
    '''
    if len(sys.argv) != 3:
        print("\tUsage: python3 echo_server.py [hostname] [port]")
        return 0

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = (sys.argv[1], int(sys.argv[2]))

    print(colors.GREEN + "[+]Initiating %s on port %s" % server_addr + colors.STOP)

    sock.bind(server_addr)
    sock.listen(5)
    
    while True:
        print(colors.BLUE + "[!]Waiting for connection..." + colors.BLUE)
        connection, client_addr = sock.accept()

        try:
            print(colors.GREEN + "[+]Incoming connection from : " + colors.STOP, client_addr)
            
            # recieve small chunks of data and retransmit it if server wants
            while True:
                data = connection.recv(1024)
                print("[+]Data : ", data.decode())
                if data:
                    connection.sendall(data)
                else:
                    print(colors.RED + "[!]No data from client : ", client_addr + colors.STOP)
                    break
        except Exception as ex:
            print(colors.RED + "[-]Error Occured!" + colors.STOP)
        finally:
            print(colors.GREEN + "[!]Closing Connection." + colors.STOP)
            connection.close()

if __name__ == '__main__':
    server()
