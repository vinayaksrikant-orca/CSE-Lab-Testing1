import os
import requests

# 1. AWS Access Key (Matches Regex Pattern: AKIA + 16 alphanumeric)
# This is the most common trigger for all scanners.
AWS_ACCESS_KEY = "AKIA3F7D3E2B1A6C4D8E"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# 2. GitHub Personal Access Token (Matches Pattern: ghp_)
# Modern GitHub tokens have a specific prefix to make them 100% identifiable.
GITHUB_TOKEN = "ghp_n0tARealT0k3nJustF0rScann3rT3st1ng12345"

# 3. Stripe Secret Key (Matches Pattern: sk_live_)
STRIPE_API_KEY = "sk_live_51P8p0mF9z9z9z9z9z9z9z9z9z9z9z9"

ALGOLIA_APP_ID = "latency"
ALGOLIA_ADMIN_API_KEY = "d1d2d3d4d5d6d7d8d9d0dadbdcdddeef"

# 4. Google Cloud Service Account Key (High Entropy JSON)
# Scanners look for the "private_key" field inside a JSON structure.
GCP_SA_KEY = {
  "type": "service_account",
  "project_id": "deep-sea-research",
  "private_key_id": "b080eeee840b4b24",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDe7pX...\n-----END PRIVATE KEY-----\n",
  "client_email": "infiltrator@deep-sea-research.iam.gserviceaccount.com"
}

# 5. Slack Incoming Webhook (Matches known URL structure)
SLACK_WEBHOOK = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# 6. Generic Database Connection String (Contains password in URL)
# Scanners flag the 'password' portion of the URI.
DB_CONN = "postgresql://marine_admin:CorrectHorseBatteryStaple123!@db.phantomfish.net:5432/research_data"

def deploy():
    print(f"Deploying to frequency: {os.environ.get('BEACON_FREQUENCY')}")
    # Using the hardcoded token to 'whisper' back to the command center
    response = requests.get("https://api.github.com/user", headers={"Authorization": f"token {GITHUB_TOKEN}"})
    return response.status_code

if __name__ == "__main__":
    deploy()
