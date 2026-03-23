# CLI-Anything Agent Integration

## Supported AI Coding Agents

### Claude Code
```bash
# Install all harnesses
source /home/m/apps/bin/activate
pip install cli-anything-*

# Use in Claude Code
claude code --help  # Shows all available harnesses
claude code cli-anything-docker status
claude code cli-anything-kubernetes pods
```

### Cursor
```json
// .cursorrules
{
  "cli-anything": {
    "enabled": true,
    "harnesses": ["docker", "kubernetes", "aws", "gcp", "azure"],
    "auto_install": true
  }
}
```

### GitHub Copilot
```yaml
# .github/copilot-cli.yml
cli-anything:
  harnesses:
    - docker
    - kubernetes
    - terraform
    - ansible
  integration:
    auto_complete: true
    context_aware: true
```

### OpenCode
```bash
# Install OpenCode integration
opencode plugin install cli-anything

# Configure
opencode config set cli-anything.harnesses "docker,kubernetes,aws,gcp,azure"
opencode config set cli-anything.auto_install true
```

### Windsurf
```json
// .windsurfrules
{
  "cli-anything": {
    "enabled": true,
    "harnesses": "all",
    "auto_suggest": true
  }
}
```

### Continue.dev
```yaml
# config.yaml
cli-anything:
  enabled: true
  harnesses: all
  integration:
    code_completion: true
    inline_suggestions: true
```

## Installation

```bash
# Clone the repo
git clone https://github.com/bopalvelut-prog/cli-anything-harnesses.git
cd cli-anything-harnesses

# Install all harnesses
source /home/m/apps/bin/activate
for dir in */; do
  if [ -f "$dir/setup.py" ]; then
    pip install -e "$dir" 2>/dev/null || true
  fi
done

# Or install specific harnesses
pip install cli-anything-docker cli-anything-kubernetes cli-anything-aws
```

## Usage

```bash
# List all harnesses
cli-anything --list

# Get help for a specific harness
cli-anything-docker --help
cli-anything-kubernetes --help

# Run commands
cli-anything-docker status
cli-anything-kubernetes pods
cli-anything-aws s3 ls
```

## Agent-Specific Features

### Claude Code
- Full CLI autocomplete
- Context-aware suggestions
- Multi-harness orchestration
- Auto-install missing harnesses

### Cursor
- Inline CLI suggestions
- Real-time command completion
- Integration with cursor rules
- Auto-discovery of harnesses

### GitHub Copilot
- CLI command suggestions
- Context-aware completions
- Integration with GitHub Actions
- Auto-configuration

### OpenCode
- Plugin system integration
- Custom harness generation
- Real-time CLI assistance
- Multi-agent support

### Windsurf
- Rule-based integration
- Auto-harness discovery
- Context-aware suggestions
- Custom harness creation

## Advanced Configuration

```json
{
  "cli-anything": {
    "version": "1.0.0",
    "harnesses": {
      "enabled": ["docker", "kubernetes", "aws", "gcp", "azure"],
      "disabled": ["bitcoin", "ethereum"],
      "auto_install": true,
      "update_on_startup": true
    },
    "integration": {
      "claude_code": { "enabled": true, "auto_complete": true },
      "cursor": { "enabled": true, "inline_suggestions": true },
      "copilot": { "enabled": true, "context_aware": true },
      "opencode": { "enabled": true, "plugin_system": true },
      "windsurf": { "enabled": true, "rules_based": true }
    },
    "features": {
      "auto_discovery": true,
      "context_aware": true,
      "multi_harness": true,
      "custom_harnesses": true
    }
  }
}
```
