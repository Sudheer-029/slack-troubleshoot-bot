from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import boto3
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Slack app
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# Initialize Bedrock
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

def ask_claude(problem):
    """Ask Claude to troubleshoot"""
    prompt = f"""You're a senior engineer. A user reports: "{problem}"
    
Provide exactly 3 possible solutions, numbered 1-3.
Be specific and actionable. Keep each solution to 1-2 sentences.

Format:
1. [Solution]
2. [Solution]  
3. [Solution]"""

    response = bedrock.invoke_model(
        modelId='anthropic.claude-3-haiku-20240307-v1:0',
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 500,
            "messages": [{"role": "user", "content": prompt}]
        })
    )
    
    return json.loads(response['body'].read())['content'][0]['text']

@app.command("/troubleshoot")
def troubleshoot(ack, command, say):
    """Handle /troubleshoot command"""
    ack()  # Acknowledge command
    
    problem = command['text']
    
    # Ask Claude
    solutions = ask_claude(problem)
    
    # Send to Slack with buttons
    say(
        text=f"Analyzing: {problem}",  # Fallback text for notifications
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"🔍 *Analyzing:* {problem}"}
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*Suggested solutions:*\n{solutions}"}
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "✅ Try Solution #1"},
                        "value": "solution_1",
                        "action_id": "execute_fix"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "❌ Escalate to Human"},
                        "value": "escalate",
                        "action_id": "escalate"
                    }
                ]
            }
        ]
    )

@app.action("execute_fix")
def handle_execute(ack, action, say):
    """When user clicks 'Try Solution'"""
    ack()
    say("🤖 Executing fix... (In production, this would run the actual fix)")
    say("✅ Fix applied successfully! Monitoring for 5 minutes...")

@app.action("escalate")
def handle_escalate(ack, action, say):
    """When user clicks 'Escalate'"""
    ack()
    say("📢 Escalated to on-call engineer. Ticket created: #12345")

if __name__ == "__main__":
    # Start the app
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
