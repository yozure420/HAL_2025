#import
import random
#スライムクラスの作成
class Slime:
    #アトリビュートの作成、初期化
    def __init__(self): #プライベートなアトリビュート(アンダースコアふたつ)
        self.__position = 0
    #乱数を組み合わせて走る
    def run(self):
        self.__position += random.randint(-1,3)
        print(self.__position)
    #ゲッター(デコレーター)
    @property
    def position(self):
        return self.__position
    #セッター
    @position.setter #@(propertyのname).setterと書く
    def position(self,position):
        self.__position = position