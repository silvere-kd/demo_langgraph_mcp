
from langgraph.graph import StateGraph, START
from langchain_core.tools import Tool
from typing import Optional, List
from src.llm.model_params import MODEL_URL, MODEL_NAME, MODEL_TEMP
from src.llm.model_provider import load_model
from src.agent.nodes import ChatNode
from src.agent.state import AgentState
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.runnables import RunnableConfig
from IPython.display import Image, display

class AgentGraph:
    def __init__(self, 
                 llm_model_url: str=MODEL_URL,
                 llm_model_name: str=MODEL_NAME,
                 ll_model_temp: float=MODEL_TEMP,
                 tools:Optional[List[Tool]]=[]):
        
        llm = load_model(llm_model_url, llm_model_name, ll_model_temp)
        self.tools = tools
        self.llm = llm.bind_tools(tools) if self.tools else llm
        self.chat_node = ChatNode(self.llm)

    def graph_builder(self):
        graph_builder = StateGraph(AgentState)

        # nodes
        graph_builder.add_node("llm", self.chat_node)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))

        # edges
        graph_builder.add_edge(START, "llm")
        graph_builder.add_conditional_edges("llm", tools_condition)
        graph_builder.add_edge("tools", "llm")

        # compile

        return graph_builder.compile()
    
    @property
    def graph(self):
        if hasattr(self, "_graph"):
            return self._graph
        self._graph = self.graph_builder()
        return self._graph
    
    def display(self):
        display(Image(self.graph.get_graph().draw_mermaid_png()))

    def invoke(self, input:str, config: Optional[RunnableConfig]=None):
        return self.graph.invoke(input, config)

    async def ainvoke(self, input:str, config: Optional[RunnableConfig]=None):
        return await self.graph.ainvoke(input, config)
