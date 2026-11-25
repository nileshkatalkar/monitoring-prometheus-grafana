import random
import time
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.0')


@app.route('/')
def home():
    return jsonify(message='Hello from the monitored app')


@app.route('/slow')
def slow():
    time.sleep(random.uniform(0.2, 1.5))
    return jsonify(message='That was slow')


@app.route('/error')
def error():
    return jsonify(error='Simulated failure'), 500


@app.route('/health')
def health():
    return jsonify(status='healthy')