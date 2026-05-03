# school_chat — Real-Time Chat Application

A real-time chat application built in Python for school use. Students and teachers communicate instantly through chat rooms organized by class or subject, using TCP socket programming.

## Tech Stack

| Technology | Usage |
|---|---|
| Python 3 | Main language |
| socket | TCP/IP networking |
| threading | Handle multiple clients |
| Flask / tkinter | Interface (web or desktop) |
| JSON | Message formatting |

## Architecture

```
┌──────────┐         ┌──────────────────┐         ┌──────────┐
│ Client A │ ──────→ │  Python Server   │ ──────→ │ Client B │
│          │ ←────── │  - Routing       │ ←────── │          │
└──────────┘         │  - Rooms         │         └──────────┘
                     │  - History       │
                     └──────────────────┘
```

## Features

- Real-time messaging with TCP sockets
- Multiple simultaneous users via threading
- Separate chat rooms (by class/subject)
- Username system and message history
- Simple and lightweight

## Project Structure

```
school_chat/
├── server.py         # TCP server — handles all connections
├── client.py         # Client — connects and sends messages
├── protocol.py       # Message format (JSON)
├── rooms.py          # Chat room management
├── requirements.txt
└── README.md
```

## Getting Started

**Prerequisites:** Python 3.8+, both machines on the same network (or localhost)

```bash
git clone https://github.com/cyberhacker1210/school_chat
cd school_chat
pip install -r requirements.txt
```

```bash
# Terminal 1 — Start server
python server.py

# Terminal 2 — Connect as client
python client.py
# Enter your username: Alice
# Enter room name: maths-class
```

### Example session

```
[maths-class] Alice: Vous avez compris l'exercice 3?
[maths-class] Bob: Oui je peux t'expliquer!
[maths-class] Alice: Super merci!
```

### Server configuration

```python
HOST = "0.0.0.0"   # Listen on all interfaces
PORT = 5555
MAX_CLIENTS = 50
```

## Author

**cyberhacker1210** — [GitHub](https://github.com/cyberhacker1210)
