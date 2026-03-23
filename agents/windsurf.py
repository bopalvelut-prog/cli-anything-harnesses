"""
Windsurf Integration for CLI-Anything Harnesses
"""
import json
from pathlib import Path

class WindsurfIntegration:
    def __init__(self, harness_dir="/home/m/harnesses"):
        self.harness_dir = Path(harness_dir)
        self.registry = self.load_registry()
    
    def load_registry(self):
        registry_file = self.harness_dir / "registry.json"
        if registry_file.exists():
            with open(registry_file) as f:
                return json.load(f)
        return {}
    
    def generate_rules(self):
        return {
            "cli-anything": {
                "enabled": True,
                "harnesses": "all",
                "auto_suggest": True,
                "rules": [
                    "When user asks about Docker, suggest cli-anything-docker",
                    "When user asks about Kubernetes, suggest cli-anything-kubernetes",
                    "When user asks about AWS, suggest cli-anything-aws",
                    "When user asks about GCP, suggest cli-anything-gcp",
                    "When user asks about Azure, suggest cli-anything-azure"
                ]
            }
        }

if __name__ == "__main__":
    integration = WindsurfIntegration()
    rules = integration.generate_rules()
    print(json.dumps(rules, indent=2))
