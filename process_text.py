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
