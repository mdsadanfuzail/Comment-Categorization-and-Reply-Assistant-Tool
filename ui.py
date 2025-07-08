import gradio as gr
import pandas as pd
from model import predict_and_visualize

def create_interface(model):
    with gr.Blocks() as demo:
        gr.Markdown("# Comment Categorization & Reply Assistant")

        with gr.Row():
            with gr.Column():
                input_comments = gr.Textbox(
                    label="Enter comment(s)", 
                    lines=5, 
                    placeholder="Paste one or more comments (separate by new lines)..."
                )
                upload_file = gr.File(label="Or Upload CSV (with 'comment' column)", file_types=[".csv"])
                submit_btn = gr.Button("Analyze Comments")

            with gr.Column():
                results_table = gr.Dataframe(headers=["Comment", "Category", "Response"])
                plot_output = gr.Plot()

        def handle_input(text_input, file):
            comments = []

            if file is not None:
                df = pd.read_csv(file.name)
                if 'comment' not in df.columns:
                    raise gr.Error("Uploaded CSV must contain a 'comment' column.")
                comments = df['comment'].dropna().tolist()

            elif text_input.strip():
                comments = [c.strip() for c in text_input.split("\n") if c.strip()]

            else:
                raise gr.Error("Please enter comments or upload a file.")

            return predict_and_visualize(comments, model)

        submit_btn.click(
            fn=handle_input,
            inputs=[input_comments, upload_file],
            outputs=[results_table, plot_output]
        )

    return demo
