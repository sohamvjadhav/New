# Network Theory Quick Reference Card

A condensed reference guide for quick lookup during study sessions.

## 🌐 IPv4 Quick Reference

### Subnet Mask Cheat Sheet
```
/8  = 255.0.0.0         = 16,777,214 hosts
/16 = 255.255.0.0       = 65,534 hosts
/24 = 255.255.255.0     = 254 hosts
/25 = 255.255.255.128   = 126 hosts
/26 = 255.255.255.192   = 62 hosts
/27 = 255.255.255.224   = 30 hosts
/28 = 255.255.255.240   = 14 hosts
/29 = 255.255.255.248   = 6 hosts
/30 = 255.255.255.252   = 2 hosts (point-to-point links)
```

### Private IP Ranges
- **Class A**: 10.0.0.0 - 10.255.255.255 (10.0.0.0/8)
- **Class B**: 172.16.0.0 - 172.31.255.255 (172.16.0.0/12)
- **Class C**: 192.168.0.0 - 192.168.255.255 (192.168.0.0/16)

### Special Addresses
- **Loopback**: 127.0.0.0/8 (127.0.0.1 = localhost)
- **Link-Local**: 169.254.0.0/16
- **Broadcast**: 255.255.255.255

## 🔢 Common Port Numbers

### Well-Known Ports (0-1023)
```
20/21  - FTP (data/control)
22     - SSH
23     - Telnet
25     - SMTP
53     - DNS
67/68  - DHCP (server/client)
80     - HTTP
110    - POP3
143    - IMAP
443    - HTTPS
```

### Registered Ports (1024-49151)
```
3306   - MySQL
5432   - PostgreSQL
8080   - HTTP alternate
```

## 📊 Protocol Comparisons

### TCP vs UDP
| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | Guaranteed delivery | Best effort |
| Ordering | Maintains order | No ordering |
| Speed | Slower (overhead) | Faster |
| Header Size | 20-60 bytes | 8 bytes |
| Use Cases | HTTP, FTP, Email | DNS, Streaming, Gaming |

### RIP vs OSPF
| Feature | RIP | OSPF |
|---------|-----|------|
| Type | Distance Vector | Link State |
| Algorithm | Bellman-Ford | Dijkstra |
| Metric | Hop count | Cost (bandwidth) |
| Max Hops | 15 | Unlimited |
| Convergence | Slow | Fast |
| Scalability | Small networks | Large networks |

### SMTP vs POP3 vs IMAP
| Feature | SMTP | POP3 | IMAP |
|---------|------|------|------|
| Purpose | Send email | Retrieve email | Retrieve email |
| Port | 25/587 | 110 | 143 |
| Direction | Push | Pull | Pull |
| Storage | Server | Client (downloads) | Server (keeps) |
| Multiple Access | N/A | No | Yes |

## 🔐 Cryptography Quick Reference

### Symmetric Algorithms
- **DES**: 56-bit key (OBSOLETE)
- **3DES**: 168-bit key (PHASING OUT)
- **AES**: 128/192/256-bit key (CURRENT STANDARD)

### Asymmetric Algorithms
- **RSA**: Key sizes 2048/4096 bits (digital signatures, key exchange)
- **Diffie-Hellman**: Key exchange protocol

### Hash Functions
- **MD5**: 128-bit hash (BROKEN - don't use)
- **SHA-1**: 160-bit hash (DEPRECATED)
- **SHA-256**: 256-bit hash (SECURE - current standard)
- **SHA-3**: Variable length (SECURE - latest standard)

## 📈 TCP States

### Connection Establishment
```
CLOSED → SYN_SENT → ESTABLISHED (client)
CLOSED → LISTEN → SYN_RECEIVED → ESTABLISHED (server)
```

### Connection Termination
```
ESTABLISHED → FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT → CLOSED
ESTABLISHED → CLOSE_WAIT → LAST_ACK → CLOSED
```

## 🎯 Key Formulas

### Subnetting
```
Number of subnets = 2^n (n = borrowed bits)
Hosts per subnet = 2^h - 2 (h = host bits)
Subnet size = 256 - last octet of mask
```

### TCP Congestion Control
```
AIMD: cwnd increases by 1 MSS per RTT (additive)
      cwnd decreases by half on loss (multiplicative)

Slow Start: cwnd doubles each RTT until ssthresh
Congestion Avoidance: cwnd += 1 MSS per RTT
```

### RTO Calculation
```
EstimatedRTT = (1-α) × EstimatedRTT + α × SampleRTT
DevRTT = (1-β) × DevRTT + β × |SampleRTT - EstimatedRTT|
RTO = EstimatedRTT + 4 × DevRTT

(α = 0.125, β = 0.25)
```

## 📡 HTTP Status Codes

### Success (2xx)
- **200** OK
- **201** Created
- **204** No Content

### Redirection (3xx)
- **301** Moved Permanently
- **302** Found (temporary redirect)
- **304** Not Modified

### Client Error (4xx)
- **400** Bad Request
- **401** Unauthorized
- **403** Forbidden
- **404** Not Found

### Server Error (5xx)
- **500** Internal Server Error
- **502** Bad Gateway
- **503** Service Unavailable

## 🔒 Security Services (CIA Triad+)

- **C**onfidentiality: Encryption (unauthorized viewing)
- **I**ntegrity: Hashing (unauthorized modification)
- **A**uthenticity: Digital signatures (identity verification)
- **A**vailability: Redundancy, DDoS protection
- **Non-repudiation**: Digital signatures (can't deny)

## 🛡️ Common Attacks & Defenses

| Attack | Defense |
|--------|---------|
| Eavesdropping | Encryption (TLS/SSL, VPN) |
| Masquerading | Authentication, certificates |
| Replay | Timestamps, nonces, sequence numbers |
| Modification | MACs, digital signatures |
| DoS/DDoS | Rate limiting, firewalls, DDoS protection |

## 📧 Email Flow

### Sending (SMTP)
```
User Agent → Mail Server (SMTP) → Recipient's Mail Server (SMTP) → Mailbox
```

### Receiving (POP3/IMAP)
```
Mailbox → Mail Server → User Agent (POP3/IMAP)
```

## 🌍 DNS Record Types

- **A**: IPv4 address
- **AAAA**: IPv6 address
- **CNAME**: Canonical name (alias)
- **MX**: Mail exchange server
- **NS**: Name server
- **PTR**: Reverse DNS (IP to name)
- **SOA**: Start of authority
- **TXT**: Text (verification, SPF)

## 🔄 NAT Types

- **Static NAT**: 1 private → 1 public (one-to-one)
- **Dynamic NAT**: Multiple private → pool of public (many-to-many)
- **PAT**: Multiple private → 1 public using ports (many-to-one)

## 📦 MTU Values

- **Ethernet**: 1500 bytes
- **802.11 (WiFi)**: 2304 bytes
- **PPPoE**: 1492 bytes
- **Jumbo Frames**: 9000 bytes

## 🎲 Three-Way Handshake

```
Client                    Server
  |                         |
  |------ SYN (Seq=X) ----->|
  |                         |
  |<-- SYN-ACK (Seq=Y) -----|
  |    (Ack=X+1)            |
  |                         |
  |---- ACK (Ack=Y+1) ----->|
  |                         |
  [Connection Established]
```

## 🔌 IPSec Modes

### Transport Mode
- Encrypts payload only
- Original IP header intact
- Host-to-host communication

### Tunnel Mode
- Encrypts entire packet
- New IP header added
- Site-to-site VPN

## 💾 Data Units by Layer

| Layer | Data Unit |
|-------|-----------|
| Application | Data/Message |
| Transport | Segment (TCP) / Datagram (UDP) |
| Network | Packet |
| Data Link | Frame |
| Physical | Bits |

## 🎯 Exam Tips

### Must Know
1. **Subnetting calculations** (practice 10+ problems)
2. **Dijkstra's algorithm** (can execute on paper)
3. **TCP handshake/termination** (draw from memory)
4. **Port numbers** (memorize top 10)
5. **Protocol comparisons** (TCP/UDP, RIP/OSPF, etc.)

### Common Mistakes
- Forgetting to subtract 2 for network/broadcast addresses
- Mixing up sequence vs acknowledgment numbers
- Confusing symmetric vs asymmetric encryption uses
- Not knowing when to use which protocol

### Time Savers
- Memorize subnet mask chart
- Know port numbers for common services
- Understand protocol purposes (don't just memorize)
- Practice algorithm execution speed

---

**Pro Tip**: Print this reference card and keep it handy during study sessions!
