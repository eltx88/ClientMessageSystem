# ClientMessageSystem
Python application which allows multiple clients to join and send messages over a hosted server

The server implements an echo server which allows a client to setup a username, see other clients, send a message to the chatroom and a private one. Commands in server are /setname, /quit, /private, /all , /allusers and /cmd which will be explained below.
Server flow

The server will recognise that user has joined by printing “User has joined” and the current active user count in the terminal. When the server is started, it first checks if the user has set up their username. If not, the server will continuously prompt the user to do so by calling the /setname command. This command takes in one parameter which is the user’s desired name itself e.g /setname john. At this point, the user has an option to do /quit as well if they are no longer interested to join the server. Command /quit will allow the user to exit the server.

If the user sends the /setname command followed by a username, the code checks if the username is already taken. If the username is available, the server accepts the username and adds the user to the list of clients.
After a successful attempt of setting up the username, the server will acknowledge this by sending a message to the user informing that the chat functions can now be used. The user will be suggested to use the command /cmd first.
The /cmd command provides a quick and easy way for users to see all the available commands.
The /allusers command is used to display the usernames of all clients currently in the chat room.
The /private command allows users to send private messages to other users in the chat room. The command is followed by the username of the recipient and the message to be sent. e.g. /private john hi how r u
The /all command is used to send a message to all users in the chat room. The command is followed by the message to be sent. e.g. /all hello everyone
If the user decides to exit the chatroom, the command /quit can be typed. This will close the connection between the user and the server. This command only works when typed in terminal running the implemented imclient.py file as a confirmation message will be sent to the client which will then respond by shutting down the client.
When running server with telnet, in order to exit the chatroom the telnet command quit needs to be used instead. When a user has disconnected, the server will display that a user has left and the current active user count.
