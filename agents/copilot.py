"""
GitHub Copilot Integration for CLI-Anything Harnesses
"""
import json
from pathlib import Path

class CopilotIntegration:
    def __init__(self, harness_dir="/home/m/harnesses"):
        self.harness_dir = Path(harness_dir)
        self.registry = self.load_registry()
    
    def load_registry(self):
        registry_file = self.harness_dir / "registry.json"
        if registry_file.exists():
            with open(registry_file) as f:
                return json.load(f)
        return {}
    
    def generate_copilot_config(self):
        config = {
            "cli-anything": {
                "harnesses": list(self.registry.keys())[:50],
                "integration": {
                    "auto_complete": True,
                    "context_aware": True,
                    "github_actions": True
                }
            }
        }
        return config
    
    def suggest_commands(self, context):
        suggestions = []
        for name in self.registry:
            if name in context.lower():
                for cmd in self.registry[name].get("commands", []):
                    suggestions.append(f"cli-anything-{name} {cmd}")
        return suggestions[:5]

if __name__ == "__main__":
    integration = CopilotIntegration()
    config = integration.generate_copilot_config()
    print(json.dumps(config, indent=2))
