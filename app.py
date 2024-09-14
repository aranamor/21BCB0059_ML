from flask import Flask, render_template, jsonify, request
import redis
import json
from models import session, Document
from scraper import start_scraper_thread, news_articles

cache = redis.StrictRedis(host='localhost', port=6379, db=0)

start_scraper_thread()
app = Flask(__name__)

MAX_REQUESTS = 5
TIME_WINDOW = 3600  # rate limit


# Serve the homepage
@app.route('/')
def index():
    return render_template('index.html', articles=news_articles)


def track_user_requests(user_id):
    user_requests = cache.get(user_id)
    if user_requests:
        user_requests = int(user_requests)
        if user_requests >= MAX_REQUESTS:
            return False
        cache.incr(user_id)
    else:
        cache.setex(user_id, TIME_WINDOW, 1)
    return True


# Search
def search_documents(query):
    results = session.query(Document).filter(
        (Document.title.ilike(f'%{query}%')) | (Document.content.ilike(f'%{query}%'))
    ).all()

    return results


# Search endpoint
@app.route('/search', methods=['GET'])
def search():
    user_id = request.args.get('user_id')
    text = request.args.get('text')

    if not user_id or not text:
        return jsonify({"error": "user_id and text are required"}), 400

    if not track_user_requests(user_id):
        return jsonify({"error": "Rate limit exceeded"}), 429

    cached_result = cache.get(text)
    if cached_result:
        return jsonify({"source": "cache", "results": json.loads(cached_result)})

    documents = search_documents(text)

    results = [{"title": doc.title, "content": doc.content} for doc in documents]

    cache.setex(text, TIME_WINDOW, json.dumps(results))

    return jsonify({"source": "server", "results": results})


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is up and running!"})


if __name__ == '__main__':
    app.run(debug=True)
