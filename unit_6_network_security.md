# Unit VI: Network Security

## 1. Prerequisite Review
*   **The Internet is Public**: By default, the internet is like a postcard. Anyone handling it can read it. Security is about putting that postcard in a sealed envelope (Encryption).
*   **Trust**: How do you know the website you are visiting is actually your bank and not a hacker? (Authentication).

---

## 2. Fundamentals

### 2.1 Security Services (CIA Triad + 2)
1.  **Confidentiality**: Only authorized people can read the data. (Privacy).
2.  **Integrity**: The data hasn't been changed in transit.
3.  **Availability**: The system is up and running when needed.
4.  **Authentication**: Verifying the identity of the user/sender.
5.  **Non-Repudiation**: The sender cannot deny sending the message later (like a digital signature).

### 2.2 Threats & Attacks
*   **Passive Attack**: The hacker just listens (Eavesdropping). Hard to detect, easy to prevent (Encryption).
*   **Active Attack**: The hacker changes data or disrupts service. Easy to detect, hard to prevent.
    *   **Masquerading**: Pretending to be someone else (Spoofing).
    *   **Replay**: Recording a valid message (like a bank transfer) and sending it again later.
    *   **DoS (Denial of Service)**: Flooding a server with traffic so it crashes.

---

## 3. Cryptography
**Cryptography** is the science of secret writing.

### 3.1 Symmetric Key Cryptography
*   **Concept**: Use the **SAME key** to lock (encrypt) and unlock (decrypt) the box.
*   **Analogy**: A house key. You give a copy to your friend. Both of you can lock and unlock the door.
*   **Algorithms**: DES (Old, broken), 3DES (Better), **AES** (Current standard, very strong).
*   **Problem**: How do you share the key securely in the first place?

### 3.2 Asymmetric Key Cryptography (Public Key)
*   **Concept**: Use **TWO keys**. A **Public Key** (to lock) and a **Private Key** (to unlock).
*   **Analogy**: A mailbox. Anyone can put a letter in (Public Key), but only the postman with the key can take it out (Private Key).
*   **Algorithms**: **RSA**, Diffie-Hellman (for key exchange).
*   **Benefit**: Solves the key sharing problem.

### 3.3 Hash Functions
*   **Concept**: A one-way fingerprint of data. You cannot get the data back from the hash.
*   **Use**: Checking Integrity. If even one bit of the file changes, the hash changes completely.
*   **Algorithms**: MD5 (Old), SHA-1, **SHA-256**.

### 3.4 Digital Signatures
*   **Goal**: Prove authenticity and integrity.
*   **Process**:
    1.  Hash the message.
    2.  Encrypt the hash with your **Private Key**.
    3.  Receiver decrypts with your **Public Key** and compares the hash.

---

## 4. Protocols

### 4.1 IPSec (Internet Protocol Security)
*   Secures IP packets at the Network Layer. Used in VPNs.
*   **Modes**:
    *   **Transport Mode**: Encrypts only the payload (data).
    *   **Tunnel Mode**: Encrypts the entire packet (header + data).
*   **Components**: AH (Authentication Header) and ESP (Encapsulating Security Payload).

### 4.2 SSL/TLS (Secure Sockets Layer / Transport Layer Security)
*   Secures the Transport Layer (Web, Email). TLS is the modern version of SSL.
*   **Handshake**:
    1.  Client says "Hello, I support these algorithms."
    2.  Server says "Hello, let's use this one. Here is my Certificate."
    3.  Client verifies Certificate with a CA (Certificate Authority).
    4.  They exchange keys and start encrypted communication.

### 4.3 S/MIME (Secure/Multipurpose Internet Mail Extensions)
*   **Purpose**: Securing Email (Authentication, Integrity, Privacy).
*   **Mechanism**:
    *   **Signing**: Encrypt hash with sender's Private Key (Proof of Origin).
    *   **Encryption**: Encrypt message with receiver's Public Key (Confidentiality).

---

## 5. Infrastructure

### 5.1 PKI (Public Key Infrastructure)
*   The system that manages Digital Certificates.
*   **CA (Certificate Authority)**: A trusted company (like Verisign or Let's Encrypt) that issues certificates. They vouch that "This Public Key belongs to Google.com".

### 5.2 Firewalls
*   **Gatekeeper**: Sits between your network and the internet.
*   **Packet Filtering**: "Block all traffic on Port 80 except from this IP."
*   **Stateful**: "Only allow incoming traffic if it's a reply to an outgoing request."

### 5.3 IDS/IPS (Intrusion Detection/Prevention System)
*   **IDS (Detection)**: The burglar alarm. Watches network traffic for suspicious patterns (signatures) and alerts the admin. Does not stop the attack.
*   **IPS (Prevention)**: The security guard. Watches traffic and *blocks* it if it looks like an attack.

### 5.4 VPN (Virtual Private Network)
*   **Tunnel**: Creates a secure, encrypted tunnel over the public internet.
*   **Use**: Employees working from home can access the office network securely.

---

## Unit VI Summary
*   **CIA Triad**: Confidentiality, Integrity, Availability.
*   **Symmetric**: One key (Fast). **Asymmetric**: Two keys (Secure key exchange).
*   **HTTPS** uses **TLS** to secure the web.
*   **Firewalls** filter traffic; **VPNs** create secure tunnels.
