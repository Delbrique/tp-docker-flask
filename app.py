from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Bienvenue sur Docker Flask</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                color: #fff;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }

            h1 {
                font-size: 3em;
                margin-bottom: 0.2em;
            }

            p {
                font-size: 1.5em;
                max-width: 800px;
            }

            .footer {
                position: absolute;
                bottom: 10px;
                font-size: 0.9em;
                opacity: 0.7;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Application Docker Flask</h1>
        <p>Bonjour à tous, Ceci est une simple application conteneurisée avec Docker, créée par <strong>Valentin Biyong</strong>.</p>
        <div class="footer">© 2025 - Projet d'apprentissage Docker</div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
