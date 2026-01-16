# 🤖 AI-Powered Slack Troubleshooting Bot

An intelligent Slack bot that uses AWS Bedrock's Claude AI to provide automated troubleshooting assistance. Get instant, expert-level solutions to technical problems directly in Slack with interactive buttons for action.

## ✨ Features

- **AI-Powered Analysis**: Uses Claude 3 Haiku to analyze problems and generate solutions
- **Instant Responses**: Get 3 specific, actionable solutions in seconds
- **Interactive UI**: Slack buttons to execute fixes or escalate to humans
- **Socket Mode**: No public webhooks needed - runs behind your firewall
- **AWS Bedrock Integration**: Enterprise-grade AI with built-in security

## 🎯 Use Cases

- Database connection issues
- Server performance problems
- Application errors and bugs
- Infrastructure troubleshooting
- Configuration issues
- Deployment problems

## 📋 Prerequisites

- Python 3.8 or higher
- AWS account with Bedrock access
- Slack workspace (admin access to create apps)
- AWS credentials configured

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <repo-directory>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Slack App

#### Create Slack App
1. Go to https://api.slack.com/apps
2. Click **"Create New App"** → **"From scratch"**
3. Name your app (e.g., "TroubleshootBot")
4. Select your workspace

#### Configure Slash Command
1. Go to **"Slash Commands"** in sidebar
2. Click **"Create New Command"**
   - Command: `/troubleshoot`
   - Request URL: (not needed for Socket Mode)
   - Short Description: "Get AI-powered troubleshooting help"
   - Usage Hint: `[describe your problem]`
3. Save

#### Add OAuth Scopes
1. Go to **"OAuth & Permissions"**
2. Under **"Bot Token Scopes"**, add:
   - `chat:write` - Send messages
   - `commands` - Use slash commands
3. Click **"Install to Workspace"**
4. Copy the **Bot User OAuth Token** (starts with `xoxb-`)

#### Enable Socket Mode
1. Go to **"Socket Mode"** in sidebar
2. Enable Socket Mode
3. Under **"App-Level Tokens"**, click **"Generate Token and Scopes"**
   - Name: `socket-token`
   - Scope: `connections:write`
4. Copy the **App-Level Token** (starts with `xapp-`)

### 4. Configure AWS Bedrock

#### Enable Claude Access
1. Go to AWS Bedrock Console: https://console.aws.amazon.com/bedrock
2. Select **us-east-1** region
3. Navigate to **Playgrounds** → **Chat**
4. Select **Claude 3 Haiku** model
5. Send a test message to activate the model

#### Configure AWS Credentials
Ensure AWS credentials are configured via:
- AWS CLI: `aws configure`
- Environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`
- IAM role (if running on EC2/ECS)

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your tokens:

```env
SLACK_BOT_TOKEN=xoxb-your-bot-token-here
SLACK_APP_TOKEN=xapp-your-app-token-here
```

## 🎮 Usage

### Start the Bot

```bash
python bot.py
```

You should see: `Bolt app is running!`

### Use in Slack

In any Slack channel where the bot is added:

```
/troubleshoot Database connection timeouts in production
```

The bot will:
1. Analyze the problem using Claude AI
2. Return 3 specific, actionable solutions
3. Display interactive buttons:
   - ✅ **Try Solution #1** - Execute the suggested fix
   - ❌ **Escalate to Human** - Create a ticket for manual intervention

### Example Interaction

**User Input:**
```
/troubleshoot API returning 500 errors intermittently
```

**Bot Response:**
```
🔍 Analyzing: API returning 500 errors intermittently

Suggested solutions:
1. Check server logs for stack traces to identify the failing endpoint and error type
2. Verify database connection pool settings aren't exhausted (increase max connections)
3. Add request timeout monitoring and implement circuit breaker pattern

[✅ Try Solution #1] [❌ Escalate to Human]
```

## 📁 Project Structure

```
.
├── bot.py              # Main bot application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in git)
├── .env.example       # Environment variables template
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🔧 Configuration

### Change AI Model

To use a different Claude model, edit `bot.py`:

```python
# Claude 3 Haiku (fastest, cheapest)
modelId='anthropic.claude-3-haiku-20240307-v1:0'

# Claude 3 Sonnet (balanced)
modelId='anthropic.claude-3-sonnet-20240229-v1:0'

# Claude 3.5 Sonnet (most capable)
modelId='anthropic.claude-3-5-sonnet-20241022-v2:0'
```

### Adjust Response Length

Modify max_tokens in `bot.py`:

```python
"max_tokens": 500,  # Increase for longer responses
```

### Customize Prompt

Edit the prompt in the `ask_claude()` function to change the response format or style.

## 🐛 Troubleshooting

### Bot doesn't respond to `/troubleshoot`
- Verify Slack app is installed in workspace
- Check OAuth scopes are added (`chat:write`, `commands`)
- Ensure bot is invited to the channel: `@TroubleshootBot`

### "Access Denied" AWS Error
- Verify AWS credentials are configured
- Check IAM permissions include `bedrock:InvokeModel`
- Confirm Claude model is enabled in Bedrock (use playground once)

### Environment Variables Not Loading
- Ensure `.env` file exists in project root
- Check file is named exactly `.env` (not `.env.txt`)
- Verify `python-dotenv` is installed

### Socket Mode Connection Fails
- Verify App-Level Token starts with `xapp-`
- Check Socket Mode is enabled in Slack App settings
- Ensure `connections:write` scope is added to app token

## 🔒 Security Best Practices

- ✅ Never commit `.env` file to git
- ✅ Use IAM roles when running on AWS infrastructure
- ✅ Rotate Slack tokens regularly
- ✅ Restrict Bedrock model access via IAM policies
- ✅ Use AWS Secrets Manager for production deployments
- ✅ Implement rate limiting for Slack commands

## 📊 Cost Considerations

**AWS Bedrock (Claude 3 Haiku):**
- Input: ~$0.25 per million tokens
- Output: ~$1.25 per million tokens
- Average troubleshooting request: ~$0.001

**Slack:**
- Free for standard features
- Socket Mode: Free

**Estimated monthly cost for 1000 troubleshooting requests: ~$1-2**

## 🚀 Deployment Options

### Local Development
```bash
python bot.py
```

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "bot.py"]
```

### AWS ECS / EC2
- Use IAM roles for AWS credentials
- Store Slack tokens in AWS Secrets Manager
- Configure auto-scaling for high traffic

### Systemd Service (Linux)
```bash
sudo systemctl enable troubleshoot-bot
sudo systemctl start troubleshoot-bot
```

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

MIT License - feel free to use in commercial projects

## 🙋 Support

For issues or questions:
- Open a GitHub issue
- Check AWS Bedrock documentation: https://docs.aws.amazon.com/bedrock
- Review Slack Bolt documentation: https://slack.dev/bolt-python

## 🎉 Acknowledgments

- Built with [Slack Bolt for Python](https://slack.dev/bolt-python)
- Powered by [AWS Bedrock](https://aws.amazon.com/bedrock)
- AI by [Anthropic Claude](https://www.anthropic.com/claude)

---

**Made with ❤️ for DevOps and SRE teams**
