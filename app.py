# -------------------------------
# Required Libraries
# -------------------------------
import random
import sqlite3
import datetime
from typing import List, Dict

# For Streamlit UI (optional)
import streamlit as st

# -------------------------------
# Memory Agent
# -------------------------------
class MemoryAgent:
    def __init__(self, db_name="mood_memory.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mood_history(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                mood TEXT,
                note TEXT
            )
        ''')
        self.conn.commit()

    def save_mood(self, mood, note):
        today = str(datetime.date.today())
        self.cursor.execute(
            "INSERT INTO mood_history (date, mood, note) VALUES (?, ?, ?)",
            (today, mood, note)
        )
        self.conn.commit()

    def get_history(self) -> List[Dict]:
        self.cursor.execute("SELECT * FROM mood_history")
        rows = self.cursor.fetchall()
        history = [{"id": r[0], "date": r[1], "mood": r[2], "note": r[3]} for r in rows]
        return history

# -------------------------------
# Mood Detection Agent
# -------------------------------
class MoodDetectionAgent:
    def __init__(self):
        # Placeholder for GPT/Gemini sentiment model
        self.moods = ["Happy", "Calm", "Stressed", "Demotivated", "Low Energy", "Focused"]

    def detect_mood(self, text: str) -> str:
        # Simple keyword-based detection for demo purposes
        text_lower = text.lower()
        if any(word in text_lower for word in ["tired", "thak", "late", "sleep"]):
            return "Low Energy"
        elif any(word in text_lower for word in ["stress", "panic", "worry"]):
            return "Stressed"
        elif any(word in text_lower for word in ["happy", "good", "great", "awesome"]):
            return "Happy"
        elif any(word in text_lower for word in ["focus", "concentrate", "work"]):
            return "Focused"
        elif any(word in text_lower for word in ["relax", "calm", "peace"]):
            return "Calm"
        else:
            return "Demotivated"

# -------------------------------
# Music Recommendation Agent
# -------------------------------
class MusicRecommendationAgent:
    def __init__(self):
        # Placeholder playlists
        self.playlists = {
            "Happy": ["Happy Song 1", "Happy Song 2", "Happy Song 3"],
            "Calm": ["Calm Song 1", "Calm Song 2", "Calm Song 3"],
            "Stressed": ["Relaxing Song 1", "Relaxing Song 2"],
            "Demotivated": ["Motivational Song 1", "Motivational Song 2"],
            "Low Energy": ["Soothing Song 1", "Soothing Song 2"],
            "Focused": ["Focus Music 1", "Focus Music 2"]
        }

    def recommend_playlist(self, mood: str) -> List[str]:
        return self.playlists.get(mood, ["Default Song 1", "Default Song 2"])

# -------------------------------
# Lifestyle Coach Agent
# -------------------------------
class LifestyleCoachAgent:
    def __init__(self):
        self.recommendations = {
            "Happy": ["Keep up the good work!", "Maybe take a short walk"],
            "Calm": ["Meditate for 5 mins", "Journal your thoughts"],
            "Stressed": ["Take 10 deep breaths", "Break for tea/water"],
            "Demotivated": ["Do 2 priority tasks", "Positive affirmation: You got this!"],
            "Low Energy": ["20 min power nap", "Hydrate well"],
            "Focused": ["Keep a timer for 25 min work sessions", "Avoid distractions"]
        }

    def suggest_actions(self, mood: str) -> List[str]:
        return self.recommendations.get(mood, ["Take care of yourself"])

# -------------------------------
# Multi-Agent System Coordinator
# -------------------------------
class LifeAssistant:
    def __init__(self):
        self.memory_agent = MemoryAgent()
        self.mood_agent = MoodDetectionAgent()
        self.music_agent = MusicRecommendationAgent()
        self.coach_agent = LifestyleCoachAgent()

    def process_input(self, text: str):
        # Detect Mood
        mood = self.mood_agent.detect_mood(text)
        # Save in memory
        self.memory_agent.save_mood(mood, text)
        # Recommend Music
        playlist = self.music_agent.recommend_playlist(mood)
        # Suggest Actions
        actions = self.coach_agent.suggest_actions(mood)
        return mood, playlist, actions

# -------------------------------
# Streamlit UI Demo
# -------------------------------
def main():
    st.title("🎧 AI Mood-Based Life Assistant")
    st.write("Enter your text/journal/voice input and get personalized playlist & productivity recommendations.")

    user_input = st.text_area("How are you feeling today?")
    assistant = LifeAssistant()

    if st.button("Get Suggestions"):
        mood, playlist, actions = assistant.process_input(user_input)
        st.subheader("Detected Mood:")
        st.write(f"**{mood}**")
        st.subheader("Recommended Playlist:")
        st.write(playlist)
        st.subheader("Lifestyle Recommendations:")
        st.write(actions)

        st.subheader("Mood History (Memory Agent):")
        history = assistant.memory_agent.get_history()
        for record in history[-5:]:
            st.write(f"{record['date']} - {record['mood']}: {record['note']}")

if __name__ == "__main__":
    main()
