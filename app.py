from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask App - Farrel</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: white;
                padding: 40px 60px;
                border-radius: 16px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }
            h1 { color: #764ba2; }
            p  { color: #555; font-size: 18px; }
            .badge {
                background: #667eea;
                color: white;
                padding: 8px 20px;
                border-radius: 20px;
                font-size: 14px;
                margin-top: 20px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Bonjour à tous !</h1>
            <p>Ceci est une simple application conteneurisée<br>avec Docker par <strong>Nyobia Farrel</strong> !</p>
            <div class="badge">Docker + Flask + Python</div>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

