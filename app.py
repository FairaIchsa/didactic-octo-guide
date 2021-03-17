from flask import Flask, render_template, url_for, request
import git

app = Flask(__name__)


@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('./didactic-octo-guide')
        origin = repo.remotes.origin
        repo.create_head('master',
    origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()
        return '', 200
    else:
        return '', 400


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
