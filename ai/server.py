import train_jobtitle
pipe = train_jobtitle.pipe

from console_logging.console import Console
console = Console()

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    return '', 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        return str(pipe.predict([request.get_json(force=True)['title']])[0])
    except Exception as e:
        console.error(e)
        return '', 500

console.info("Starting server...")
app.run()