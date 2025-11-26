# Unit III: Network Layer

## 1. Prerequisite Review
Before diving into the Network Layer, let's recall a few key concepts:
*   **Data Encapsulation**: Data moves down the layers, getting wrapped in headers. The Network Layer adds an **IP Header** to the Transport Layer segment, creating a **Packet**.
*   **Addressing**: Just like houses have addresses, devices on a network need unique identifiers. We've seen MAC addresses (Data Link Layer) which are physical and permanent. Now we introduce **IP Addresses** (Network Layer) which are logical and hierarchical.
*   **The Goal**: The Network Layer is responsible for **Host-to-Host delivery**. It's like the postal service ensuring a letter gets from your house to your friend's house, regardless of the path it takes.

---

## 2. IPv4 Addressing
**Internet Protocol version 4 (IPv4)** is the fundamental addressing system of the internet.

### 2.1 Structure and Notation
*   **Analogy**: Think of an IP address like a phone number. It has an area code (Network ID) and a subscriber number (Host ID).
*   **Format**: A 32-bit address, typically written in **Dotted Decimal Notation** (e.g., `192.168.1.1`).
*   **Bits**: 32 bits total, divided into 4 octets (8 bits each).
    *   Example: `11000000.10101000.00000001.00000001` = `192.168.1.1`

### 2.2 Classful Addressing (Legacy)
Originally, IP addresses were divided into "Classes" to define the network size.

| Class | Leading Bits | Range (1st Octet) | Default Subnet Mask | Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **A** | `0` | 1 - 126 | 255.0.0.0 (/8) | Huge networks (ISPs, Gov) |
| **B** | `10` | 128 - 191 | 255.255.0.0 (/16) | Medium networks (Universities) |
| **C** | `110` | 192 - 223 | 255.255.255.0 (/24) | Small networks (Home/Office) |
| **D** | `1110` | 224 - 239 | N/A | Multicast (Streaming) |
| **E** | `1111` | 240 - 255 | N/A | Experimental/Research |

*   **Problem**: Inefficient. A Class A network has 16 million addresses! If a company needed 5000, giving them a Class B (65,000) wasted 60,000 addresses.

### 2.3 Subnetting
**Subnetting** is the process of borrowing bits from the Host ID to create a Subnet ID.
*   **Analogy**: A large office building (Network) is divided into floors (Subnets). The main address gets you to the building, the floor number gets you to the department.
*   **Benefit**: Reduces network traffic (broadcast domains) and improves security.
*   **Subnet Mask**: A 32-bit number that tells the computer which part of the IP is the Network and which is the Host.
    *   `1`s represent the Network.
    *   `0`s represent the Host.

### 2.4 CIDR (Classless Inter-Domain Routing)
**CIDR** replaced Classful addressing. It allows for flexible network sizes using "slash notation".
*   **Notation**: `IP_Address / Prefix_Length`
*   **Example**: `192.168.1.0/24` means the first 24 bits are the network.
*   **VLSM (Variable Length Subnet Mask)**: Allows a network administrator to use different subnet masks for subnets of the same network, optimizing address usage.

### 2.5 NAT (Network Address Translation)
**NAT** allows multiple devices on a private network to share a single public IP address.
*   **Analogy**: An apartment complex has one main mailing address. The concierge (NAT Router) sorts the mail to individual apartment numbers (Private IPs).
*   **Private IP Ranges** (Not routable on the internet):
    *   `10.0.0.0` - `10.255.255.255`
    *   `172.16.0.0` - `172.31.255.255`
    *   `192.168.0.0` - `192.168.255.255`

---

## 3. IPv6 Addressing
We ran out of IPv4 addresses! **IPv6** is the successor.

### 3.1 Key Differences
*   **Size**: 128-bit address (vs 32-bit). That's enough for every grain of sand on Earth to have an IP.
*   **Format**: Hexadecimal, separated by colons.
    *   Example: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
*   **Header**: Simplified header for faster processing. No checksum (Transport layer handles it).

### 3.2 Address Types
1.  **Unicast**: One-to-One. (Send to a specific device).
2.  **Multicast**: One-to-Many. (Send to a group).
3.  **Anycast**: One-to-Nearest. (Send to the closest server in a group, e.g., DNS).
    *   *Note: IPv6 has no Broadcast.*

### 3.3 Transition Strategies
How do we switch from IPv4 to IPv6?
1.  **Dual Stack**: Devices run both IPv4 and IPv6 simultaneously.
2.  **Tunneling**: Wrapping an IPv6 packet inside an IPv4 packet to cross an IPv4 network.
3.  **Translation**: Converting headers between versions (NAT64).

---

## 4. Routing
**Routing** is finding the best path for a packet to travel from source to destination.

### 4.1 Static vs Dynamic
*   **Static Routing**: Admin manually types in the routes.
    *   *Pros*: Secure, no overhead.
    *   *Cons*: Doesn't adapt to failures. Hard to manage in large networks.
*   **Dynamic Routing**: Routers talk to each other to learn paths.
    *   *Pros*: Automatic, scalable, adapts to broken links.
    *   *Cons*: Uses bandwidth and CPU.

### 4.2 Distance Vector Routing (e.g., RIP)
*   **Concept**: "Tell your neighbors about the world."
*   **Metric**: Hop count (number of routers to cross).
*   **Algorithm**: Bellman-Ford.
*   **Problem**: **Count-to-Infinity**. If A tells B "I can reach C", and the link to C breaks, A might learn a path to C *through* B (which is actually A -> B -> A -> ...).
    *   *Fix*: Split Horizon (don't tell a neighbor about a route you learned from them).

### 4.3 Link State Routing (e.g., OSPF)
*   **Concept**: "Tell the world about your neighbors."
*   **Mechanism**:
    1.  Discover neighbors (Hello packets).
    2.  Measure cost (delay, bandwidth).
    3.  Flood **LSA (Link State Advertisements)** to everyone.
    4.  Build a map of the entire network.
    5.  Run **Dijkstra's Algorithm** to find the Shortest Path.

---

## 5. Protocols

### 5.1 IP (Internet Protocol)
*   **Unreliable**: Best effort delivery. No guarantees.
*   **Connectionless**: Each packet is independent.

### 5.2 ICMP (Internet Control Message Protocol)
*   **Purpose**: Error reporting and diagnostics.
*   **Tools**: `ping` (Echo Request/Reply) and `traceroute`.
*   **Messages**: "Destination Unreachable", "Time Exceeded" (TTL expired).

### 5.3 ARP (Address Resolution Protocol)
*   **Problem**: I know the IP address (`192.168.1.5`), but I need the MAC address to send the frame.
*   **Solution**: Broadcast "Who has 192.168.1.5?"
*   **Reply**: "I do! Here is my MAC."
*   **RARP**: Reverse ARP (Diskless workstations asking "What is my IP?").

### 5.4 Fragmentation
*   **MTU (Maximum Transmission Unit)**: The largest packet a network link can carry (usually 1500 bytes for Ethernet).
*   **Process**: If a packet is too big, the router breaks it into fragments.
*   **Reassembly**: Happens **only at the destination**, not intermediate routers.

---

## Unit III Summary
*   **IPv4** uses 32-bit addresses; **IPv6** uses 128-bit addresses.
*   **Subnetting** divides networks; **CIDR** allows flexible sizing.
*   **Routing** finds the path: **Distance Vector** (Hops, Neighbors) vs **Link State** (Map, Dijkstra).
*   **ARP** maps IP to MAC. **ICMP** helps debug.
