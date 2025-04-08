from flask import Flask, request, jsonify, redirect
import redis
import hashlib

app = Flask(__name__)

redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

BASE_URL = "http://localhost:5000/"

def generate_short_url(long_url):
    hash_object = hashlib.md5(long_url.encode())
    return hash_object.hexdigest()[:6]  

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get("long_url")
    
    # This is the updated code for the flask app
    if not long_url:
        