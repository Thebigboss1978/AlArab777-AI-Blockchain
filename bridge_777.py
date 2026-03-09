import os
import json
import time
import subprocess
from datetime import datetime

# CONFIGURATION - PUBLIC SYNC HUB
REPO_PATH = "/Users/macos/Sovereign-Matrix-777"
COMMAND_FILE = os.path.join(REPO_PATH, "COMMAND_BOX.json")

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 𓂀 {msg}")

def sync_to_github():
    log("Synchronizing Command Box to PUBLIC GATE...")
    try:
        os.chdir(REPO_PATH)
        subprocess.run(["git", "add", "COMMAND_BOX.json"], check=True)
        subprocess.run(["git", "commit", "-m", "𓂀 Sovereign Sync: Shared Brain Update"], check=True)
        subprocess.run(["git", "push", "public", "main", "-f"], check=True)
        log("PUSH SUCCESSFUL.")
    except Exception as e:
        log(f"PUSH FAILED: {e}")

def pull_from_github():
    log("Pulling latest state from Public Gate...")
    try:
        os.chdir(REPO_PATH)
        subprocess.run(["git", "pull", "public", "main", "--rebase"], check=True)
        log("PULL SUCCESSFUL.")
    except Exception as e:
        log(f"PULL FAILED: {e}")

def main():
    log("777 PUBLIC BRIDGE ACTIVE. MONITORING SOVEREIGN HUB.")
    while True:
        # 1. Pull changes (to see what other local processes did)
        pull_from_github()
        
        # 2. Check for External Agent Input (The Tunnel)
        INPUT_TUNNEL = os.path.join(REPO_PATH, "AGENT_INPUT_TUNNEL.json")
        if os.path.exists(INPUT_TUNNEL):
            with open(INPUT_TUNNEL, 'r') as f:
                input_data = json.load(f)
            
            if input_data.get("content") != "PASTE_AGENT_RESPONSE_HERE":
                log("DETECTED EXTERNAL AGENT DATA IN TUNNEL!")
                with open(COMMAND_FILE, 'r') as f:
                    main_box = json.load(f)
                
                # Merge logic
                new_entry = f"{datetime.now().isoformat()} - {input_data['agent_id']}: {input_data['content'][:50]}..."
                main_box["command_history"].append(new_entry)
                agent_key = input_data['agent_id'].lower()
                if agent_key in main_box["agent_sync"]:
                    main_box["agent_sync"][agent_key]["status"] = "SYNCED"
                    main_box["agent_sync"][agent_key]["last_message"] = input_data["content"]
                
                # Update Master Box
                with open(COMMAND_FILE, 'w') as f:
                    json.dump(main_box, f, indent=4)
                
                # Reset Tunnel
                input_data["content"] = "PASTE_AGENT_RESPONSE_HERE"
                with open(INPUT_TUNNEL, 'w') as f:
                    json.dump(input_data, f, indent=4)
                log("MERGE COMPLETE. PREPARING BROADCAST.")

        # 3. Update Timestamp locally
        if os.path.exists(COMMAND_FILE):
            with open(COMMAND_FILE, 'r') as f:
                data = json.load(f)
            data["timestamp"] = datetime.now().isoformat() + "Z"
            # The original line `data["agent_sync"]["antigravity"]["status"] = "CONNECTED"` is removed as per instruction
            with open(COMMAND_FILE, 'w') as f:
                json.dump(data, f, indent=4)
        
        # 4. Push to Public Gate
        sync_to_github()
        log("Waiting for Inter-Agent response (60s)...")
        time.sleep(60)

if __name__ == "__main__":
    main()
