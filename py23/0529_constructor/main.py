# コンストラクタ
# 　インスタンス化の際に動作するメソッド。
# 　初期化の用途にて利用される。
# [定義書式]
class User:
    def __init__(self):
        print('コンストラクタ')

user = User()
        #↑↑↑これでコンストラクタが動作する

# コンストラクタ＆引数
# 　コンストラクタはメソッドなので、引数を渡せる。

class User:
    def __init__(self,a):
        print(a)

user = User(123)

# コンストラクタにてreturnは記述しない。他言語だとクラス名をそのままコンストラクタにする場合が多い。

class User:
    def __init__(self,a):
        #return 1 #何も返さないはずなのに、int返してるでってエラーでるよ
        return #あまりないけど、あるとしてもこれくらい。

user = User()
