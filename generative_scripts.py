import google.generativeai as genai
from typing import Dict, List

# Manually set your API key
GOOGLE_API_KEY = 'AIzaSyAYDLf3HqH1I1an0uPJ-3OnBCKRfCKsbZ4'
genai.configure(api_key=GOOGLE_API_KEY)

class GenerativeScripts:
    """
    A class to generate cohesive scripts from cleaned transcripts using a generative AI model.

    Attributes:
        cleaned_scripts (Dict[str, List[Dict[str, str]]]): 
            A dictionary where keys are strings representing script names, 
            and values are lists of dictionaries containing text data.

    Methods:
        generate_script() -> str:
            Generates a cohesive script based on the combined text of all cleaned transcripts.
    """
    
    def __init__(self, cleaned_scripts: Dict[str, List[Dict[str, str]]]):
        """
        Constructs all the necessary attributes for the GenerativeScripts object.

        Args:
            cleaned_scripts (Dict[str, List[Dict[str, str]]]): 
                A dictionary of cleaned scripts with script names as keys and lists of 
                dictionaries containing text entries as values.
        """
        self.cleaned_scripts = cleaned_scripts

    def generate_script(self) -> str:
        """
        Generates a cohesive script from the combined text of all cleaned transcripts.

        Combines all text entries from the cleaned scripts and sends a prompt to the 
        generative AI model to create a summarized, cohesive script.

        Returns:
            str: The generated script or an error message if script generation fails.
        """
        try:
            # Create a generative model instance
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Combine all text entries into a single string
            combined_text = " ".join([entry['text'] for transcript in self.cleaned_scripts.values() for entry in transcript])
            
            # Create a prompt for the generative model
            prompt = "Summarize the following content and generate a cohesive script: " + combined_text
            
            # Generate content using the model
            response = model.generate_content(prompt)
            
            # Return the generated script
            return response.text
        except Exception as e:
            # Return an error message in case of an exception
            return f"Error generating script: {str(e)}"
