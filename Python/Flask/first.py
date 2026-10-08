from flask import Flask
import matplotlib.pyplot as plt
import numpy as np
import fastf1 as F1
from fastf1 import plotting
import seaborn as sns


F1.Cache.enable_cache(r"F:\! Fast F1 Cache")
F1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1')

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/about")
def about():
    return "kaam krle"

@app.route("/F1graph")
def f1g():
    race = F1.get_session(2026,"Japan","Q")
    race.load()
    
    Laps = race.laps
    Fast = Laps.pick_fastest()
    
    Tel = Fast.get_telemetry()
    
    x = Tel["X"]
    y = Tel["Y"]
    plt.plot(x,y,color="red")
    return plt.show()
@app.route("/F1not")
def F1not():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>

<body>
    <h1>Hello!</h1>
    <p>Welcome to my website.</p>
</body>
</html>"""

app.run(debug=True)