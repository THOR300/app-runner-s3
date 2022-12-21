import os
from flask import Flask
from boto3 import client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BUCKET_NAME = os.environ.get("BUCKET_NAME")


@app.route("/")
def index():
    return 'Hello World from App Runner!'


@app.route("/s3talk")
def s3talk():

    conn = client('s3')
    objects = conn.list_objects(Bucket=BUCKET_NAME)['Contents']

    return "Successfully talked to s3 - found {} objects".format(len(objects))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
