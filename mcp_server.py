
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CalculatorTools")

@mcp.tool()
async def multiply_numbers(a: int, b: int) -> int:
    """Returns the product of two integers"""
    return a*b

@mcp.tool()
async def subtract_numbers(a: int, b: int) -> int:
    """Returns the difference between two integers"""
    return a-b

if __name__ == "__main__":
    mcp.run(transport="stdio")
