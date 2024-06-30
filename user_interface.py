import gradio as gr

def gather_user_input():
    with gr.Blocks() as interface:
        gr.Markdown("Welcome to the Financial Advisory System!")
        with gr.Row():
            name = gr.Textbox(label="Name")
            age = gr.Number(label="Age")
        risk_tolerance = gr.Radio(["Low", "Medium", "High"], label="Risk Tolerance")
        investment_amount = gr.Number(label="Investment Amount ($)")

        btn = gr.Button("Get Financial Advice")
        output = gr.Textbox(label="Financial Advice", lines=10)
        strategy_output = gr.Textbox(label="Investment Strategy", lines=10)
        allocation_output = gr.Textbox(label="Optimal Allocation")
        risk_output = gr.Textbox(label="Risk Assessment")

        btn.click(fn=get_financial_advice, inputs=[name, age, risk_tolerance, investment_amount], outputs=[output, strategy_output, allocation_output, risk_output])

    interface.launch()

def get_financial_advice(name, age, risk_tolerance, investment_amount):
    # Call the orchestrator to generate advice using the user input
    from orchestrator import orchestrate
    result = orchestrate(name, age, risk_tolerance, investment_amount)  # Pass the user input to orchestrator
    return result["financial_advice"], result["investment_strategy"], result["optimal_allocation"], result["risk_assessment_results"]

user_interface_tool = FunctionTool.from_defaults(gather_user_input, name="UserInterfaceTool", description="Gather user input and preferences via a Gradio interface")
