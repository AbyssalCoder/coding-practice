## Roo Code — Fork of Cline

Enhanced fork with additional features.

### Differences from Cline
- Multiple modes (Code, Architect, Debug)
- Custom modes with specific instructions
- Better context management
- Community-driven development

### Setup
Install from VS Code marketplace → Search "Roo Code"

## Bolt.new — Full-Stack App Generator

Browser-based AI that generates and deploys full-stack apps.

### Strengths
- Generates complete projects (frontend + backend)
- Deploys instantly
- Uses WebContainers (runs Node.js in browser)
- Great for prototyping

### Limitations
- Can struggle with complex requirements
- Limited backend options
- Code quality varies

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


<!-- fixed typo -->

## Cline — Autonomous Coding Agent for VS Code

### Features
- Creates and edits files autonomously
- Runs terminal commands
- Asks for approval before actions
- Uses browser for testing

### Observations
- Very capable but can be expensive (high token usage)
- Good at building full features end-to-end
- Works with Claude, GPT-4, and other models
- Human-in-the-loop design (approve/reject each action)
