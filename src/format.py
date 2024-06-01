import openai

class Formatter:
    def __init__(self, api_key):
        openai.api_key = api_key

    def format_notes_to_cornell(self, input_text):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Format the following academic notes into the Cornell note-taking system:\n\n{input_text}",
            max_tokens=1500
        )
        return response.choices[0].text.strip()
    
    def summarize_notes(self, input_text):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Summarize the following notes:\n\n{input_text}",
            max_tokens=1500
        )
        return response.choices[0].text.strip()
    
    def create_outline(self, input_text):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Create an outline for the following notes:\n\n{input_text}",
            max_tokens=1500
        )
        return response.choices[0].text.strip()
    
    def highlight_key_points(self, input_text):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Highlight the key points in the following notes:\n\n{input_text}",
            max_tokens=1500
        )
        return response.choices[0].text.strip()
