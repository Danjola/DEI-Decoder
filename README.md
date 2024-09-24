# DEI Decoder: Job Posting Bias Analysis Tool

## Installation:

### 1- Clone the Repository
```bash
git clone https://github.com/Ahmed-Osman-AI/DEI-Decoder.git
cd DEI-Decoder
```

### 2- Create a Conda Virtual Environment:
```bash
conda create -p venv python==3.10 -y
conda activate venv/
```

### 3- Install Dependencies:
```bash
pip install -r requirements.txt
```

### 4- Configure Environment Variables:
- Create a `.env` file in the root directory with your GROQ_API_KEY credentials:
Create account on Groq then https://console.groq.com/keys to get an API Key

```ini
GROQ_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 5- Run the Application:
```bash
streamlit run main.py
```

### 6- Access The App Interface
The application will be accessible in your web browser at http://localhost:8501.



## Usage Instructions:
1. Launch the app: After running ((streamlit run main.py)), the app will open in your browser.
2. Input job posting: You can upload .docx or .txt files, or paste job descriptions manually.
3. Analyze: Click the "Analyze Job Posting" button to review tone, bias, and discriminatory language.
4. Download Report: After analysis, you can download a detailed PDF report.