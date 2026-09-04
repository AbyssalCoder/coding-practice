## Reverse Proxy

Sits in front of backend servers and forwards client requests.

### Benefits
- SSL termination
- Load balancing
- Caching static content
- Hiding backend topology
- Rate limiting

### Nginx reverse proxy config
```nginx
server {
    listen 80;
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
    }
}
```

## 2026-08-27

Practiced Load Balancers with some exercises.

Going to revisit this topic next week for deeper understanding.


<!-- formatting -->

## 2026-09-04

Morning study session: Linear Search.

The hands-on practice made the theory click.
