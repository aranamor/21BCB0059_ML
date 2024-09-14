import redis
import json
from flask import Flask, jsonify, request
from scraper import start_scraper_thread

cache = redis.StrictRedis(host='localhost', port=6379, db=0)
app = Flask(__name__)
start_scraper_thread()


@app.route('/search', methods=['GET'])
def search():
    text = request.args.get('text', default='', type=str)
    cached_result = cache.get(text)
    if cached_result:
        return jsonify({"source": "cache", "results": json.loads(cached_result)})

    result = f"Search results for {text}"

    cache.set(text, json.dumps(result), ex=3600)  # Set expiry of 1 hour

    return jsonify({"source": "server", "results": result})


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API running!"})


if __name__ == '__main__':
    app.run(debug=True)
