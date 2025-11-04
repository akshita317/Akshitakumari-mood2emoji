import streamlit as st
from textblob import TextBlob
import re

# Set page config FIRST (must be first Streamlit command)
st.set_page_config(
    page_title="Mood2Emoji",
    page_icon="😀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Bad words filter (simple list for demonstration)
BAD_WORDS = ['bad', 'stupid', 'hate', 'dumb', 'idiot']  # Extend as needed

def filter_bad_words(text):
    """Check if text contains inappropriate words"""
    text_lower = text.lower()
    for word in BAD_WORDS:
        if word in text_lower:
            return True
    return False

def analyze_mood(text):
    """
    Analyze the mood of input text using TextBlob with improved logic
    Returns: emoji, explanation, polarity score
    """
    if not text.strip():
        return "😐", "Please enter some text!", 0.0
    
    # Check for inappropriate content
    if filter_bad_words(text):
        return "😐", "Let's use kind words!", 0.0
    
    # Analyze sentiment using TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    # Check for negative keywords that TextBlob might miss
    negative_keywords = ['lost', 'lose', 'losing', 'sad', 'cry', 'crying', 
                         'upset', 'angry', 'mad', 'hurt', 'pain', 'lonely',
                         'miss', 'missing', 'broke', 'broken', 'fail', 'failed',
                         'disappointed', 'terrible', 'awful', 'horrible', 'worry',
                         'scared', 'fear', 'anxious']
    
    positive_keywords = ['love', 'happy', 'joy', 'excited', 'great', 'awesome',
                         'amazing', 'wonderful', 'fantastic', 'excellent', 'best',
                         'brilliant', 'perfect', 'delightful', 'pleased', 'glad']
    
    text_lower = text.lower()
    
    # Count negative and positive keywords
    negative_count = sum(1 for word in negative_keywords if word in text_lower)
    positive_count = sum(1 for word in positive_keywords if word in text_lower)
    
    # Adjust polarity based on keyword detection
    if negative_count > positive_count and polarity > -0.1:
        polarity = -0.3  # Force negative if negative keywords dominate
    elif positive_count > negative_count and polarity < 0.1:
        polarity = 0.3   # Force positive if positive keywords dominate
    
    # Check for negations (don't, not, never, etc.)
    if any(neg in text_lower for neg in ["don't", "not", "never", "no ", "isn't", "aren't", "wasn't", "weren't", "won't", "can't"]):
        # If there's a negation and the polarity is positive, flip it
        if polarity > 0:
            polarity = -abs(polarity) * 0.8
    
    # Classify based on adjusted polarity score
    if polarity > 0.1:
        emoji = "😀"
        explanation = "Sounds happy! This sentence has positive words."
    elif polarity < -0.1:
        emoji = "😞"
        explanation = "Sounds a bit sad. This sentence has negative words."
    else:
        emoji = "😐"
        explanation = "Sounds neutral. Not too happy, not too sad."
    
    return emoji, explanation, polarity

def show_teacher_mode():
    """Display educational diagram for teachers"""
    st.markdown("### 🎓 Teacher Mode: How It Works")
    
    st.markdown("""
    #### The Mood Detection Process:
    
    ```
    1. USER INPUT
       ↓
    2. SAFETY CHECK (Filter bad words)
       ↓
    3. TEXT ANALYSIS (TextBlob analyzes words)
       ↓
    4. SENTIMENT SCORE (-1.0 to +1.0)
       ↓
    5. EMOJI ASSIGNMENT
       • Score > 0.1  → 😀 Happy
       • Score < -0.1 → 😞 Sad
       • Score ≈ 0    → 😐 Neutral
       ↓
    6. DISPLAY RESULT
    ```
    
    #### What is TextBlob?
    - A Python library that understands the emotional tone of words
    - It gives each sentence a "polarity" score from -1 (very negative) to +1 (very positive)
    - Example: "I love ice cream" = positive score ≈ +0.5
    - Example: "I don't like rain" = negative score ≈ -0.5
    
    #### How We Improved Accuracy:
    - ✅ Keyword detection for common emotional words
    - ✅ Negation handling ("don't", "not", "never")
    - ✅ Context-aware adjustments
    - ✅ Override mechanism for TextBlob limitations
    
    #### Learning Objectives:
    ✅ Understand basic sentiment analysis  
    ✅ Learn about polarity scores  
    ✅ Build interactive web apps with Streamlit  
    ✅ Implement content filtering for safety  
    ✅ Explore real-world AI applications  
    ✅ Recognize AI limitations and improvements
    """)

# Main App
def main():
    st.title("😀 Mood2Emoji Detector")
    st.markdown("### Discover the mood in your sentences!")
    st.markdown("*A kid-friendly text mood analyzer for ages 12-16*")
    
    # Sidebar
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("""
        This app analyzes the **mood** of your sentence and shows you an emoji!
        
        **How to use:**
        1. Type a sentence in the box
        2. Click 'Analyze Mood'
        3. See the emoji and explanation!
        
        **Try these examples:**
        - "I love sunny days!"
        - "I'm excited about the party"
        - "I lost my favorite book"
        - "The movie was okay"
        """)
        
        teacher_mode = st.checkbox("🎓 Teacher Mode")
    
    # Main input area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        user_input = st.text_area(
            "Enter your sentence here:",
            placeholder="Type something like 'I'm having a great day!'",
            height=100
        )
        
        analyze_button = st.button("🔍 Analyze Mood", type="primary", use_container_width=True)
    
    with col2:
        st.markdown("### Quick Examples:")
        if st.button("😀 Happy example"):
            user_input = "I love learning new things!"
            analyze_button = True
        if st.button("😞 Sad example"):
            user_input = "I lost my favorite book"
            analyze_button = True
        if st.button("😐 Neutral example"):
            user_input = "The sky is blue"
            analyze_button = True
    
    # Analysis section
    if analyze_button and user_input:
        emoji, explanation, polarity = analyze_mood(user_input)
        
        st.markdown("---")
        st.markdown("## 📊 Results")
        
        # Display result in a nice format
        result_col1, result_col2 = st.columns([1, 2])
        
        with result_col1:
            st.markdown(f"<h1 style='text-align: center; font-size: 120px;'>{emoji}</h1>", 
                       unsafe_allow_html=True)
        
        with result_col2:
            st.markdown(f"### {explanation}")
            st.markdown(f"**Your sentence:** *{user_input}*")
            
            # Show polarity score in teacher mode
            if teacher_mode:
                st.metric("Polarity Score", f"{polarity:.2f}", 
                         help="Range: -1.0 (very negative) to +1.0 (very positive)")
                
                # Visual bar for polarity
                progress_value = (polarity + 1) / 2  # Convert -1 to 1 → 0 to 1
                st.progress(progress_value)
    
    # Teacher Mode section
    if teacher_mode:
        st.markdown("---")
        show_teacher_mode()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray; font-size: 12px;'>
        Made with ❤️ for young learners By Akshita Kumari | Safe & Educational
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()