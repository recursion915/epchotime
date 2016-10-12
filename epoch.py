#!/usr/bin/env python3
import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def epcho_time():
        return 'The epcho time in secs is ' + str(time.time()) + ' s'

if __name__ == "__main__":
    app.run()
