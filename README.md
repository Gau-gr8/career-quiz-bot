# Career Explorer Quiz Bot

## Project Overview
This is a web-based interactive quiz designed to help users get personalized career suggestions. It leverages a multi-choice question system and integrates Natural Language Processing (NLP) to analyze free-form text input for more nuanced feedback.

The project is split into a frontend (what you see in the browser) and a powerful Python backend (that processes your answers and interests).

## Technologies Used

### Frontend
* **HTML5:** For the structure and content of the web page.
* **CSS (Tailwind CSS):** For modern, responsive styling and layout.
* **JavaScript:** Powers the quiz logic, question navigation, and handles communication with the backend.

### Backend
* **Python:** The core language for the server-side logic.
* **Flask:** A lightweight web framework used to create the API endpoint that the frontend communicates with.
* **SpaCy:** A highly efficient library for Natural Language Processing, used to analyze the user's free-form text input and generate career suggestions.

## Features
* **Interactive Multi-Choice Questions:** Guides users through a series of questions to understand their preferences.
* **NLP-Powered Free-Form Input:** Allows users to describe their interests in their own words for more personalized career suggestions.
* **Personalized Career Feedback:** Provides detailed suggestions based on a combination of quiz answers and NLP analysis.
* **Responsive Web Interface:** Designed to look good on various screen sizes (desktops, tablets, mobile).

## Setup and Running the Project

To run this project locally, follow these steps:

### 1. Clone the Repository
First, get a copy of this project onto your local machine:
```bash
git clone [https://github.com/Gau-gr8/career-quiz-bot.git](https://github.com/Gau-gr8/career-quiz-bot.git)
cd career-quiz-bot
```
### 2. Backend Setup(Python) 

# Create a virtual environment (recommended for dependency isolation)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install Flask spacy

# Download the SpaCy English language model
python -m spacy download en_core_web_sm

# Run the Flask backend server
python app.py


The Flask server will typically start on http://127.0.0.1:5000. Keep this terminal window open while you use the quiz.

### 3. Frontend Usage
The frontend is a simple HTML file. You can open it directly in your web browser:

Navigate to the career-quiz-bot folder on your computer.

Double-click on index.html.

Your browser will open the quiz. When you interact with the quiz, the JavaScript in index.html will communicate with the Python backend you started in step 2.

Contributing
If you'd like to contribute to this project, please feel free to fork the repository and submit pull requests.
