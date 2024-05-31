# YouTube Script Generator

YouTube Script Generator is a Python application developed during an internship to convert YouTube videos into text transcripts and generate cohesive scripts using generative AI models.

## Features
- **YouTube Video to Text:** Extract text transcripts from YouTube videos using the YouTube Transcript API.
- **Transcript Processing:** Clean transcripts by removing newlines and extra spaces to enhance readability.
- **Generative Script Generation:** Generate cohesive scripts from cleaned transcripts using generative AI models.

## Technologies Used
- Python
- Flask
- YouTube Transcript API
- Google's GenerativeAI

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/AlRashidIssa/YouTube-Script-Generator.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Google API key in `generative_scripts.py`.
4. Run the Flask app:
   ```bash
   python app.py
   ```

## Usage
1. Access the web interface by navigating to `http://localhost:5000` in your browser.
2. Enter YouTube video URLs and select the language script.
3. Click "Generate" to generate cohesive scripts.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the [MIT License](LICENSE).
