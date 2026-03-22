# app_live_news.py
import streamlit as st
import requests

st.set_page_config(page_title="Live News Fetcher", page_icon="📰")
st.title("🌐 Live News Fetcher")

st.markdown(
    "Fetch the latest headlines about **Iran, UAE, and US** using NewsAPI.org. "
    "No predictions, just live news!"
)

# Step 1: Enter your NewsAPI key
api_key = st.text_input("Enter your NewsAPI.org API key:")

# Step 2: Fetch live news using 'everything' endpoint
if api_key:
    try:
        url = f"https://newsapi.org/v2/everything?q=Iran OR UAE OR US&language=en&sortBy=publishedAt&apiKey={api_key}"
        response = requests.get(url)
        data = response.json()

        if data.get("status") != "ok":
            st.error(f"Error fetching news: {data.get('message', 'Unknown error')}")
        else:
            articles = data.get("articles", [])
            if not articles:
                st.warning("No news found. Try again later or check your API key.")
            else:
                st.success(f"Found {len(articles)} latest news headlines:")
                for i, article in enumerate(articles, 1):
                    st.write(f"{i}. 📰 [{article.get('title')}]({article.get('url')})")
    except Exception as e:
        st.error(f"An error occurred: {e}")