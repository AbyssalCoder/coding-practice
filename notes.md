## HTTP Basics

### Common methods
- `GET` — Retrieve a resource
- `POST` — Submit data
- `PUT` — Replace a resource
- `PATCH` — Partial update
- `DELETE` — Remove a resource

### Status codes
| Range | Meaning       | Example          |
|-------|---------------|------------------|
| 2xx   | Success       | 200 OK           |
| 3xx   | Redirect      | 301 Moved        |
| 4xx   | Client error  | 404 Not Found    |
| 5xx   | Server error  | 500 Internal     |

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

## Git Branching

```bash
git branch feature-x            # Create branch
git checkout feature-x           # Switch to branch
git checkout -b feature-y        # Create + switch
git branch -d feature-x          # Delete branch
git merge feature-y              # Merge into current
```

### Best practices
- Keep branches short-lived
- Use descriptive names: `feature/login`, `fix/header-bug`
- Delete merged branches

## Claude Code — Observations

Anthropic's CLI coding agent.

### Strengths
- Excellent at multi-file refactoring
- Understands project context across many files
- Strong at writing tests
- Good at explaining existing code

### Setup
```bash
npm install -g @anthropic-ai/claude-code
claude
```

Works directly in the terminal. Reads your repo and makes edits in place.

## String Manipulation Basics

```python
s = 'hello world'

print(s.upper())         # HELLO WORLD
print(s.title())         # Hello World
print(s.split())         # ['hello', 'world']
print(s.replace('o', '0'))  # hell0 w0rld
print(s.count('l'))      # 3
print(s.find('world'))   # 6
```

String methods return new strings — strings are immutable in Python.

## Gemini CLI — Google's Terminal AI

### Setup
```bash
npm install -g @anthropic-ai/gemini-cli  # placeholder
gemini
```

### Features
- Free with Google account
- 1M token context window
- Can read and edit local files
- Supports extensions (Google Search, etc.)

Huge context window makes it good for analyzing large codebases.
