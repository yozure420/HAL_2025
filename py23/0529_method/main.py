# Memeber
#     物が持ってる特性のこと。
# 以下2つがある。
# 属性...アトリビュート。※他言語ではフィールドやプロパティともいう。
#         その物が持つ、データのこと。※名詞
# 振る舞い...メソッド。
#           その物が持つ、処理のこと。※動詞

# 振る舞い(メソッド)
# [定義書式]
# def メソッド名(self [,引数[,引数...]]):
class User:
    # ここで関数を定義すれば、それがメソッドとなる。
    def hello(self): #selfは必須
        print('hello')

# メソッド呼び出し
# [呼び出し書式]
# インスタンス.メソッド名()
# window.alert("error");
# alert("err");

#インスタンス化
user = User()

user.hello()
# メソッド(≒関数)呼び出しは、「括弧」が必要！
# メソッド呼び出し時、定義側のselfは気にしない。(selfは勝手に渡る。)

#引数
class User:
    def hello(self,name):
        print(f'hello {name}')
#       第１引数のselfはくどいけど必須。
#        第２引数以降に、任意引数を設定していく。
user = User()
user.hello("abc")
#戻り値
class User:
    def hello(self):
        return 'hello!'

user = User()
print(user.hello())
# ちなみに、return省略時はNoneが返却される。
# メソッドは複数定義できる。
class User:
    def a(self):
        print('a')

    def b(self):
        print('b')

user = User()
user.a()
user.b()
# 同一メソッド名は後方優先。やらないけど、言語仕様上動く。＊スクリプト言語の特性
print("uuuuuuuuuuuuuuuu")
class User:
    def a(self):
        print('a')

    def a(self):
        print('b')

user = User()
user.a()#上から下に実行されるので、bが出力される