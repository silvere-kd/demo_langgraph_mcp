from src.agent.state import AgentState


class ChatNode:
    def __init__(self, llm):
        self.llm = llm

    async def __call__(self, state: AgentState) -> AgentState:
        messages = state['messages']

        response = await self.llm.ainvoke(messages)

        state['messages'].append(response)
        return state
