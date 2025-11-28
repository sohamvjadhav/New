# Unit V: Application Layer

## 1. Prerequisite Review
*   **User Interface**: The Application Layer is where the human interacts with the network. It's the web browser, the email client, the file transfer tool.
*   **Client-Server Model**: Most apps work this way. A **Client** (your phone) requests a service, and a **Server** (a powerful computer in a data center) provides it.

---

## 2. DNS (Domain Name System)
**DNS** is the phonebook of the internet.

### 2.1 Hierarchy
*   **Root Servers**: The top of the tree (represented by a dot `.`).
*   **TLD (Top-Level Domain)**: `.com`, `.org`, `.edu`, `.in`.
*   **Authoritative Servers**: The servers that actually know the IP address for a specific domain (e.g., `google.com`).

### 2.2 Resolution Process
How does your computer find `www.example.com`?
1.  **Browser Cache**: "Have I been there recently?"
2.  **OS Cache**: "Does my computer know?"
3.  **Resolver (ISP)**: "Hey ISP, do you know?"
4.  **Root Server**: "I don't know, but here is the address for `.com`."
5.  **TLD Server**: "I don't know, but here is the address for `example.com`."
6.  **Authoritative Server**: "Yes! The IP is `93.184.216.34`."

### 2.3 Record Types
*   **A**: IPv4 Address.
*   **AAAA**: IPv6 Address.
*   **MX**: Mail Exchange (Email server).
*   **CNAME**: Canonical Name (Alias, e.g., `www` -> `server1`).
*   **NS**: Name Server (Who is authoritative?).
*   **PTR**: Pointer Record (Reverse DNS). Maps IP to Domain Name.

---

## 3. HTTP (HyperText Transfer Protocol)
**HTTP** is the protocol of the World Wide Web.

### 3.1 Versions
*   **HTTP/1.0**: Old. Created a new TCP connection for every file (very slow).
*   **HTTP/1.1**: Persistent connections (keep-alive). Reuse the connection for multiple files.
*   **HTTP/2.0**: Multiplexing. Send multiple requests at once over a single connection. Binary (not text).

### 3.2 Request/Response
*   **Request**: Client sends "GET /index.html HTTP/1.1".
*   **Response**: Server sends "HTTP/1.1 200 OK" followed by the webpage.

### 3.3 Methods (Verbs)
*   **GET**: Retrieve data (Loading a page).
*   **POST**: Submit data (Filling a form).
*   **PUT**: Update data (Uploading a file).
*   **DELETE**: Remove data.

### 3.3 Status Codes
*   **2xx (Success)**: 200 OK.
*   **3xx (Redirection)**: 301 Moved Permanently.
*   **4xx (Client Error)**: 404 Not Found (You typed the URL wrong).
*   **5xx (Server Error)**: 500 Internal Server Error (The server crashed).

### 3.4 HTTPS & TLS/SSL
*   **HTTP** is plain text. Anyone can spy on it.
*   **HTTPS** is HTTP + **SSL/TLS** (Encryption). It ensures:
    1.  **Privacy**: No one can read the data.
    2.  **Integrity**: No one changed the data.
    3.  **Authentication**: You are talking to the real bank, not a fake one.

---

## 4. Email Protocols
Sending an email involves multiple protocols.

### 4.1 SMTP (Simple Mail Transfer Protocol)
*   **Role**: **Pushing** mail.
*   Used by the sender to send email to the server, and by servers to send email to other servers.

### 4.2 POP3 (Post Office Protocol v3)
*   **Role**: **Pulling** mail.
*   **Behavior**: Downloads email to your device and deletes it from the server. Good for one device, bad for multiple (phone + laptop).

### 4.3 IMAP (Internet Message Access Protocol)
*   **Role**: **Syncing** mail.
*   **Behavior**: Reads email on the server. Keeps everything in sync across multiple devices.

### 4.4 MIME (Multipurpose Internet Mail Extensions)
*   SMTP only supports text. **MIME** allows sending images, audio, video, and non-English characters in email.

---

## 5. Other Protocols

### 5.1 FTP (File Transfer Protocol)
*   Used for transferring large files.
*   **Two Connections**:
    1.  **Control Connection (Port 21)**: Sends commands (Login, CD, LS).
    2.  **Data Connection (Port 20)**: Sends the actual file.
*   **Modes**:
    *   **Active Mode**: Client opens a random port and server connects back to it (Problematic for firewalls).
    *   **Passive Mode**: Server opens a random port and client connects to it (Firewall friendly).

### 5.2 DHCP (Dynamic Host Configuration Protocol)
*   **Role**: Automatically assigns IP addresses to devices when they join a network.
*   **Process (DORA)**:
    1.  **D**iscover: "Is there a DHCP server?"
    2.  **O**ffer: "Yes, you can use `192.168.1.50`."
    3.  **R**equest: "Great, I'll take it."
    4.  **A**cknowledge: "It's yours for 24 hours."

### 5.3 SSH (Secure Shell) vs Telnet
*   **Telnet**: Remote login, but sends passwords in plain text (Unsafe!).
*   **SSH**: Encrypted remote login (Safe!). Used by admins to manage servers.

### 5.4 SNMP (Simple Network Management Protocol)
*   **Purpose**: Monitoring network devices (routers, switches, printers).
*   **Components**:
    *   **Manager**: The central computer monitoring everything.
    *   **Agent**: The software running on the router/switch.
    *   **MIB (Management Information Base)**: The database of variables (CPU usage, bandwidth, errors).

---

## Unit V Summary
*   **DNS** translates Names to IPs.
*   **HTTP** transfers web pages; **HTTPS** secures them.
*   **SMTP** sends email; **IMAP** syncs it.
*   **DHCP** gives you an IP address automatically.
