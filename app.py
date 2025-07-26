# app.py (Your Flask backend file)
from flask import Flask, request, jsonify
from flask_cors import CORS # To allow requests from your frontend's domain
import spacy
import os

app = Flask(__name__)
CORS(app) # Enable CORS for cross-origin requests

# Load SpaCy model once when the app starts
# Use a try-except block to handle potential model loading errors
try:
    nlp = spacy.load("en_core_web_sm")
    print("SpaCy model 'en_core_web_sm' loaded successfully.")
except Exception as e:
    print(f"Error loading SpaCy model: {e}")
    print("Please ensure you have run 'python -m spacy download en_core_web_sm'")
    nlp = None # Set nlp to None if loading fails

# Define career categories and keywords (simplified for example)
CAREER_KEYWORDS = {
    "Technology": ["code", "software", "developer", "engineer", "data", "algorithm", "AI", "machine learning", "innovation", "programming", "web development", "cybersecurity", "IT"],
    "Creative Arts": ["art", "design", "write", "creative", "music", "film", "story", "express", "visual", "graphic", "artist", "writer", "performer"],
    "Business": ["manage", "lead", "strategy", "finance", "market", "entrepreneur", "organize", "negotiate", "sales", "consulting", "project management"],
    "Healthcare": ["health", "care", "patient", "medical", "nurse", "doctor", "therapy", "wellness", "hospital", "clinic", "diagnosis", "treatment"],
    "Science": ["research", "experiment", "discover", "biology", "chemistry", "physics", "environment", "analyze", "lab", "scientific", "astronomy", "geology"],
    "Social Services": ["help", "community", "social", "support", "educate", "non-profit", "advocate", "counseling", "psychology", "teaching", "public service"]
}

@app.route('/analyze_interests', methods=['POST'])
def analyze_interests():
    data = request.get_json()
    free_text_input = data.get('free_text_input', '')
    # quiz_answers = data.get('quiz_answers', {}) # Not used in this simplified NLP example

    suggested_career = "Explore Diverse Fields"
    description = "It seems you have a wide range of interests! Consider exploring various fields like technology, creative arts, business, or healthcare to find what truly resonates with you. Internships and informational interviews can be very helpful."

    if free_text_input and nlp:
        # --- NLP Processing using SpaCy ---
        doc = nlp(free_text_input.lower()) # Process the text

        # Initialize scores for each career
        career_scores = {career: 0 for career in CAREER_KEYWORDS}

        # Keyword matching and weighting
        for career, keywords in CAREER_KEYWORDS.items():
            for token in doc:
                if token.text in keywords:
                    career_scores[career] += 1
            # Add score for lemma (base form of word)
            for keyword in keywords:
                if nlp(keyword)[0].lemma_ in [t.lemma_ for t in doc]:
                    career_scores[career] += 0.5 # Slightly less weight for lemma match

        # You could also add more sophisticated NLP here:
        # - Named Entity Recognition (NER): doc.ents to find specific entities (e.g., "finance", "medicine")
        # - Part-of-Speech (POS) Tagging: token.pos_ to identify verbs (actions), nouns (objects)
        # - Dependency Parsing: to understand relationships between words

        # Find the career with the highest score from NLP
        if career_scores:
            max_score = -1
            best_career_matches = [] # Handle potential ties

            for career, score in career_scores.items():
                if score > max_score:
                    max_score = score
                    best_career_matches = [career]
                elif score == max_score and score > 0: # Only add to tie if score is positive
                    best_career_matches.append(career)

            if max_score > 0:
                if len(best_career_matches) == 1:
                    suggested_career = best_career_matches[0]
                    description = f"Based on your description, a career in **{suggested_career}** seems highly suitable. Your interests strongly align with this field."
                else:
                    # Handle ties by suggesting a combination or broader field
                    suggested_career = " or ".join(best_career_matches)
                    description = f"Your interests show strong alignment with multiple fields, including **{suggested_career}**. This indicates versatility and a potential for interdisciplinary roles."
            else:
                description = "Your description is interesting, but it didn't strongly align with specific career keywords. Consider exploring various fields to find what truly resonates with you."
        else:
            description = "Could not process your interests. Please try rephrasing or providing more details."
    elif not nlp:
        description = "NLP model failed to load on the server. Please check server logs."


    return jsonify({
        "suggested_career": suggested_career,
        "description": description
    })

if __name__ == '__main__':
    # Get the port from environment variable or use default 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port) # host='0.0.0.0' makes it accessible externally (useful for deployment)