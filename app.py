from flask import Flask, jsonify
from scraper import start_scraper_thread

app = Flask(__name__)

# Start scrapper
start_scraper_thread()


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API running!"})


if __name__ == '__main__':
    app.run(debug=True)
