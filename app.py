from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("<h1>Welcome to Mini-Spotify 🎵</h1><p>This is your mock streaming platform!</p>")

if __name__ == '__main__':
    app.run(debug=True)