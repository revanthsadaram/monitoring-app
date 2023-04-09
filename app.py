import psutil   #To retrive CPU and memory utilization of my server
from flask import Flask, render_template #web-development framework in python

app = Flask(__name__)

@app.route("/")
def index():    #this function will be executed when app/web routes to /
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        message = "High CPU  or Memory utilization detected. Please scale up"
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=Message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
