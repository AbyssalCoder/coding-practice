## Docker Volumes

Volumes persist data beyond container lifecycle.

```bash
# Named volume
docker volume create mydata
docker run -v mydata:/app/data nginx

# Bind mount (host directory)
docker run -v $(pwd)/data:/app/data nginx

# List volumes
docker volume ls

# Inspect
docker volume inspect mydata
```

Prefer named volumes over bind mounts in production.

## CI/CD Basics

### Continuous Integration (CI)
- Automatically build and test on every push
- Catch bugs early
- Run linters, formatters, tests

### Continuous Delivery (CD)
- Automatically deploy after CI passes
- Staging → Production pipeline

### Popular tools
- GitHub Actions
- GitLab CI
- Jenkins
- CircleCI
- Travis CI

A good pipeline: Lint → Test → Build → Deploy


<!-- fixed typo -->
