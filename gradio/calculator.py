import gradio as gr
# from foo import BAR
#


def calculator(num1, operation, num2):
    gr.Info("Starting process")
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise gr.Error("Cannot divide by zero!")
        return num1 / num2


demo = gr.Interface(
    calculator,
    [
        "number",
        gr.Radio(["add", "subtract", "multiply", "divide"]),
        "number"
    ],
    "number",
    examples=[
        [45, "add", 12],
        [3.14, "divide", 2],
        [144, "multiply", 7.5],
        [0, "subtract", 1.2],
    ],
    cache_examples=True,
    title="Toy Calculator",
    description="""Here's a sample toy calculator.
         Allows you to calculate things like $2+2=4$""",
    theme=gr.themes.Monochrome(),
    css=".gradio-container {background-color: red}",
)

demo.launch()
