#import
import random,time
#スライムクラスの作成
class Slime:
    #アトリビュートの作成、初期化
    def __init__(self, head='○', body='='): #プライベートなアトリビュート(アンダースコアふたつ)
        self.__position = 0
        self.__head = head
        self.__body = body
    #乱数を組み合わせて走る
    def run(self):
        num = random.randint(-1,3)
        strat = 0
        while strat < self.__position + num:
            print(self.__body,end='',flush=True)
            time.sleep(0.1)
            strat += 1
        print(self.head)
        self.__position += num
    #デコレーター
    @property
    def position(self):
        return self.__position
    @position.setter #@(propertyのname).setterと書く
    def position(self,position):
        self.__position = position

    @property
    def head(self):
        return self.__head
    @head.setter
    def head(self,head):
        self.__head = head

    @property
    def body(self):
        return self.__body
    @body.setter
    def body(self,body):
        self.__body = body