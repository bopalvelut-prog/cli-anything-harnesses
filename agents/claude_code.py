"""
Claude Code Integration for CLI-Anything Harnesses
"""
import subprocess
import json
import os
from pathlib import Path

class ClaudeCodeIntegration:
    def __init__(self, harness_dir="/home/m/harnesses"):
        self.harness_dir = Path(harness_dir)
        self.registry = self.load_registry()
    
    def load_registry(self):
        registry_file = self.harness_dir / "registry.json"
        if registry_file.exists():
            with open(registry_file) as f:
                return json.load(f)
        return {}
    
    def list_harnesses(self):
        return list(self.registry.keys())
    
    def get_harness_commands(self, harness_name):
        if harness_name in self.registry:
            return self.registry[harness_name].get("commands", [])
        return []
    
    def execute(self, harness_name, command, args=None):
        if harness_name not in self.registry:
            return {"error": f"Harness {harness_name} not found"}
        pkg = self.registry[harness_name]["package"]
        cli = self.registry[harness_name]["cli"]
        cmd = [cli, command]
        if args:
            cmd.extend(args)
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            return {"stdout": result.stdout, "stderr": result.stderr, "returncode": result.returncode}
        except Exception as e:
            return {"error": str(e)}
    
    def suggest_harness(self, context):
        suggestions = []
        context_lower = context.lower()
        for name in self.registry:
            if name in context_lower:
                suggestions.append({"name": name, "package": self.registry[name]["package"], "commands": self.registry[name].get("commands", [])})
        return suggestions[:5]
    
    def auto_install(self, harness_name):
        try:
            subprocess.run(["pip", "install", f"cli-anything-{harness_name}"], capture_output=True, check=True)
            return {"success": True, "message": f"Installed {harness_name}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_completions(self, partial_input):
        completions = []
        words = partial_input.split()
        if not words:
            return [h for h in self.registry.keys() if h.startswith("cli-anything")]
        if words[0] == "cli-anything":
            if len(words) == 1:
                return [f"cli-anything-{h}" for h in self.registry.keys()]
            elif len(words) == 2:
                harness = words[1].replace("cli-anything-", "")
                if harness in self.registry:
                    return [f"{words[1]} {cmd}" for cmd in self.registry[harness].get("commands", [])]
        return completions

if __name__ == "__main__":
    integration = ClaudeCodeIntegration()
    print(f"Available harnesses: {len(integration.list_harnesses())}")
    print(f"Sample: {integration.list_harnesses()[:10]}")
