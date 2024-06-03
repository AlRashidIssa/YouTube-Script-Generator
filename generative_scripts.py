import google.generativeai as genai
from typing import Dict, List

# Manually set your API key
GOOGLE_API_KEY = 'Your_key_API'
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
