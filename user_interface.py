from llama_index.core.tools import FunctionTool

def gather_user_input():
    # Placeholder for user input logic
    return {"name": "John Doe", "age": 40, "investment_goals": ["retirement", "college fund"], "risk_tolerance": "medium"}

user_interface_tool = FunctionTool.from_defaults(gather_user_input, name="UserInterfaceTool", description="Gather user input and preferences")
