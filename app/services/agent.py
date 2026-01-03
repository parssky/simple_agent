from iragent.agent import AgentFactory
from iragent.message import Message
from app.core.config import settings
from app.services.prompt import AGENT_PROMPT
from iragent.tools import get_time_now

agent_factory = AgentFactory(
    base_url=settings.BASE_URL,
    api_key=settings.API_KEY,
    model="gpt-4o-mini"
)

agent = agent_factory.create_agent(
    name="test",
    system_prompt = AGENT_PROMPT,
    max_token = 2048,
    fn=[get_time_now]
)

async def run_agent(message: str) -> dict:
    msg = Message(
        content=message
    )
    res = agent.call_message(msg)
    return res.content

