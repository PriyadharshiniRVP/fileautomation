from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return render_template('index.html', cpu=cpu_usage, ram=ram_usage, disk=disk_usage)

if __name__ == '__main__':
    app.run(debug=True)