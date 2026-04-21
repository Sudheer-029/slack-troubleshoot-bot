# AI Troubleshoot Bot — Human-in-the-Loop Incident Response

> Built in **24 hours**. Production-style AI incident response system that brings human oversight to autonomous troubleshooting.

An AI-powered Slack bot that helps engineering teams resolve incidents faster — with Claude AI suggesting fixes and humans staying in control of execution.

---

## The Flow

```
Engineer types: /troubleshoot [describe the issue]
                        ?
         Claude AI (via Amazon Bedrock) analyzes the issue
                        ?
         AI returns 3 ranked fix suggestions with reasoning
                        ?
              Human reviews and chooses:
         +--------------------------------+
       Approve    Reject    Escalate
         ?                      ?
    Bot executes         On-call engineer
      the fix             gets notified
```

---

## Why Human-in-the-Loop?

Fully autonomous incident response is risky in production. This architecture gives you the speed of AI analysis with the safety of human judgment before any action is taken.

- AI handles the cognitive load of diagnosis and option generation
- Human retains decision authority on execution
- Every incident and resolution is logged — builds institutional knowledge over time
- Scales senior engineering judgment across the entire team

---

## Tech Stack

| Component | Technology |
|---|---|
| AI Model | Claude Sonnet via Amazon Bedrock |
| Bot Framework | Slack Bolt API (Python) |
| Language | Python |
| Architecture | Human-in-the-loop (HITL) |

---

## Setup

```bash
git clone https://github.com/Sudheer-029/slack-troubleshoot-bot.git
cd slack-troubleshoot-bot
pip install -r requirements.txt
```

Create a `.env` file:
```
SLACK_BOT_TOKEN=your_slack_bot_token
SLACK_SIGNING_SECRET=your_signing_secret
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_REGION=us-east-1
```

Run the bot:
```bash
python app.py
```

---

## Business Impact

- Reduces **Mean Time To Resolution (MTTR)** by surfacing fixes instantly
- Eliminates context-switching — engineers stay in Slack
- Captures institutional knowledge on every incident
- Safe for production — no autonomous execution without human approval

---

## Key Concepts Demonstrated

- Agentic AI with human oversight
- AWS Bedrock (Claude Sonnet) integration
- Slack Bolt API event handling
- Production-grade bot architecture
- Responsible AI design (HITL pattern)
