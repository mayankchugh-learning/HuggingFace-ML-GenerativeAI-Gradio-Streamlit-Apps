import gradio as gr
import json

def create_json(ug_hall, room_type, student_name, student_class):
    data = {
        "UG Hall": ug_hall,
        "Room Type": room_type,
        "Student Name": student_name,
        "Student Class": student_class
    }
    return json.dumps(data, indent=2)

ug_hall_options = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
room_type_options = ["Single room", "Double room", "Triple room", "Bunkbed"]

with gr.Blocks() as app:
    gr.Markdown("# HALL Selection")

    with gr.Row():
        ug_hall = gr.Dropdown(ug_hall_options, label="UG Hall")
        room_type = gr.Radio(room_type_options, label="Room Type")

    student_name = gr.Text(label="Student Name")
    student_class = gr.Text(label="Student Class")

    submit_button = gr.Button("Submit")
    output_text = gr.Textbox(label="JSON Output")

    submit_button.click(
        fn=create_json,
        inputs=[ug_hall, room_type, student_name, student_class],
        outputs=[output_text]
    )

app.launch()