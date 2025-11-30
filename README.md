# 🎧 AI Mood-Based Hyper-Personalized Playlist & Life-Assistant

![Python](https://img.shields.io/badge/Python-3.10+-blue) 
![Streamlit](https://img.shields.io/badge/Streamlit-v1.26-orange) 
![License](https://img.shields.io/badge/License-MIT-green)

A **multi-agent AI system** that detects your mood from text, generates personalized playlists, and provides productivity & self-care recommendations — all in one place.  

## 🔹 Project Overview

Managing mood, music, and productivity often requires multiple apps. This project solves that by providing a **single AI assistant** which:

- Detects mood from text input (journal/chat)  
- Suggests personalized music playlists (Spotify/YouTube)  
- Recommends lifestyle actions: meditation, breaks, affirmations  
- Tracks past moods for better personalization  

**Agents Used:**

| Agent | Function |
|-------|---------|
| Mood Detection | NLP-based sentiment analysis (text/journal/chat) |
| Music Recommendation | Playlist suggestions based on mood |
| Lifestyle Coach | Productivity schedule, meditation prompts, affirmations |
| Memory | Stores past moods for continuous personalization |

## 🔹 Demo Video

(https://drive.google.com/file/d/11nAeFWhV2bcW-tbqUlcQNPH9vd6jFAZR/view?usp=drive_link)  
*Streamlit interface with mood input, playlist, and recommendations.*

## 🔹 Features

- Multi-agent modular architecture  
- Real-time mood detection (keyword-based demo, can upgrade to Gemini/GPT)  
- Mood-based playlist recommendations (static demo, can integrate Spotify API)  
- Personalized lifestyle & productivity guidance  
- Mood history tracking  
- Streamlit UI for easy interaction  

## 🔹 Tech Stack

- **Python 3.10+** – Core programming language  
- **Streamlit** – Interactive UI  
- **SQLite** – Memory agent & mood history storage  
- **Spotipy / YouTube API** – Playlist integration (optional)  
- **Gemini / GPT API** – Advanced mood detection (optional)  

## 🔹 Installation

1. Clone the repo:  
```bash
git clone https://github.com/yourusername/AI-Mood-Life-Assistant.git
cd AI-Mood-Life-Assistant
````

2. Create and activate virtual environment:

```bash
python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app.py
```

## 🔹 Usage

1. Enter your mood/journal text.
2. Click **Get Suggestions**.
3. View:

   * Detected Mood
   * Suggested Playlist
   * Lifestyle Recommendations
   * Last 5 Mood Entries

## 🔹 Future Enhancements

* Spotify API / YouTube API real playlist fetch
* Gemini / GPT API for advanced sentiment analysis
* Heart-rate based mood detection via wearables
* AI voice assistant for hands-free operation
* Daily/weekly emotion trends & visualization

## 🔹 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add new feature"`
4. Push: `git push origin feature-name`
5. Open a Pull Request

## 🔹 License

This project is licensed under the MIT License.
  
