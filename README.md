# DoomChatApp

**DoomChatApp** is a terminal-based chat application developed using **Python**. It enables real-time text communication over the Internet using **Ngrok TCP tunnels**. The app is lightweight, installation-free, and designed to work easily across laptops.

---

## 💡 Features

- ✅ Real-time one-on-one and group messaging
- ✅ Internet-based communication using Ngrok
- ✅ Cross-platform (tested on macOS and Windows)
- ✅ Fully portable (no installation required)
- ✅ Terminal interface using Python

---

## 🛠️ Technologies Used

- **Language**: Python
- **Networking**: Ngrok TCP tunnels
- **Interface**: Terminal (CLI-based)
- **Platform**: macOS / Windows 10/11
- **Version Control**: Git & GitHub

---

## 🚀 How to Run

### 📦 Prerequisites

- Python 3 installed (use `python3`)
- [Ngrok](https://ngrok.com/) account and Ngrok CLI installed

---

### 💻 Run Instructions

Open **3 terminal windows** and follow the steps below:

#### 🖥️ 1. Start the server


python3 server.py

#### 💬 2. Start the client
# Run client (in a new terminal)
python3 client.py

🌐 3. Start Ngrok TCP tunnel
ngrok tcp 12345
You will get an output like:


Forwarding tcp://0.tcp.ngrok.io:13537 -> localhost:12345
🔗 Share this forwarding address (e.g., 0.tcp.ngrok.io and port 13537) with the user on the other laptop.

🧑‍💻 On the client laptop
When prompted, enter the Ngrok TCP address and port shared by the server owner.
