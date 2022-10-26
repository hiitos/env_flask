# falsk

## <span style="color:orange">@app.route</span>
routeに指定した引数をurlの後に指定すると、下に記述した関数が呼び出される 

```
@app.route("/")
def hello_world():
    return "<p>!++++++Hello, World FLASK++++++!</p>"
```
で、URL叩いた時、!++++++Hello, World FLASK++++++!を返す  
http://localhost:9000

<br>

```
@app.route("/user/<username>")
def show_user_profile(username):
    return "UserName: " + str(username)
```
で、localhost:8000/hello/random_name
叩いた時、random_nameに入れた値をを返す  
http://localhost:9000/user/aaaaa

<br>

```
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post" + str(post_id)
```
http://localhost:9000/post/1

## <span style="color:orange">render_templateによる読み込み</span>
Flaskでは、render_template関数を使い、htmlファイルを表示させ、htmlファイルに簡単に値を入れることができる。

render_templateを使う場合
- importによる記述  
- templatesフォルダを新たに作成しそこにhtmlファイルを置く  
＊render_templateを用いる際には、templatesフォルダを作成する必要があり、作成していないとhtmlファイルを読み込むことが出来ない  

http://localhost:9000/rendering

## login機能の場合
http://localhost:9000/login_form

## <span style="color:orange">Web API (JSON API)</span>
aa


## <span style="color:orange">Blueprint</span>
Blueprintとは、Flaskの中で使われるモジュールで、アプリを分割することができ、プログラムの保守性を向上させることができるライブラリのこと

```
from views1 import site1_bp
app.register_blueprint(site1_bp)
```

```
from flask import Blueprint, render_template
site1_bp = Blueprint('site1', __name__, url_prefix='/site1')

@site1_bp.route('/')
def hello():
    return render_template('site1/hello1.html')
```

```
Blueprint(name,  # Blueprintの名前を指定
    import_name,  # ブループリントのパッケージ名を指定
    static_folder,   # 静的ファイルを配置するフォルダを指定
    static_url_path,   # 特に指定しなければ url_prefix の値が設定される
    template_folder,   # アプリのテンプレート検索パスを指定
    url_prefix,   # アプリのルートパスを指定
    subdomain,  # ブループリントルートが一致するサブドメインを指定
    url_defaults,   # ブループリントがルーティングするデフォルト値の指示
    root_path)  # import_nameが取得できなかった場合の検索先を指定  
```