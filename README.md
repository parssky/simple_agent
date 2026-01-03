# Simple Agent Deployment
In this repo I use Iragent package for Agent usage and also save the messages in a redis database.

### How to use it ?

Just clone the repo, then create .env file like below:

```
APP_HOST=0.0.0.0
APP_PORT=8000

BASE_URL=http://YOUR_LLM_IP:8009/v1
API_KEY=YOUR_KEY

REDIS_URI=redis://redis:6379
```
Then Just need to build the docker file like below :

```bash
docker-compose up --build
```
Then when you see the server logs, You can send request like below :

```bash
curl -X POST "http://localhost:8000/chat/session_1" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "what time is it?"  
  }'
```

And the response is like :
```json
{"response":"Of course! How can I assist you today?","history":[{"role":"user","content":"Hello, can you help me?","timestamp":"2026-01-03T15:40:52.316051"},{"role":"assistant","content":"Of course! I'm here to help. What do you need assistance with? \n\nCurrent time: 12:00 PM","timestamp":"2026-01-03T15:40:53.466771"},{"role":"user","content":"Hello, can you help me?","timestamp":"2026-01-03T15:48:46.913568"},{"role":"assistant","content":"Of course! How can I assist you today?","timestamp":"2026-01-03T15:48:48.178674"}]}
```
Agent tools:
- Agnet have acess to current date and time. You can ask about it.
Notes:

- `session_id` is just a key to save the each conversation.
http://localhost:8000/chat/{session_id}


Have fun !
