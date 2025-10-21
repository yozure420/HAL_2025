from flask import Flask

app = Flask(__name__)

@app.route("/") #この関数のときにこのURLを動かすよ(routing機能)この場合は、/がきたときにこのURLを動かすよって意味
def index():
    html = '''
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>index</h1>
</body>
</html>
        '''
    return html

# routeでURLを決める。
@app.route('/hello')#※先頭の/は必須(ルート)
# このURLに対応する処理を関数で定義する。
# 関数名はなんでもOK。(URLと不一致でもOK)
# ただし、ダブりはないこと。
def hello():
    return "Hello"
# 関数名をダブらせると...
# @app.route('/hello2')
# def hello():
#     return "Hello"
# AssertionError: View function mapping is overwriting an existing endpoint function: helloになる


# エンドポイント
# URLに紐づいた処理をエンドポイントと言う。
# 既定では関数名がエンドポイント名となる。
# 主に後述のurl_forにて利用する。
# また、app.routeで指定したURLのことをルール(rule)と言う。
# flask routes コマンドで確認可能
# ※app.pyが存在するディレクトリにて実行すること。


if __name__ == "__main__":
    #WEbサーバー起動
    app.run('0.0.0.0',80,debug=True)

