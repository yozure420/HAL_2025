#import
import random,time
#スライムクラスの作成
class Slime:
    #アトリビュートの作成、初期化
    def __init__(self): #プライベートなアトリビュート(アンダースコアふたつ)
        self.__position = 0
    #乱数を組み合わせて走る
    def run(self):
        num = random.randint(-1,3)
        strat = 0
        while strat < self.__position + num: #やったミス:<を<=にしてた
            print('=',end='',flush=True)
            time.sleep(0.1)
            strat += 1
        print('○')
        self.__position += num

    #ゲッター(デコレーター)
    @property
    def position(self):
        return self.__position
    #セッター
    @position.setter #@(propertyのname).setterと書く
    def position(self,position):
        self.__position = position