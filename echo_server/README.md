## Echo Server in Python

The following client/server applications implement the simple echo server
using python.

### Description:
  The server starts on the provided host and port and waits for TCP connections
  to connect. Once the client specifies the server name and port, it connects 
  to the server and the client can now send messags to the server which are 
  echoed back.
  Coloring of text has been done for ease of reading the text sent to the server
  and by the server.

### Requirements:
  The server and the client both require the `socket` library along with `sys` library
  in order to function properly.

### Usage:
  Clone the repository using the following commands and move to the directory.
  ```bash
  $ git clone https://github.com/samsepi0x0/TCP-IP-Codes.git
  $ cd TCP-IP-Codes/echo_server
  ```
  Run the server on one terminal and client on another one(for testing).
  ```bash
  $ python3 echo_server.py [hostname] [port]
  ```
  on another terminal:
  ```bash
  $ python3 echo_client.py [hostname] [port]
  ```
  
### Output:
  Client sending messages to server.
  ![ScreenShot of client](https://raw.githubusercontent.com/samsepi0x0/TCP-IP-Codes/main/echo_server/client.png)
  
  Server response to the messages.
  ![ScreenShot of server](https://raw.githubusercontent.com/samsepi0x0/TCP-IP-Codes/main/echo_server/server.png)
