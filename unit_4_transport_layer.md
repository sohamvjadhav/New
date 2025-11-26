# Unit IV: Transport Layer

## 1. Prerequisite Review
*   **Host-to-Host vs. Process-to-Process**: The Network Layer gets the packet to the correct computer (Host). The Transport Layer gets it to the correct application (Process) running on that computer.
*   **Reliability**: The Network Layer (IP) is unreliable. The Transport Layer is responsible for fixing errors, if needed.

---

## 2. Services & Fundamentals

### 2.1 Port Addressing
*   **Analogy**: The IP address is the apartment building address. The **Port Number** is the specific apartment number where a person (application) lives.
*   **Socket**: IP Address + Port Number = Socket (e.g., `192.168.1.1:80`). This uniquely identifies a connection.
*   **Well-Known Ports**:
    *   80: HTTP (Web)
    *   443: HTTPS (Secure Web)
    *   25: SMTP (Email)
    *   53: DNS

### 2.2 Multiplexing & Demultiplexing
*   **Multiplexing (Sender)**: Gathering data from different apps (Chrome, Spotify, Zoom), adding headers, and sending them out as a single stream of packets.
*   **Demultiplexing (Receiver)**: Receiving the stream, checking the Port Number, and delivering the data to the correct app.

---

## 3. UDP (User Datagram Protocol)
**UDP** is the "fire and forget" protocol.

### 3.1 Characteristics
*   **Connectionless**: No handshake. Just send.
*   **Unreliable**: No guarantees. If a packet is lost, it's gone.
*   **Fast**: Low overhead (small header).
*   **Use Cases**: Streaming (YouTube, Netflix), VoIP (Skype), Gaming (where speed > perfection).

### 3.2 Header
*   Very simple, only 8 bytes:
    1.  Source Port
    2.  Destination Port
    3.  Length
    4.  Checksum (for error detection)

---

## 4. TCP (Transmission Control Protocol)
**TCP** is the reliable workhorse of the internet.

### 4.1 Characteristics
*   **Connection-Oriented**: Must establish a connection before sending data.
*   **Reliable**: Guarantees delivery, in order, without errors.
*   **Byte-Stream**: Data is sent as a continuous stream of bytes.

### 4.2 The 3-Way Handshake (Connection Setup)
Before talking, Alice and Bob must agree to talk.
1.  **SYN** (Synchronize): Client sends "Let's connect! My sequence number is X."
2.  **SYN-ACK**: Server says "Okay! I see X. My sequence number is Y."
3.  **ACK**: Client says "Okay! I see Y. Connection established."

### 4.3 Flow Control
**Flow Control** prevents the sender from overwhelming the **receiver**.
*   **Sliding Window Protocol**: The receiver tells the sender "I have room for 5000 bytes" (Window Size). The sender sends 5000 bytes and waits for an update.
*   **Analogy**: Eating a hot dog. You tell the person feeding you "Slow down!" if your mouth is full.

### 4.4 Congestion Control
**Congestion Control** prevents the sender from overwhelming the **network** (routers).
*   **Analogy**: Traffic jam. If everyone drives onto the highway at once, no one moves.
*   **Algorithms**:
    1.  **Slow Start**: Start sending slowly (1 packet). If successful, double it (2, 4, 8...). Exponential growth.
    2.  **Congestion Avoidance**: When a threshold is reached, grow linearly (add 1).
    3.  **Congestion Detection**: If a packet is lost (timeout), assume congestion. Drop the speed dramatically (back to 1 or half).
    4.  **AIMD (Additive Increase, Multiplicative Decrease)**: Slowly increase speed to find the limit, but cut speed by half immediately if a problem occurs.

---

## 5. Reliability Mechanisms
How does TCP ensure reliability?

1.  **Sequence Numbers**: Every byte is numbered. The receiver can reorder packets if they arrive out of order.
2.  **Acknowledgments (ACK)**: The receiver tells the sender "I received everything up to byte X."
3.  **Retransmission**:
    *   **Timeout**: If I don't get an ACK after a certain time, I assume the packet is lost and send it again.
    *   **Fast Retransmit**: If I get 3 duplicate ACKs for the same packet, I know the *next* packet is missing, so I resend it immediately without waiting for the timer.

---

## Unit IV Summary
*   **UDP** is fast but unreliable (Streaming). **TCP** is reliable but slower (Web, Email).
*   **Ports** identify applications.
*   **3-Way Handshake** establishes a TCP connection.
*   **Flow Control** protects the receiver (Sliding Window).
*   **Congestion Control** protects the network (Slow Start, AIMD).
