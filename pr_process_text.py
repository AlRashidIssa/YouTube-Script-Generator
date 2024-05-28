from typing import List, Dict

class ProcessText:
    """
    A class to process and clean transcript data.

    Attributes:
        transcripts (Dict[str, List[Dict[str, str]]]): 
            A dictionary where keys are video IDs, and values are lists of dictionaries 
            containing 'start' times and 'text' entries for the transcripts.

    Methods:
        clean_transcripts() -> Dict[str, List[Dict[str, str]]]:
            Cleans the transcript text by removing newlines and stripping extra spaces.
    """
    
    def __init__(self, transcripts: Dict[str, List[Dict[str, str]]]) -> None:
        """
        Constructs all the necessary attributes for the Pr_ProcessText object.

        Args:
            transcripts (Dict[str, List[Dict[str, str]]]): 
                A dictionary of transcripts with video IDs as keys and lists of dictionaries 
                containing 'start' times and 'text' entries as values.
        """
        self.transcripts = transcripts

    def clean_transcripts(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Cleans the transcript text by removing newlines and stripping extra spaces.

        Iterates through the transcripts, replacing newlines with spaces and stripping 
        leading and trailing whitespace. Empty entries are excluded.

        Returns:
            Dict[str, List[Dict[str, str]]]: 
                A dictionary with the same structure as the input transcripts, but with 
                cleaned text entries.
        """
        cleaned_transcripts = {}
        for video_id, transcript in self.transcripts.items():
            cleaned_transcript = []
            for entry in transcript:
                cleaned_text = entry['text'].replace('\n', ' ').strip()
                if cleaned_text:
                    cleaned_transcript.append({'start': entry['start'], 'text': cleaned_text})
            cleaned_transcripts[video_id] = cleaned_transcript
        return cleaned_transcripts
