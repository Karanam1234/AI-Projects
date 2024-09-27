# pip install pyttsx3 flask


from flask import Flask, render_template, request
import pyttsx3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    if request.method == 'POST':
        input_text = request.form['text']
        
        # Initialize pyttsx3 engine
        text_speech = pyttsx3.init()

        # Convert text to speech
        text_speech.say(input_text)
        text_speech.runAndWait()
        
        return render_template('index.html', message="Text has been successfully converted to Speech.......!")

if __name__ == "__main__":
    app.run(debug=True)
