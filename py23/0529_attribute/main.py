# 属性...アトリビュート。※他言語ではフィールドやプロパティともいう。
#         その物が持つ、データのこと。※名詞
#[定義書式]
# def __init__(self):
#    コンストラクタで、selfを用いて定義していく。
#    self.アトリビュート名1 = 初期値
#    self.アトリビュート名2 = 初期値 ※必要数分記述OK

# self...自分。自身。自己。
# ということで、インスタンス化によって
# 出来上がったものの、その物"自身"を表すのがself。

class User:

    def __init__(self):
        self.id = 0
        self.name = 'no name'
        self.address = ''
        tel = '090'#selfがないと、ローカル変数

# アトリビュート値の操作
# [利用書式]
# インスタンス.アトリビュート名
user = User()
user.id = 123
user.address = '東京'
print(user.id,user.name,user.address)
#print(user.tel)#←ない
#アトリビュートはコンストラクタで定義が基本
#でも、言語仕様的にはコンストラクタで無くても可。
#(保守性上、やらない方が良い)
class User:
    def a(self):
        self.aaa = 0
        self.bbb = 0


user = User()
#print(user.aaa)
user.a()#まずaメソッドを呼んで、初めて
print(user.aaa)
#が動く(やらないほうがいい。__init__でやるべき)

# また、外部からの追加も可(やらない方が良い)
user.ccc = 999
print(user.ccc)
user.aab = 'ddd'
print(user.aaa)