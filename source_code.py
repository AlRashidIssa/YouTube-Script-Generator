from typing import Dict, List
from youtube_transcript_api import YouTubeTranscriptApi

class ConvertVideoToText:
    """
    A class to convert YouTube videos to text transcripts.

    Attributes:
        urls (List[str]): A list of YouTube video URLs.
        language_script (str): The language code for the desired transcript.

    Methods:
        extract_video_id(url: str) -> str:
            Extracts the video ID from a YouTube URL.
        convert_video_to_text() -> Dict[str, List[Dict[str, str]]]:
            Converts the videos to text transcripts.
    """

    def __init__(self, urls: List[str], language_script: str) -> None:
        """
        Constructs all the necessary attributes for the ConvertVideoToText object.

        Args:
            urls (List[str]): A list of YouTube video URLs.
            language_script (str): The language code for the desired transcript.
        """
        self.urls = urls
        self.language_script = language_script

    @staticmethod
    def extract_video_id(url: str) -> str:
        """
        Extracts the video ID from a YouTube URL.

        Args:
            url (str): The YouTube video URL.

        Returns:
            str: The extracted video ID.
        """
        if 'v=' in url:
            return url.split('v=')[1].split('&')[0]
        return url.split('/')[-1].split('?')[0]

    def convert_video_to_text(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Converts the YouTube videos to text transcripts.

        Uses the YouTube Transcript API to fetch the transcripts for the provided video URLs.

        Returns:
            Dict[str, List[Dict[str, str]]]: A dictionary where keys are video IDs and values
                                             are lists of dictionaries containing 'start' times
                                             and 'text' entries for the transcripts.
        """
        transcripts = {}
        for url in self.urls:
            video_id = self.extract_video_id(url)
            try:
                transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=[self.language_script])
                transcripts[video_id] = transcript_list
            except Exception as e:
                print(f"Could not retrieve transcript for video ID {video_id}: {str(e)}")
        return transcripts
    
# urls = ['https://www.youtube.com/watch?v=rM9BjciBLmg',
#         'https://www.youtube.com/watch?v=VSG3_JvnCkU',
#         'https://www.youtube.com/watch?v=w4FFX_otR-4']
# test = ConvertVideoToText(urls=urls, language_script='en')
# dict_script = test.convert_video_to_text()


# len(dict_script)

from typing import Dict, List

class ProcessText:
    """
    A class to process and clean transcript data.

    Attributes:
        transcripts (Dict[str, List[Dict[str, str]]]): 
            A dictionary where keys are video IDs, and values are lists of dictionaries 
            containing 'start' times and 'text' entries for the transcripts.

    Methods:
        clean_transcripts() -> str:
            Cleans the transcript text by removing newlines and stripping extra spaces 
            and returns a single string containing all the cleaned transcript texts.
    """

    def __init__(self, transcripts: Dict[str, List[Dict[str, str]]]) -> None:
        """
        Constructs all the necessary attributes for the ProcessText object.

        Args:
            transcripts (Dict[str, List[Dict[str, str]]]): 
                A dictionary of transcripts with video IDs as keys and lists of dictionaries 
                containing 'start' times and 'text' entries as values.
        """
        self.transcripts = transcripts

    def clean_transcripts(self) -> str:
        """
        Cleans the transcript text by removing newlines and stripping extra spaces.

        Iterates through the transcripts, replacing newlines with spaces and stripping 
        leading and trailing whitespace. Empty entries are excluded.

        Returns:
            str: A single string containing all the cleaned transcript texts.
        """
        cleaned_texts = []
        for transcript in self.transcripts.values():
            for entry in transcript:
                cleaned_text = entry['text'].replace('\n', ' ').strip()
                if cleaned_text:
                    cleaned_texts.append(cleaned_text)
        return ' '.join(cleaned_texts)

# # Example usage:
# # Assuming you have already defined ConvertVideoToText class and imported it
# from convert_video_to_text import ConvertVideoToText
# urls = ['https://www.youtube.com/watch?v=rM9BjciBLmg',
#         'https://www.youtube.com/watch?v=VSG3_JvnCkU',
#         'https://www.youtube.com/watch?v=w4FFX_otR-4']

# test = ConvertVideoToText(urls=urls, language_script='en')
# dict_script = test.convert_video_to_text()
# test2 = ProcessText(transcripts=dict_script)

# # Print cleaned transcript text as a single string
# cleaned_transcript_text = test2.clean_transcripts()
# print(cleaned_transcript_text)

import google.generativeai as genai
from typing import Dict, List

# Manually set your API key
GOOGLE_API_KEY = 'AIzaSyBmnV48Lgg54buSbr4Pag89NmqbeFCuZ1E'
genai.configure(api_key=GOOGLE_API_KEY)

class GenerativeScripts:
    """
    A class to generate cohesive scripts from cleaned transcripts using a generative AI model.

    Attributes:
        cleaned_scripts (Dict[str, List[Dict[str, str]]]): 
            A dictionary where keys are strings representing script names, 
            and values are lists of dictionaries containing text data.

    Methods:
        generate_sections() -> List[str]:
            Generates script sections based on the cleaned transcripts.
        
        generate_final_script() -> str:
            Generates a final cohesive script from the combined sections.
    """
    
    def __init__(self, cleaned_scripts: str) -> None:
        """
        Constructs all the necessary attributes for the GenerativeScripts object.

        Args:
            cleaned_scripts (str): 
                A string containing cleaned scripts with script names and text entries.
        """
        self.model = genai.GenerativeModel(model_name='gemini-1.5-flash')
        self.cleaned_scripts = cleaned_scripts

    def generate_sections(self) -> List[str]:
        """
        Generates script sections from the cleaned transcripts.

        Combines text entries from each script and generates a summarized section for each.

        Returns:
            List[str]: A list of generated script sections.
        """
        try:
            prompt = "Summarize the following content and generate a cohesive script: " + self.cleaned_scripts
            response = self.model.generate_content(prompt)

            return response.text # type: ignore
        except Exception as e:
            return [f"Error generating section for {str(e)}"]
        
# generative = GenerativeScripts(cleaned_scripts="")
# generate_sections = generative.generate_sections()

from flask import Flask, render_template, request
# from convert_video_to_text import ConvertVideoToText
# from process_text import ProcessText
# from generative_scripts import GenerativeScripts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    urls = request.form.get('urls').split() # type: ignore
    language_script = request.form.get('language_script')

    converter = ConvertVideoToText(urls, language_script) # type: ignore
    transcripts = converter.convert_video_to_text()

    processor = ProcessText(transcripts)
    cleaned_transcripts = processor.clean_transcripts()

    generative = GenerativeScripts(cleaned_scripts= cleaned_transcripts)
    cohesive_script = generative.generate_sections()

    return render_template('result.html', script=cohesive_script)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



"""
project/
│
├── app.py
├── fetch_transcripts.py
├── pr_process_text.py
├── generative_scripts.py
├── templates/
│   ├── index.html
│   ├── result.html
├── static/
│   ├── style.css
└── requirements.txt
"""