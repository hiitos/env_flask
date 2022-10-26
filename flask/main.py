from flask import Flask, Blueprint, request ,render_template
import flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>!++++++Hello, World FLASK++++++!</p>"

@app.route("/user/<username>")
def show_user_profile(username):
    return "UserName: " + str(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post" + str(post_id)

@app.route('/rendering')
def index():
    return render_template('index.html', message="花子~~~")

# login処理
@app.route('/login_form', methods=['GET', 'POST'])
def form():
    # ２回目以降データが送られてきた時の処理です
    if request.method == 'POST':
        print("POSTされたIDは？" + str(request.form['id']))
        print("POSTされたPASSWORDは？" + str(request.form['pwd']))
        return render_template('form.html')
    # １回目のデータが何も送られてこなかった時の処理です。
    else:
        return render_template('form.html')

# web API
@app.route("/webapi")
def mypage():
    # login = False
    login = True
    if login is False:
        return flask.jsonify({
            "code" : 400,
            "msg"  : "Bad Request"
        })

    user_data = {"user_name": "ai_academy"}
    return flask.jsonify({
        "code": 200,
        "msg" : "OK",
        "result": user_data
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)