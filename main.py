import requests
from flask import Flask, render_template, request

app = Flask(__name__)

TOKEN = "ce6f97de53a2d4c3e48ba0a0ac6c2234aaa45ccb"
URL = 'https://api-ssl.bitly.com/v4/shorten'

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/new_url", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        site = request.form.get("input")
        data = '{ "long_url": "https://bitly.com/"}'
        x = data[:15] + site + data[-2:]
        new_data = x

        response = requests.post(url=URL, headers=HEADERS, data=new_data).json()["link"]

        return render_template("index.html", name=response, pre=site)


if __name__ == "__main__":
    app.run(debug=True)









