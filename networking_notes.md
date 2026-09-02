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
