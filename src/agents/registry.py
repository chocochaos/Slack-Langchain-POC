# A global registry for agents
AGENT_REGISTRY = {}

def register_agent(cls):
    AGENT_REGISTRY[cls.agent_name] = cls
    return cls

# Import agents to trigger registration
from .addition import AdditionAgent
from .echo import EchoAgent
from .reverse import ReverseAgent
