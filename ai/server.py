import train_jobtitle
pipe = train_jobtitle.pipe

from console_logging.console import Console
console = Console()

from sanic import Sanic
from sanic.response import json, text
app = Sanic(__name__)

@app.route('/')
async def hello(request):
    return text('', status=200)

@app.route('/predict', methods=['POST'])
async def predict(request):
    try:
        return text(str(pipe.predict([request.json['title']])[0]))
    except Exception as e:
        console.error(e)
        return text(e, status=500)

@app.route('/predict_many', methods=['POST'])
async def predict_many(request):
    try:
        return json(list(pipe.predict(request.json['titles'])))
    except Exception as e:
        console.error(e)
        return text(e, status=500)

@app.route('/log')
async def log(request):
    try:
        return text(str(train_jobtitle.get_analytics()))
    except Exception as e:
        console.error(e)
        return text(e, status=500)

console.info("Starting server...")
app.run()