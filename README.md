## Caching Strategy: 

I have used Redis as our caching solution because it is an in-memory key-value store that is highly efficient in ensuring that cached results are retrieved very fast. Redis is best suited for tasks where instant access and low latency are important. By caching search results, one can avoid reprocessing the same queries again, which acts as a performance improvement. We chose Redis over Memcached because Redis supported more advanced data structures (like sets and hashes) which could be useful for extending the system in the future.



# Flask Document Search & News Scraper

## Overview

This web application is a **document search engine** with an integrated **news scraper**. The system scrapes news articles, allows users to search through a set of documents stored in a database, and implements user rate-limiting to control API access.

### Key Features:
- **Document Retrieval**: Search through documents stored in the database.
- **News Scraping**: Automatically scrape top news articles and display them on the homepage.
- **Rate-Limiting**: Limits each user to 5 searches per hour, returning a 429 status code when exceeded.
- **Caching**: Caches search results using Redis for faster repeated queries.
- **Background Scraping**: Continuously scrapes new news articles in the background while the app runs.


## Prerequisites

Before setting up this project, ensure you have the following installed:

- Python 3.8+
- Redis
- Docker (for containerization)
- PostgreSQL or SQLite for the database (SQLite is used by default)

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_directory>
```

2. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate 
```

3. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the SQLite database (or connect to PostgreSQL if using):

```bash
python models.py 
```

5. Add some sample documents and users to the database:

```bash
python add_data.py  
```

6. Start the Redis server (needed for caching):

```bash
redis-server
```

## Running the Application

To run the Flask application:

```bash
python app.py
```

Once running, the app will be available at:

```
http://127.0.0.1:5000
```

You can access the following features:
- **News Scraping**: Displayed on the homepage.
- **Document Search**: Enter search terms to search through the database of documents.

## Dockerization

### Step-by-Step Instructions to Dockerize the Application:

1. Build the Docker image:

```bash
docker build -t flask-app:latest .
```

2. Run the container:

```bash
docker run -d -p 5000:5000 flask-app
```

Your app will now be accessible at `http://localhost:5000`.

### Docker Compose (Optional)

If you want to run the app along with Redis using **Docker Compose**, create a `docker-compose.yml` file as outlined in the repository and run:

```bash
docker-compose up --build
```

This will spin up both the Flask app and a Redis instance.

## API Endpoints

### 1. `/` - Homepage
- Displays the **scraped news articles** and provides a **search interface** for querying documents.

### 2. `/search?text=<search_query>&user_id=<user_id>` - Search Documents
- **Method**: GET
- **Description**: Search for documents by providing a search term (`text`) and a `user_id`.
- **Rate-Limiting**: Each user can only make 5 requests per hour. Exceeding this will return a **429 Too Many Requests** error.
- **Caching**: Search results are cached to speed up repeated queries.

Example request:

```bash
curl "http://127.0.0.1:5000/search?text=AI&user_id=user_123"
```

### 3. `/health` - Health Check
- **Method**: GET
- **Description**: Check the status of the API.

Example request:

```bash
curl http://127.0.0.1:5000/health
```

Response:

```json
{
    "status": "API is up and running!"
}
