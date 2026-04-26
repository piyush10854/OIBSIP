# Chat Application (Python) — Beginner Project

## Objective

The objective of this project is to build a basic real-time chat application using Python. It demonstrates how two or more users can communicate over a network using a client-server architecture.

---

## Project Description

This is a command-line-based chat application where multiple users can connect to a central server and exchange messages instantly. The project uses socket programming and multithreading to handle multiple clients simultaneously.

---

## Tools & Technologies Used

* **Python** 
* **Socket Programming** (for network communication)
* **Threading Module** (for handling multiple users)
* **Command Line Interface (CLI)**

---

## Steps Performed

1. **Server Setup**

   * Created a server using Python sockets.
   * Configured it to listen for incoming client connections.

2. **Client Setup**

   * Developed a client program that connects to the server.
   * Allowed users to enter a nickname for identification.

3. **Real-time Communication**

   * Implemented message sending and receiving.
   * Used multithreading to handle multiple clients simultaneously.

4. **Broadcast System**

   * Messages from one client are sent to all connected users.

5. **Error Handling**

   * Managed disconnections and removed inactive users.

---

## How to Run the Project

### Step 1: Start Server

```bash
python server.py
```

### Step 2: Start Clients (Open multiple terminals)

```bash
python client.py
```

### Step 3: Enter Nickname and Start Chatting

---

## Sample Output

```
User1: Hello
User2: Hi!
User1: How are you?
User2: I'm good!
```

---

## Outcome

* Successfully built a real-time chat system.
* Learned core concepts of:

  * Networking
  * Client-server architecture
  * Multithreading
* Enabled communication between multiple users through a simple interface.

---

## Future Enhancements

* GUI-based chat interface
* User authentication system
* File and image sharing
* Emoji support 
* Message encryption 

---

## Conclusion

This project provides a strong foundation in networking and real-time application development using Python. It can be further expanded into a full-featured chat application.

## Author 

Piyush Pandey 
---
