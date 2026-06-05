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
