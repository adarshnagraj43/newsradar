# NewsAPI Fetcher

This is a simple Flask application that fetches news articles using the NewsAPI and exposes an API endpoint to retrieve the news.

## Installation

1. Clone the repository:

git clone <repository_url>
cd newsapi-fetcher


2. Set up a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate


3. Install the required packages:

pip3 install -r app/requirements.txt


4. Replace `'YOUR_API_KEY'` in `app/news_fetcher.py` with your actual NewsAPI API key.

## Usage

To run the application locally, execute the following command:

``
python3 app/main.py


This will start the Flask development server and the application will be accessible at `http://localhost:8080/news`.

## API Endpoint

The application exposes a single API endpoint:

GET /news


This endpoint retrieves the latest news articles from the NewsAPI. The response is in JSON format and contains the title and source of each news article.

Example response:

```json
[
  {
    "title": "News Article 1",
    "source": "Source 1"
  },
  {
    "title": "News Article 2",
    "source": "Source 2"
  },
  ...
]

Make a GET request to http://localhost:8080/news to retrieve the news articles.

Deployment to Kubernetes
The project includes Kubernetes deployment and service configurations in the kubernetes/ directory. You can use these files to deploy the NewsAPI Fetcher application to a Kubernetes cluster.

1. Ensure you have kubectl and a running Kubernetes cluster.

2. Navigate to the kubernetes/ directory:

cd kubernetes

3. Apply the deployment and service configurations:
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

This will create a deployment and expose the application as a service in your Kubernetes cluster.

