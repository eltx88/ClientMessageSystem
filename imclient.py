"""

To run imclient.py, first start the server with the command python3 imserver.py localhost 8090 in one terminal
On another terminal type python3 imclient.py localhost 8090 to connect to server and chat with other connected clients

This sets up the server and client to chat with one other.Multiple clients can be run at the same time to chat with one another

Upon starting, user will be kept on being prompted to type a username in order to use chatroom functions. User can do so by typing /setname Bob for example.

Once user has entered name, able to use all functions and can be aware of what cmds there are by typing /cmd.
This returns a set of commands that can be used in any order.
"""
import sys
from ex2utils import Client

class IRCClient(Client):
    flag = True
    def onMessage(self, socket, message):
        print(message)
        if message == "You have left the chat" or message == "Server has been closed by host":
            socket.close()
            self.stop()
            self.flag = False
            exit(0)
        return True

# Parse the IP address and port you wish to connect to.
ip = sys.argv[1]
port = int(sys.argv[2])

# Create an IRC client.
client = IRCClient()

# Start the client.
client.start(ip, port)

while client.flag:
    message = input()
    client.send(message.encode())
