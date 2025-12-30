# 🔍 GitHub Profile Analyzer

A sleek web application built with Flask that analyzes any public GitHub profile using GitHub's API. Enter a GitHub username, and the app displays detailed insights like repository stats, followers, and more — all presented in a visually appealing UI.

---

## 🚀 Features

- 🔎 Analyze any GitHub profile instantly
- 📊 View repository stats, followers, and following count
- 🧑‍💻 Display total repositories, top repositories by stars
- 💬 Error handling for invalid users or API rate limits
- 💅 Modern and attractive frontend using HTML & CSS

---

## 🛠️ Tech Stack

- Backend: **Flask**
- Frontend: **HTML5**, **CSS3**, **Jinja2 Templates**
- API: **GitHub REST API**

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/github-profile-analyzer.git
   cd github-profile-analyzer

2. **Create a virtual environment (optional but recommended)**
    python -m venv venv
    source venv/bin/activate     # On Windows: venv\Scripts\activate

3. **Install dependencies**
    pip install -r requirements.txt

4. **Run the app**
    python app.py

5. **Open your browser and go to:**
     http://127.0.0.1:5000

🔐 Optional: Using GitHub Token
To avoid GitHub’s API rate limits, you can optionally provide a GitHub Personal Access Token during profile analysis.

You can generate one here: https://github.com/settings/tokens

📄 License
MIT License. Feel free to use, modify, and share.


