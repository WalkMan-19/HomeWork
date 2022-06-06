from flask import Flask
from utils import load_json

app = Flask(__name__)


@app.route('/')
def main_page():
    result = str()

    for candidate in load_json():
        result += ('<pre>{}\nИмя кандидата: {}\nПозиция: {}\nНавыки: {}\n<pre>'.format(
            candidate["picture"], candidate["name"], candidate["position"], candidate["skills"]))

    return result


@app.route('/candidates/<int:uid>')
def candidate_id(uid):

    for i in load_json():
        if i["id"] == uid:
            return '<pre>{}\nИмя кандидата: {}\nПозиция: {}\nНавыки: {}\n<pre>'.format(
                i["picture"], i["name"], i["position"], i["skills"])


@app.route('/skills/<x>')
def skills_id(x):
    skill_result = str()
    for i in load_json():
        if x.lower() in i["skills"].lower():
            skill_result += '<pre>{}\nИмя кандидата: {}\nПозиция: {}\nНавыки: {}\n<pre>'.format(
                i["picture"], i["name"], i["position"], i["skills"])
    return skill_result


app.run()
