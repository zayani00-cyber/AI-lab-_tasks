🎬 CinemaPulse AI
A Movie Sentiment Explorer
Hi! This is my project for analyzing how people feel about movies using data. Instead of just guessing, I built an app that looks at 50,000 real IMDB reviews to give you a "vibe check" on any movie you search for

What does this app do?
Imagine you want to know if a movie is actually good according to thousands of people. You type the name into my app, and it does two things:

The Visuals: It talks to the internet (using the OMDb API) to grab the official movie poster and plot summary.

The Brains: It scans my local dataset of 50,000 reviews to see how many people liked it vs. disliked it. It then calculates an "Audience Score" out of 10.

How I built it
Python: The main language I used.

Streamlit: The tool that turned my code into this cool-looking website.

Machine Learning Logic: I used "Sentiment Analysis" to help the computer understand if a review is happy or sad.

API Power: I connected the app to the OMDb database so it can show real posters for almost any movie.

Custom Design: I wrote some CSS to give it a "Dark Mode" cinema feel with glowing boxes (Glassmorphism).

What’s in the folders?
app.py: This is the heart of the project where everything is put together.

components.py: A helper file that handles the "talking" to the movie database and stores the design bits.

assets/style.css: The "paint" that makes the app look professional and dark.

IMDB Dataset.csv: The huge list of reviews the app uses to calculate scores.

requirements.txt: A simple list of tools anyone needs to install to run this on their own computer.

Since you want the README to feel more human and less like a technical manual, let's focus on "The Why" and "The How" in plain English. This version tells your teacher exactly what you were trying to achieve and how the different parts of your project work together.

Here is a simpler, more conversational version for your README.md:

🎬 CinemaPulse AI
A Movie Sentiment Explorer
Hi! This is my project for analyzing how people feel about movies using data. Instead of just guessing, I built an app that looks at 50,000 real IMDB reviews to give you a "vibe check" on any movie you search for.

🤔 What does this app do?
Imagine you want to know if a movie is actually good according to thousands of people. You type the name into my app, and it does two things:

The Visuals: It talks to the internet (using the OMDb API) to grab the official movie poster and plot summary.

The Brains: It scans my local dataset of 50,000 reviews to see how many people liked it vs. disliked it. It then calculates an "Audience Score" out of 10.

🛠️ How I built it
Python: The main language I used.

Streamlit: The tool that turned my code into this cool-looking website.

Machine Learning Logic: I used "Sentiment Analysis" to help the computer understand if a review is happy or sad.

API Power: I connected the app to the OMDb database so it can show real posters for almost any movie.

Custom Design: I wrote some CSS to give it a "Dark Mode" cinema feel with glowing boxes (Glassmorphism).

📂 What’s in the folders?
app.py: This is the heart of the project where everything is put together.

components.py: A helper file that handles the "talking" to the movie database and stores the design bits.

assets/style.css: The "paint" that makes the app look professional and dark.

IMDB Dataset.csv: The huge list of reviews the app uses to calculate scores.

requirements.txt: A simple list of tools anyone needs to install to run this on their own computer.

🚀 How to see it in action
Install the tools: pip install -r requirements.txt

Launch the app: streamlit run app.py

Type a movie like "Inception" or "Titanic" and watch it work!