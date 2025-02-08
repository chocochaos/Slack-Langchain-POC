# A global registry for agents
AGENT_REGISTRY = {}

def register_agent(cls):
    AGENT_REGISTRY[cls.agent_name] = cls
    return cls
