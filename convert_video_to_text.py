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