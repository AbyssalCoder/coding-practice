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

## Essential Linux Commands

```bash
# File operations
ls -la                  # List all with details
cp -r src/ dest/        # Copy directory
mv old.txt new.txt      # Rename/move
rm -rf dir/             # Remove directory
find . -name '*.py'     # Find files

# Text processing
cat file.txt            # Display file
grep -r 'pattern' .     # Search recursively
wc -l file.txt          # Count lines
head -20 file.txt       # First 20 lines
tail -f log.txt         # Follow log file

# System
ps aux                  # List processes
top                     # Process monitor
df -h                   # Disk usage
chmod 755 script.sh     # Set permissions
```

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

## Python Dictionary Practice

```python
# Word frequency counter
text = 'the cat sat on the mat the cat'
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)  # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

# Using collections.Counter
from collections import Counter
print(Counter(text.split()))
```

## File Handling in Python

```python
# Writing
with open('output.txt', 'w') as f:
    f.write('Hello, file!\n')
    f.write('Second line\n')

# Reading
with open('output.txt', 'r') as f:
    content = f.read()
    print(content)

# Reading line by line
with open('output.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

Always use `with` statements — they handle closing automatically.

## OpenCommit — AI Commit Messages

Generates meaningful commit messages from your staged changes.

### Setup
```bash
npm install -g opencommit
oco config set OCO_API_KEY=<key>
```

### Usage
```bash
git add .
oco  # generates commit message from diff
```

Follows conventional commit format. Saves time on writing descriptive messages.

## File Handling in Python

```python
# Writing
with open('output.txt', 'w') as f:
    f.write('Hello, file!\n')
    f.write('Second line\n')

# Reading
with open('output.txt', 'r') as f:
    content = f.read()
    print(content)

# Reading line by line
with open('output.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

Always use `with` statements — they handle closing automatically.

## Lovable — AI Full-Stack Builder

### Features
- Natural language to full-stack app
- Supabase integration for backend
- Real-time preview
- Git-based version control

### Observations
- Good for MVPs and prototypes
- React + Tailwind + TypeScript stack
- Better at frontend than backend logic
- Iterative refinement via chat

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

## Nested Loop — Multiplication Table

```python
for i in range(1, 6):
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')
    print('---')
```

Useful for practising nested iteration and formatting.

## Sieve of Eratosthenes

```python
def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i, v in enumerate(is_prime) if v]

print(sieve(100))
```

Efficient for generating all primes up to a limit. Runs in O(n log log n).

## Palindrome Check

```python
def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

print(is_palindrome('racecar'))  # True
print(is_palindrome('hello'))    # False
```

Slicing `[::-1]` reverses the string in one step.

## Network Monitoring Commands

```bash
# Check connectivity
ping google.com

# Trace route to host
traceroute google.com   # Linux
tracert google.com      # Windows

# View active connections
netstat -tuln
ss -tuln                # modern alternative

# DNS lookup
nslookup example.com
dig example.com

# Capture packets
tcpdump -i eth0 port 80
```

## Windsurf — Codeium's IDE

### Features
- Cascade: agentic workflow that reads, plans, and edits
- Flows: tracks your intent across multiple steps
- Fast autocomplete
- Free tier available

### Compared to Cursor
- Cascade is more autonomous than Cursor's Composer
- Windsurf feels more guided, Cursor more manual
- Both are VS Code forks
