"""
Cursor Integration for CLI-Anything Harnesses
"""
import json
from pathlib import Path

class CursorIntegration:
    def __init__(self, harness_dir="/home/m/harnesses"):
        self.harness_dir = Path(harness_dir)
        self.registry = self.load_registry()
    
    def load_registry(self):
        registry_file = self.harness_dir / "registry.json"
        if registry_file.exists():
            with open(registry_file) as f:
                return json.load(f)
        return {}
    
    def generate_cursor_rules(self):
        rules = {
            "cli-anything": {
                "enabled": True,
                "harnesses": list(self.registry.keys())[:100],
                "auto_install": True,
                "context_aware": True
            }
        }
        return rules
    
    def inline_suggestions(self, context):
        suggestions = []
        context_lower = context.lower()
        for name in self.registry:
            if name in context_lower:
                pkg = self.registry[name]["package"]
                suggestions.append(f"cli-anything-{name}")
        return suggestions[:3]

if __name__ == "__main__":
    integration = CursorIntegration()
    rules = integration.generate_cursor_rules()
    print(json.dumps(rules, indent=2))
