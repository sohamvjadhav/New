# Network Theory Study Guide - Units III-VI

A comprehensive, beginner-friendly PDF study guide for undergraduate networking theory exams covering 28 hours of material.

## 📚 Contents

This study guide covers four major units of network theory:

### Unit III: Network Layer (7 Hours)
- **IPv4 Addressing**: Classful/classless addressing, structure, notation, subnetting, VLSM, NAT, CIDR
- **IPv6**: Address format, types (unicast, multicast, anycast), header structure, IPv4-IPv6 transitions
- **Routing**: Static vs dynamic, routing tables, Distance Vector (Bellman-Ford, RIP, count-to-infinity), Link State (Dijkstra, OSPF, LSA flooding), packet forwarding
- **Protocols**: IP, ICMP, ARP, RARP, fragmentation/reassembly

### Unit IV: Transport Layer (7 Hours)
- **Services**: Process-to-process communication, port addressing, sockets, multiplexing/demultiplexing
- **UDP**: Header structure, characteristics, applications, checksum calculation
- **TCP**: Header structure, 3-way handshake, 4-way termination, sequence/acknowledgment numbers
- **Flow Control**: Sliding window, window management, stop-and-wait vs pipelining
- **Congestion Control**: Causes, TCP algorithms (slow start, congestion avoidance, fast retransmit/recovery), AIMD
- **Reliability**: Error detection/correction, retransmission strategies, timeout mechanisms

### Unit V: Application Layer (7 Hours)
- **DNS**: Hierarchy, architecture, query types, record types (A, AAAA, MX, CNAME, NS, PTR), resolution process
- **HTTP/HTTPS**: Methods (GET, POST, PUT, DELETE), request/response structure, status codes, versions (1.0, 1.1, 2.0), TLS/SSL
- **Email Protocols**: SMTP, POP3, IMAP, MIME
- **FTP**: Architecture, active/passive modes, commands/responses
- **Other**: DHCP, Telnet, SSH, SNMP

### Unit VI: Network Security (7 Hours)
- **Fundamentals**: Security services (confidentiality, integrity, authentication, non-repudiation, availability), threats, attack types
- **Cryptography**: Symmetric (DES, 3DES, AES), asymmetric (RSA, Diffie-Hellman), hash functions (MD5, SHA), digital signatures, certificates
- **Protocols**: IPSec (AH, ESP, tunnel/transport modes), SSL/TLS handshake, HTTPS, S/MIME
- **Infrastructure**: PKI, CAs, firewalls, IDS/IPS, VPNs

## 🎯 Key Features

- **Beginner-Friendly**: Assumes minimal prior networking knowledge
- **Progressive Learning**: Builds from foundational concepts to advanced applications
- **Prerequisite Reviews**: Each unit starts with a review of necessary background concepts
- **Visual Learning**: Includes diagrams and illustrations for complex concepts
- **Real-World Examples**: Practical applications and scenarios throughout
- **Highlighted Key Concepts**: Important information emphasized with colored boxes
- **Comprehensive Glossary**: Quick reference for all major terms
- **Unit Summaries**: Checklists for key concepts in each unit
- **Exam Preparation Tips**: Study strategies and common question types

## 📖 Document Structure

1. **Abstract**: Overview of the study guide
2. **Table of Contents**: Detailed navigation
3. **Unit III-VI**: Comprehensive coverage of all topics
4. **Glossary**: Alphabetical listing of key networking terms
5. **Exam Preparation Tips**: Study strategies and final checklist

## 📄 Files

- `network_theory_study_guide.pdf` - The complete study guide (61 pages)
- `network_theory_study_guide.tex` - LaTeX source file
- `README.md` - This file

## 🔧 Building from Source

If you want to regenerate the PDF from the LaTeX source:

```bash
# Install LaTeX (Ubuntu/Debian)
sudo apt-get install texlive-latex-base texlive-latex-extra texlive-fonts-recommended

# Compile the PDF (run twice for proper references)
pdflatex network_theory_study_guide.tex
pdflatex network_theory_study_guide.tex
```

## 📐 Document Statistics

- **Pages**: 61
- **File Size**: ~313 KB
- **Format**: PDF (optimized for printing and digital viewing)
- **Coverage**: 28 hours of course material

## 🎓 How to Use This Guide

1. **Sequential Reading**: Start from Unit III and progress through Unit VI
2. **Topic-Based Study**: Use the table of contents to jump to specific topics
3. **Active Learning**: Work through the examples and practice problems
4. **Review Sessions**: Use unit summaries and glossary for quick review
5. **Exam Preparation**: Follow the exam tips in the final section

## ✨ Quality Standards

- Clear, accessible language suitable for undergraduate beginners
- Logical progression from foundations to complex concepts
- Consistent terminology and notation throughout
- Professional formatting with clear sections and subsections
- Comprehensive coverage of all specified topics

## 📝 License

This study guide is provided for educational purposes.

## 🤝 Contributing

Suggestions for improvements are welcome. Please ensure any contributions maintain:
- Beginner-friendly explanations
- Progressive complexity
- Consistent formatting
- Accurate technical information

---

**Good luck with your exam preparation!** 🚀
