# 😀 Mood2Emoji: Kid-Safe Text Mood Detector

A simple, interactive web application that helps students (ages 12-16) learn about sentiment analysis by detecting the mood of text and displaying kid-friendly emoji feedback.

## 🌐 Live Demo

**Try it now:** 🚀 **[https://mood2emoji-app.streamlit.app](https://mood2emoji-app.streamlit.app)**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mood2emoji-app.streamlit.app)

---

## 🎯 What This Project Does

Mood2Emoji is an educational tool that:
- Takes a sentence as input
- Analyzes the emotional tone (sentiment) of the text
- Returns an emoji (😀 😐 😞) with a simple explanation
- Filters inappropriate content to keep it kid-safe
- Includes a "Teacher Mode" to show how the technology works

## 🚀 Setup and Run Instructions

### Try Online (No Installation Required)
👉 **[Launch the app](https://mood2emoji-app.streamlit.app)** - Ready to use instantly!

### Run Locally

#### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

#### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/akshita317/Akshitakumari-mood2emoji.git
   cd Akshitakumari-mood2emoji
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download TextBlob corpora** (first time only)
   ```bash
   python -m textblob.download_corpora
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to the URL shown in the terminal

## 🧠 What Kids Learn From This Project

### Educational Value

1. **Introduction to AI & NLP**
   - Understanding how computers can "read" emotions in text
   - Basic concepts of sentiment analysis
   - Real-world applications of Natural Language Processing

2. **Computational Thinking**
   - Input → Process → Output workflow
   - How algorithms make decisions based on rules
   - Understanding polarity scores and thresholds

3. **Python Programming Concepts**
   - Using external libraries (TextBlob, Streamlit)
   - Functions and conditional logic
   - String manipulation and text processing
   - Building interactive user interfaces

4. **Digital Safety**
   - Importance of content filtering
   - Creating safe, age-appropriate applications
   - Responsible use of technology

## 📚 How to Teach This in 60 Minutes

### Lesson Structure (See lesson_plan.pdf for detailed plan)

**Phase 1: Introduction (10 min)**
- Demo the app and ask students to try different sentences
- Discuss: "How do you think the computer knows if text is happy or sad?"

**Phase 2: Concept Explanation (15 min)**
- Explain sentiment analysis with simple examples
- Show Teacher Mode diagram
- Introduce polarity scores with a visual scale

**Phase 3: Hands-on Exploration (20 min)**
- Students experiment with different sentence types
- Record observations: What makes text happy? Sad? Neutral?
- Test edge cases and safety features

**Phase 4: Code Walkthrough (10 min)**
- Walk through app.py highlighting key sections:
  - Input handling
  - TextBlob analysis
  - Emoji assignment logic
  - Safety filtering

**Phase 5: Wrap-up & Extension (5 min)**
- Discuss real-world applications (customer reviews, social media monitoring)
- Challenge: How could we improve this app?

## 🛠️ How It Works (Technical Overview)

### Core Technology

**TextBlob Library**
- Provides simple API for sentiment analysis
- Returns polarity score: -1.0 (negative) to +1.0 (positive)
- Analyzes word combinations and context

### Decision Logic

```
Input Text → Safety Check → TextBlob Analysis → Polarity Score

If polarity > 0.1:   Return 😀 "Sounds happy!"
If polarity < -0.1:  Return 😞 "Sounds a bit sad"
Else:                Return 😐 "Sounds neutral"
```

### Safety Features

- Bad word filter (simple list-based)
- Neutral fallback for flagged content
- Age-appropriate language in all responses
- No data storage or external API calls

## ⚠️ Known Limitations

1. **Simple Sentiment Analysis**
   - TextBlob uses basic pattern matching, not advanced AI
   - May not understand sarcasm or complex emotions
   - Limited to English language

2. **Basic Safety Filter**
   - Uses a simple word list (not comprehensive)
   - For production use, would need more robust content moderation

3. **No Context Memory**
   - Each sentence is analyzed independently
   - Doesn't remember previous inputs

4. **Limited Emotional Range**
   - Only three emoji categories (happy, sad, neutral)
   - Real emotions are more nuanced

5. **Polarity Threshold**
   - Fixed thresholds (±0.1) may not suit all use cases
   - Some sentences might be misclassified

## 🎓 Learning Outcomes

By the end of the lesson, students will be able to:
- ✅ Explain what sentiment analysis is and why it's useful
- ✅ Understand how polarity scores work
- ✅ Identify positive, negative, and neutral language
- ✅ Run a Python web application locally
- ✅ Recognize the importance of safety in kid-facing apps
- ✅ Think critically about AI limitations

## 🔧 Extension Ideas

For advanced students or follow-up lessons:
1. Add more emoji categories (angry, excited, confused)
2. Implement a custom word-score dictionary
3. Add a visualization showing word-by-word analysis
4. Create a "mood tracker" that saves daily sentence moods
5. Compare TextBlob with rule-based approach

## 📦 Project Structure

```
Akshitakumari-mood2emoji/
├── .streamlit/
│   └── config.toml     # Light theme configuration
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── lesson_plan.pdf    # 60-minute lesson plan for ages 12-16
```

## 🔗 Links

- **Live Demo:** [https://mood2emoji-app.streamlit.app](https://mood2emoji-app.streamlit.app)
- **GitHub Repository:** [https://github.com/akshita317/Akshitakumari-mood2emoji](https://github.com/akshita317/Akshitakumari-mood2emoji)
- **Lesson Plan:** [View PDF](https://github.com/akshita317/Akshitakumari-mood2emoji/blob/main/lesson_plan.pdf)

## 🙏 Credits & References

- **TextBlob**: [https://textblob.readthedocs.io/](https://textblob.readthedocs.io/)
- **Streamlit**: [https://streamlit.io/](https://streamlit.io/)
- **Sentiment Analysis Concept**: Introduced by researchers in computational linguistics

## 📝 License

This project is created for educational purposes as part of a curriculum development assignment.

## 📧 Contact

Created by Akshita Kumari for the Curriculum Developer Intern assignment.

**Email:** akshitasingh3027@gmail.com

---

*Built with ❤️ for young learners by Akshita Kumari*