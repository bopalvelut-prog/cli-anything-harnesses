"""
OpenCode Integration for CLI-Anything Harnesses
"""
import json
from pathlib import Path

class OpenCodeIntegration:
    def __init__(self, harness_dir="/home/m/harnesses"):
        self.harness_dir = Path(harness_dir)
        self.registry = self.load_registry()
    
    def load_registry(self):
        registry_file = self.harness_dir / "registry.json"
        if registry_file.exists():
            with open(registry_file) as f:
                return json.load(f)
        return {}
    
    def install_plugin(self):
        return {
            "plugin": "cli-anything",
            "version": "1.0.0",
            "harnesses": list(self.registry.keys()),
            "features": ["auto_complete", "context_aware", "multi_harness"]
        }
    
    def get_commands(self, harness_name):
        if harness_name in self.registry:
            return self.registry[harness_name].get("commands", [])
        return []

if __name__ == "__main__":
    integration = OpenCodeIntegration()
    plugin = integration.install_plugin()
    print(json.dumps(plugin, indent=2))
