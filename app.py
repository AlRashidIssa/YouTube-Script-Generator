from flask import Flask, render_template, request
from fetch_transcripts import ConvertVideoToText
from pr_process_text import ProcessText
from generative_scripts import GenerativeScripts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    urls = request.form.get('urls').split()
    language_script = request.form.get('language_script')

    converter = ConvertVideoToText(urls, language_script)
    transcripts = converter.convert_video_to_text()

    processor = ProcessText(transcripts)
    cleaned_transcripts = processor.clean_transcripts()

    generative = GenerativeScripts(cleaned_transcripts)
    cohesive_script = generative.generate_script()

    return render_template('result.html', script=cohesive_script)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

