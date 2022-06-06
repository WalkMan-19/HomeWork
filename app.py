from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def main_page():
    with open('candidates.json', 'r', encoding="utf-8") as f:
        candidates_info = json.load(f)
        result = str()

        for candidate in candidates_info:
            result += ('<pre>{}\nИмя кандидата: {}\nПозиция: {}\nНавыки: {}\n<pre>'.format(
                candidate["picture"], candidate["name"], candidate["position"], candidate["skills"]))

        return result


@app.route('/candidates/<int:uid>')
def candidate_id(uid):
    with open('candidates.json', 'r', encoding="utf-8") as f:
        candidates_info = json.load(f)
        for i in candidates_info:
            if i["id"] == uid:
                return '<pre>{}\nИмя кандидата: {}\nПозиция: {}\nНавыки: {}\n<pre>'.format(
                    i["picture"], i["name"], i["position"], i["skills"])


@app.route('/skills/<x>')
def skills_id(x):
    with open('candidates.json', 'r', encoding="utf-8") as f:
        candidates_info = json.load(f)
        skill_result = str()
        for i in candidates_info:
            if x.lower() in i["skills"]:
                skill_result += '<pre>{}\nИмя кандидата: {}\nПозиция: {}\nНавыки: {}\n<pre>'.format(
                    i["picture"], i["name"], i["position"], i["skills"])
        return skill_result


app.run()
