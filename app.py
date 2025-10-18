from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Fake data generator (in real use you'd scrape or import your own list)
def generate_fake_users(count=200):
    users = []
    for i in range(count):
        followers = random.randint(100, 20000)
        following = followers + random.randint(-5000, 5000)
        username = f"user_{i}"
        users.append({
            "username": username,
            "followers": followers,
            "following": following,
            "ratio": round(following / max(followers, 1), 2)
        })
    return users


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run")
def run_bot():
    all_users = generate_fake_users()
    # keep users whose following ≥ followers or roughly equal
    selected = [u for u in all_users if u["following"] >= 0.9 * u["followers"]]
    # Sort by ratio, descending
    selected.sort(key=lambda x: x["ratio"], reverse=True)
    return jsonify(selected)


if __name__ == "__main__":
    app.run(debug=True)
