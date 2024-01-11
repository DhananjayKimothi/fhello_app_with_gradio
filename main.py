from ml.ml_utils import count_words


import gradio as gr

def count_words_(sentence):
    n_words = count_words(sentence)
    return f"the number of words in the provided sentence are {n_words}", n_words

demo = gr.Interface(
    fn=count_words_,
    inputs=[gr.Textbox(label = "Please Provide an Input Sentence", lines = 3)],
    outputs=[gr.Textbox(label = "Output", lines = 3), gr.Textbox(label = "Count", lines = 1)]
)

# demo = gr.Interface(
#     fn=greet,
#     inputs=["text", "checkbox", gr.Slider(0, 100)],
#     outputs=["text", "number"],
# )
demo.launch()

# Example usage:
input_sentence = "This is a sample sentence."
word_count = count_words(input_sentence)

print(f"The number of words in the sentence is: {word_count}")