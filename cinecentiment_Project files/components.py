import requests

# Your unique API Key
API_KEY = "c0ffc107"

def fetch_movie_details(movie_name):
    """Fetches official movie data from OMDb API"""
    try:
        url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        
        if data.get("Response") == "True":
            return {
                "title": data.get("Title"),
                "poster": data.get("Poster"),
                "year": data.get("Year"),
                "genre": data.get("Genre"),
                "plot": data.get("Plot")
            }
    except Exception:
        return None
    return None

def header_component():
    return '<h1 class="main-title">CinemaPulse <span style="color:#ffffff; font-weight:200;">AI</span></h1>'

def review_card(sentiment, text):
    badge_class = "badge-pos" if sentiment == "positive" else "badge-neg"
    return f"""
    <div class="movie-card">
        <span class="{badge_class}">{sentiment.upper()}</span>
        <p style="margin-top:15px; color:#bdc3c7; font-style:italic; line-height:1.6; font-size:0.9rem;">
            "{text[:250]}..."
        </p>
    </div>
    """