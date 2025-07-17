# インスタンスメソッドとクラスメソッド
#  インスタンス(実体)に依存しているメソッドと、
#  クラスに依存しているメソッド。
#  言い換えると、インスタンスの持ち物か、クラスの持ち物かの違い。

# インスタンスメソッド
#  インスタンス(実体)の持ち物なので、
#  インスタンス変数.メソッド名()にて呼び出す。
# ※今まで作成してきたメソッド。
# [定義書式]= Class Myclass:
#               def method_name(self):
# 利用例）
#  my_class = MyClass()
#  my_class.method_name()   # 呼び出しにインスタンス変数が必須。

# クラスメソッド
#  クラスの持ち物なので、
#  クラス名.メソッド名()にて呼び出せる。
# [定義書式] = Class Myclass:
# @classmethod            ※デコレーター必須
# def method_name(cls):   ※第１引数必須。clsという名前は慣例。
# [利用書式]
# MyClass.method_name()   # 呼び出しにインスタンス変数は不要。※クラスの持ち物なので。
class User:
    def instance_method(self):
        print(1)
        
    @classmethod
    def class_method(cls):
        print(2)
#クラスメソッドはインスタンス不要で呼び出せる
User.class_method() ##user→classmethodと直接呼出
#クラスから、インスタンス・メソッドは呼べない
# User.instance_method()
user =User()
user.instance_method()

# インスタンスからクラスメソッドはよべる
user.class_method()

# ポイント!
# インスタンスメソッドは、
# 出来上がったインスタンスの持ち物。
# クラスメソッドは、
# インスタンスに関係なく、
# クラス自体の持ち物。