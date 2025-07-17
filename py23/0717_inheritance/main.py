'''id0717_inheritance
インヘリタンス(継承)
オブジェクト指向3大要素の2つめ
あるクラスの性質を別のクラスに
引き継げる仕組み。
一言で言うと、コピペは止めて、差分だけ作ろうよ！

[継承組織]
class クラス名(継承元クラス名):
'''
class A:
    def a(self):
        print('a')
        
# Aの性質(メンバ)を継承したBの定義
class B(A):
    pass

b = B()
b.a()

'''Aクラスの性質をBクラスに
引き継いで(継承して)いるので、
Bクラスの持ち物にaメソッドがある。

アトリビュートも引き継がれる。'''
class A:
    def __init__(self):
        self.id = 0

class B(A):
    pass

b = B()
print(b.id)
'''[用語]
継承元を特に、
・スーパークラス
・上位クラス
・親クラス
継承先を特に
・サブクラス
・下位クラス
・子クラス
と言う。'''


#基本親は一つで子は複数の関係
class A:
    def a(self):
        print('a')
class B(A):
    def b(self):
        print('b')
class C(A):
    def c(self):
        print('c')


b = B()
b.a()
b.b()

c = C()
c.a()
c.c()