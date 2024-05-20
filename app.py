import logging
from flask import Flask, jsonify, request

app = Flask(__name__)

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s'))

# Create a stream handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s'))

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b
