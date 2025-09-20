# Reddit Content Research Agent

A lightweight agent designed to research and analyze Reddit content using LLMs, SERP APIs, and webhook-based background tasks. This project integrates **Bright Data SERP API**, **Google Gemini LLM**, **LangChain**, **Django**, **Celery**, and **Django-QStash** to automate content discovery, analysis, and asynchronous processing.

---

## 📂 Project Structure

```
.
├── data/                        # Stored data from scraped Reddit threads
├── nbs/                         # Jupyter notebooks for experimentation
│   ├── 01-Init.ipynb
│   ├── 02-serp-api-init.ipynb
│   ├── 03-google-gemini-llm-langchain.ipynb
│   ├── ... (other notebooks)
│   └── setup.py
├── src/
│   ├── blog/                     # Django app for testing Celery & webhook tasks
│   │   ├── tasks.py              # Celery & QStash tasks
│   │   ├── views.py              # Webhook endpoints
│   │   └── ... (other Django files)
│   ├── ResearchAgent/            # Main Django project
│   │   ├── settings.py           # Includes QStash and Celery configs
│   │   ├── celery.py             # Celery configuration
│   │   └── ... (other Django files)
│   └── manage.py
├── .env                          # Environment variables
├── .env.example                  # Template for environment variables
├── compose.yaml                   # Docker-compose for Redis and other services
├── requirements.txt               # Python dependencies
├── rav.yaml                       # Project scripts (runserver, ngrok, Celery, etc.)
└── README.md
```

---

## 🚀 Features

* 🔎 **Search Automation:** Uses Bright Data SERP API for search queries.
* 🤖 **LLM Integration:** Google Gemini LLM with LangChain for intelligent responses.
* 🧩 **Tool Calling:** Demonstrates manual and automated LLM tool usage.
* 🧱 **Structured Output:** Pydantic for clean, validated data formats.
* ⚡ **Asynchronous Webhooks:** Django-QStash + Celery for reliable webhook processing.
* 🌐 **Local Testing:** Ngrok for exposing local Django server endpoints to the internet.

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Reddit-Content-Research-Agent.git
cd Reddit-Content-Research-Agent
```

2. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure environment variables (`.env`) including:

```
DJANGO_DEBUG=1
DJANGO_SECRET_KEY=<your_django_secret_key>
DATABASE_URL=postgres://pguser:pgpassword@localhost:5433/pgdb
REDIS_URL="redis://localhost:6380/0"
BRIGHT_DATA_SERP_API_KEY=<your_bright_data_key>
GOOGLE_GEMINI_API_KEY=<your_gemini_key>
QSTASH_TOKEN=<your_qstash_token>
CSRF_TRUSTED_ORIGINS=<ngrok_https_url>
ALLOWED_HOSTS=<ngrok_domain>
```

---

## ▶️ Usage

### 1. Jupyter Notebooks

```bash
rav run notebook
```

* Open notebooks in `nbs/` and run them step-by-step to validate API integrations and experiment with LLM tool calls.

### 2. Django & Celery

```bash
rav run runserver      # Start Django server on localhost:8000
rav run worker         # Start Celery worker for background tasks
```

* Make sure **Redis** is running:

```bash
rav run docker_up      # Start Redis via Docker
```

### 3. Ngrok for Webhooks

```bash
rav run ngrok          # Expose local server to the internet
```

* Copy the **HTTPS forwarding URL** and use it as your webhook endpoint (e.g., Stripe, Razorpay).
* Example webhook URL:

```
https://abcd-1234.ngrok-free.app/blog/webhook/
```

---

## 📌 Webhook & Background Tasks

**Example Webhook Endpoint (`blog/views.py`):**

```python
from django.http import HttpResponse
from django_qstash.decorators import qstash_signed
from .tasks import process_payment_task

@qstash_signed
def stripe_webhook(request):
    process_payment_task.delay(request.json())
    return HttpResponse("Webhook received")
```

**Example Background Task (`blog/tasks.py`):**

```python
from celery import shared_task

@shared_task
def process_payment_task(data):
    print(f"Processing webhook data: {data}")
```

* `@qstash_signed` ensures that only QStash-sent requests are accepted.
* Celery handles heavy processing asynchronously so webhook returns immediately.

---

## 📌 Notes

* Free-tier **ngrok URLs change every session** → update `CSRF_TRUSTED_ORIGINS` and `ALLOWED_HOSTS`.
* QStash provides **reliable, signed delivery** of webhook tasks.
* Pre-commit hooks are included to maintain code formatting:

```bash
rav run clean
```