# LangGraph + MCP: Simple demo of how to connect LangGraph agent to an MCP server

### **Purpose**:

Our goal is to showcase how to connect LangGraph agent to an MCP server. The MCP server will expose tools for string analysis, while the client (LangGraph agent) will interact with these tools using Python subprocesses.

Here is how the system works:

 - The MCP server exposes tools to perform arithmetic operations (multiplication and subtraction).
 - The Client launches the MCP server and creates a session using standard I/O to enable communication between the LangGraph agent and the MCP tools.
 - The agent loads these tools into its session, intakes the user’s natural language input, and decides whether a tool invocation is needed.
 - If the agent detects a suitable tool is available, it calls the MCP server through the client and retrieves the result.
 - The final response is returned to the user in natural language.

### **System Architecture**:

 1. **MCP Server**: This component exposes computational tools using FastMCP.
 2. **Custom Client using StdioClient**: We’ll implement a Python client using the StdioClient to interact with the server via subprocesses.
 3. **LangGraph Agent**: We will build a custom ReAct agent using LangGraph. This agent will receive user’s input, decide whether a tool is needed, and if so, it will automatically load the appropriate tool from the MCP tools running in the connected server session.
 4. **Session Communication**: The system uses standard I/O to allow two-way communication between the LangGraph agent and the MCP server.

#### **Constraints**:

 - None


#### **Tools**:

 - Use local **ollama** model

#### **Requirements**:
 - Make it work as expected



### How to run

 - In a terminal

 ```
  git clone https://github.com/silvere-kd/demo_langgraph_mcp.git
  cd demo_langgraph_mcp
  uv run mcp_client.py
 ```

 Example outputs:

 ```
 You: Subtract 3 from 4
Processing request of type CallToolRequest
================================ System Message ================================

You are a smart assistant. For general conversation and reasoning, you may use your own thinking.
However, for the following operations, you must never calculate by yourself. Always use the tools listed below:

- multiply_numbers: Returns the product of two integers
- subtract_numbers: Returns the difference between two integers

if user asks something that requries other tool, use your own thinking and answer it.
================================ Human Message =================================

Subtract 3 from 4
================================== Ai Message ==================================
Tool Calls:
  subtract_numbers (ee3b3910-d3e1-43d9-a05d-dcb63c48035d)
 Call ID: ee3b3910-d3e1-43d9-a05d-dcb63c48035d
  Args:
    a: 4
    b: 3
================================= Tool Message =================================
Name: subtract_numbers

1
================================== Ai Message ==================================

The result of subtracting 3 from 4 is 1.
You: product of 2 and 4
Processing request of type CallToolRequest
================================ System Message ================================

You are a smart assistant. For general conversation and reasoning, you may use your own thinking.
However, for the following operations, you must never calculate by yourself. Always use the tools listed below:

- multiply_numbers: Returns the product of two integers
- subtract_numbers: Returns the difference between two integers

if user asks something that requries other tool, use your own thinking and answer it.
================================ Human Message =================================

product of 2 and 4
================================== Ai Message ==================================
Tool Calls:
  multiply_numbers (bbbc8f1f-6a17-47ee-aea8-5cddf9ecf461)
 Call ID: bbbc8f1f-6a17-47ee-aea8-5cddf9ecf461
  Args:
    a: 2
    b: 4
================================= Tool Message =================================
Name: multiply_numbers

8
================================== Ai Message ==================================

The product of 2 and 4 is 8.

 ```