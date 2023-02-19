# P2P chat server
This project is a component in a larger project, a peer-to-peer chat application. 
As it's a peer-to-peer application, there is no server needed for chatting. 
This server handles "registering" clients, so that the actual [application](https://github.com/JefvdA/p2p-chat-terminal-client) is able to retrieve a list of all clients, 
and their ips to chat with.

## Installation
If you want to run this application yourself, here are some easy steps to follow.

### Local python installation
Setup a virtual python environment <br>
`python -m venv venv`

Activate the virtual python environment <br>
Unix: `source ./venv/bin/activate` <br>
Windows: `./venv/Scripts/activate`

Now you can run the project locally with following make command: <br>
`make run-dev`

### Docker
Coming soon, see following [issue](https://github.com/JefvdA/p2p-chat-server/issues/6)

## Features
As this chat application works peer-to-peer, there's no need for a server that handles the chatting. 
This server is basically a client contact list, so people can just share their usernames, and their ips can be fetched from this server. <br>
That's why only these features are needed:
- **Register**: A client should be able to register themselves in the client list. A username, password and a host-ip are required.
  - POST : /register
- **Fetch client list**: A client should be able to fetch a list of all clients 
  - GET : /
- **Fetch one client**: A client should be able to fetch information about a single client by their username
  - GET : /client/<username>
- **Unregister**: A client should be able to remove themselves from the client list. Their password is required for safety.
  - DELETE : /client/<username>

## Testing
At the moment, there are no tests for this project. If you think there should be, create an issue for this.

## Contributions
Contributions are always welcome, check for any open [issues](https://github.com/JefvdA/p2p-chat-server/issues), or create one if you have any ideas / comments.
