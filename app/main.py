from flask import Flask, request, render_template, jsonify, redirect, url_for
from short_url import add_link, get_link

app = Flask(__name__)


@app.route("/link", methods=['POST'])
def to_tiny_url():
    full_text = request.form["original_text"]
    tiny_url = add_link(full_text)
    return redirect(url_for("get_tiny_url", tiny_id=tiny_url), code=302)


@app.route("/<tiny_id>", methods=['GET'])
def get_tiny_url(tiny_id):
    status, full_text = get_link(tiny_id)
    if status:
        return render_template('shorturl.html', data={"full": full_text,
                                                      "tiny": tiny_id})
    else:
        return "some error happened"


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
