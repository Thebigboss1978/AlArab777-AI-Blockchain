import os
import json
import time
import subprocess
from datetime import datetime

# CONFIGURATION
REPO_PATH = "/Users/macos/AlArab777/░▒▓█𓁹█▓▒░/AlArabClub777.com-1/"
COMMAND_FILE = os.path.join(REPO_PATH, "COMMAND_BOX.json")

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 𓂀 {msg}")

def sync_to_github():
    log("Synchronizing Command Box to GitHub...")
    try:
        os.chdir(REPO_PATH)
        subprocess.run(["git", "add", "COMMAND_BOX.json"], check=True)
        subprocess.run(["git", "commit", "-m", "𓂀 Sovereign Sync: Update Command Box State"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        log("PUSH SUCCESSFUL.")
    except Exception as e:
        log(f"PUSH FAILED: {e}")

def pull_from_github():
    log("Pulling latest state from Gate...")
    try:
        os.chdir(REPO_PATH)
        subprocess.run(["git", "pull", "origin", "main", "--rebase"], check=True)
        log("PULL SUCCESSFUL.")
    except Exception as e:
        log(f"PULL FAILED: {e}")

def main():
    log("777 BRIDGE LOADED. MONITORING INTER-AGENT PULSE.")
    while True:
        # 1. Pull changes (to see what ChatGPT/Gemini did)
        pull_from_github()
        
        # 2. Update Timestamp locally to show Antigravity is ALIVE
        if os.path.exists(COMMAND_FILE):
            with open(COMMAND_FILE, 'r') as f:
                data = json.load(f)
            
            data["timestamp"] = datetime.utcnow().isoformat() + "Z"
            data["agent_sync"]["antigravity"]["status"] = "CONNECTED"
            
            with open(COMMAND_FILE, 'w') as f:
                json.dump(data, f, indent=4)
        
        # 3. Push to GitHub so everyone stays in sync
        sync_to_github()
        
        log("Sleeping for 60s... Waiting for foreign agent input.")
        time.sleep(60)

if __name__ == "__main__":
    main()
