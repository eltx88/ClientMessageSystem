import sys
from ex2utils import Server

class myServer(Server):
    count = 0
    users = []
    clients = {}
    
    def onStart(self):
        print("Echo server has started")

    def onStop(self):
        print("Stopping server")
        
    def onMessage(self, socket, message):
        mlist = [x.strip() for x in message.split(" ")]

        if(socket.nameSet == False and mlist[0]!="/setname" and mlist[0]!="/quit"):
            socket.send("please enter user name to use chat room".encode())

        elif mlist[0] == "/setname":
            if len(mlist) < 2:
                socket.send("please enter a username </setname> <username> ".encode())
            else:
                if(mlist[1] in myServer.users):
                    socket.send("please re-enter a username, username entered taken".encode())
                else:
                    socket.send("Username accepted, type /cmd to see available commands".encode())
                    socket.username = mlist[1]
                    myServer.clients[socket] = socket.username
                    myServer.users.append(mlist[1])
                    socket.nameSet = True

        elif mlist[0] == "/allusers":
            socket.send("Users in chat:".encode())
            for user in myServer.clients:
                socket.send(user.username.encode())

        elif mlist[0] == "/private" and socket.nameSet:
            if len(mlist) < 3:
                socket.send("please enter valid format </private> <username> <message>".encode())
            else:
                if(mlist[1] not in myServer.users):
                    socket.send("User not found".encode())
                else:
                    for socketX,username in myServer.clients.items():
                        if username == mlist[1]:
                            sentence = " ".join(mlist[2:])
                            msg = str(socket.username) + "(private): " + sentence
                            socketX.send(msg.encode())
       
        elif(mlist[0] == "/all" and socket.nameSet):
            if len(mlist) < 2:
                socket.send("please enter valid format </all> <message>".encode())
            else:
                for socketX,username in myServer.clients.items():
                    if socket != socketX:
                        sentence = " ".join(mlist[1:])
                        msg = str(socket.username) +": "+ sentence
                        socketX.send(msg.encode())

       
        elif mlist[0] == "/quit":
            socket.send("You have left the chat".encode())

        elif mlist[0] == "/cmd":
            socket.send("Commands: /private , /all, /allusers, /quit".encode())

        return True

    def onConnect(self, socket):
        socket.nameSet = False
        print("User joined")
        self.count += 1
        print("Active users: " + str(self.count))
        message = "Please enter username below by typing eg. /setname Bob to use chatroom"
        socket.send(message.encode())

        
        return True


    def onDisconnect(self, socket):
        self.count -= 1
        if(socket.nameSet):
            print(f"{socket.username} has disconnected")
            myServer.users.remove(socket.username)
            del myServer.clients[socket]
            print("Active users: " + str(self.count))
            socket.send("Server has been closed by host".encode())
        else:
            print("Unregistered User left")
            print("Active users: " + str(self.count))
            socket.send("Server has been closed by host".encode())
        socket.close()
           
# Parse the IP address and port you wish to listen on.
ip = sys.argv[1]
port = int(sys.argv[2])

# Create an echo server.
server = myServer()

server.start(ip, port)
