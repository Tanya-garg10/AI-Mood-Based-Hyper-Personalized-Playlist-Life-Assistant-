AI Mood-Based Hyper-Personalized Playlist & Life-Assistant 🎧🧠

A multi-agent system that detects your mood from text, generates personalized music playlists, and provides productivity and self-care recommendations — all in one place.

Project Overview

Humari daily life emotionally complex aur fast-paced hai. Users ko mood ke hisaab se music, productivity schedule, meditation aur journaling alag-alag apps me manage karna padta hai.

Solution:
A multi-agent AI system that:

Detects user mood from text input

Generates personalized playlists (Spotify / YouTube)

Suggests lifestyle actions like meditation, breaks, and affirmations

Stores mood history for personalized recommendations over time

Agents:

Agent	Task
Mood Detection	NLP-based sentiment analysis (text / voice / chat / journal)
Music Recommendation	Playlist suggestion using mood tags
Lifestyle Coach	Productivity schedule, meditation prompts, affirmations
Memory	Stores past moods for continuous personalization
Demo Screenshot / UI

Streamlit interface with:

Text input for mood/journal

Button to get suggestions

Display detected mood, recommended playlist, and lifestyle actions

Mood history from Memory Agent

Features

Multi-agent modular architecture

Real-time mood detection (demo: keyword-based; can upgrade to Gemini/GPT)

Personalized playlist suggestions (demo: static; can integrate Spotify API)

Lifestyle & productivity recommendations based on emotional state

Mood history tracking for improved personalization

Easy-to-use Streamlit interface

Tech Stack

Python 3.x – Core language

Streamlit – Web-based interactive UI

SQLite – Memory agent & mood history storage

Spotipy / YouTube API – Mood-based playlists (optional)

Gemini / GPT API – Advanced mood detection (optional)

Installation & Setup

Clone the repository:

git clone https://github.com/yourusername/AI-Mood-Life-Assistant.git
cd AI-Mood-Life-Assistant


Create and activate virtual environment:

python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

Usage

Enter your mood/journal text in the input box.

Click Get Suggestions.

View:

Detected mood

Suggested playlist

Lifestyle recommendations

Last 5 mood entries

Future Enhancements

Integrate Spotify API / YouTube API to fetch real playlists

Use Gemini or GPT API for advanced sentiment/mood detection

Integrate wearables for heart-rate-based mood detection

Add AI voice assistant for hands-free interaction

Advanced mood analytics with graphs and trends

Contributing

Contributions are welcome!

Fork the repository

Create a feature branch (git checkout -b feature-name)

Commit changes (git commit -m "Add feature")

Push to branch (git push origin feature-name)

Open a Pull Request

License

This project is open-source and available under the MIT License.
