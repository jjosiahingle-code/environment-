import random

from flask import Flask

app = Flask(__name__)

facts_list = {"Most people who suffer from technological addiction experience strong stress when they find themselves outside the network coverage area or cannot use their devices", 
              "According to a study conducted in 2018, more than 50% of people aged 18 to 34 consider themselves dependent on their smartphones.",
              "The study of technological dependency is one of the most relevant areas of modern scientific research",
              "According to a 2019 study, more than 60% of people respond to work messages on their smartphones within 15 minutes after leaving work",
              "One way to combat technological dependency is to look for activities that bring pleasure and improve mood",
              "Elon Musk claims that social networks are designed to keep us inside the platform, so that we spend as much time as possible viewing content",
              "Elon Musk also advocates for the regulation of social networks and the protection of users' personal data. He claims that social networks collect a huge amount of information about us, which can then be used to manipulate our thoughts and behavior",
              "Social networks have their positives and negatives, and we should be aware of both when using these platforms." 
              }

heads = {"heads", "tails"}

@app.route("/random_fact")
def hello_world():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)

@app.route("/coin_toss")
def coin_toss():
    return f'<p>{random.choice(heads)}</p>'