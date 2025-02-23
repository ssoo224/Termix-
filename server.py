import threading
from flask import Flask

app = Flask(__name__)

def run_worker():
    while True:
        print("Worker is running...")

# تشغيل الـ Worker كـ Thread
worker_thread = threading.Thread(target=run_worker)
worker_thread.start()

@app.route('/')
def home():
    return "Worker is running in the background!"
