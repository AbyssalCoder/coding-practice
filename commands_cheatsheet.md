## Docker Compose

Define multi-container apps in a single YAML file.

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - '8080:8080'
    depends_on:
      - db
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

```bash
docker compose up -d
docker compose logs -f
docker compose down
```
