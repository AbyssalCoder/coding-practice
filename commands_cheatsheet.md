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

## Git Basics

```bash
git init                        # Initialize repo
git add .                       # Stage all changes
git commit -m 'Initial commit'  # Commit
git status                      # Check status
git log --oneline               # Compact log
git diff                        # Show unstaged changes
git diff --staged               # Show staged changes
```

### Three areas
Working Directory → Staging Area → Repository

## GitHub Actions — CI/CD

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: python -m pytest
```

Workflows live in `.github/workflows/` and trigger on events.


<!-- fixed typo -->
