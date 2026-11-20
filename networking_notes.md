## HTTPS & TLS

HTTPS = HTTP + TLS encryption.

### TLS handshake (simplified)
1. Client Hello (supported cipher suites)
2. Server Hello (chosen cipher + certificate)
3. Key exchange (asymmetric → symmetric key)
4. Encrypted communication begins

### Why HTTPS matters
- Encrypts data in transit
- Authenticates the server via certificates
- Prevents man-in-the-middle attacks
- Required for modern web features (service workers, geolocation)

## JWT Authentication

A JSON Web Token has three parts: `header.payload.signature`

### Flow
1. User logs in with credentials
2. Server validates and returns a signed JWT
3. Client stores JWT (usually in memory or httpOnly cookie)
4. Client sends JWT in `Authorization: Bearer <token>` header
5. Server verifies signature on each request

### Security tips
- Keep tokens short-lived (15-30 min)
- Use refresh tokens for re-auth
- Never store JWTs in localStorage (XSS risk)
- Always validate `exp` and `iss` claims

## VLAN Basics

A Virtual LAN segments a physical network into logical groups.

### Why VLANs?
- Reduce broadcast domains
- Improve security (isolate departments)
- Simplify network management

### Types
- **Data VLAN** — regular user traffic
- **Voice VLAN** — VoIP traffic priority
- **Management VLAN** — switch management
- **Native VLAN** — untagged trunk traffic

VLAN tagging uses IEEE 802.1Q standard.


<!-- fixed typo -->

## TCP Three-Way Handshake

1. **SYN** — Client sends SYN with initial sequence number
2. **SYN-ACK** — Server responds with its own SYN + ACK
3. **ACK** — Client acknowledges, connection established

### Why three steps?
Both sides must agree on initial sequence numbers to guarantee reliable, ordered delivery.

### Connection teardown (4-way)
FIN → ACK → FIN → ACK

TCP is **connection-oriented** and **reliable** — it retransmits lost segments.

## DNS Resolution

DNS translates domain names to IP addresses.

### Resolution flow
1. Browser cache → OS cache → Router cache
2. Recursive resolver (ISP)
3. Root nameserver → TLD nameserver → Authoritative nameserver

### Common record types
| Type  | Purpose              | Example            |
|-------|----------------------|--------------------|
| A     | IPv4 address         | 93.184.216.34      |
| AAAA  | IPv6 address         | 2606:2800:220:1::  |
| CNAME | Alias                | www → example.com  |
| MX    | Mail server          | mail.example.com   |
| TXT   | Verification/SPF     | v=spf1 ...         |

```bash
nslookup example.com
dig example.com A
```

## Subnetting Basics

### CIDR notation
- `192.168.1.0/24` → 256 addresses, 254 usable hosts
- `10.0.0.0/8` → Class A, ~16 million hosts

### Quick subnet math
| CIDR | Subnet Mask     | Hosts |
|------|-----------------|-------|
| /24  | 255.255.255.0   | 254   |
| /25  | 255.255.255.128 | 126   |
| /26  | 255.255.255.192 | 62    |
| /27  | 255.255.255.224 | 30    |
| /28  | 255.255.255.240 | 14    |

Usable hosts = 2^(32 - prefix) - 2
