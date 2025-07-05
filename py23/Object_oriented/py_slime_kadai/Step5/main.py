from slime import Slime
import time

# スライムの見た目をリストで定義(後から追加するときはここでappend)
slime_looks = [
    {'head': '○', 'body': '='},
    {'head': '★', 'body': '~'},
    # スライムを追加したい場合は、ここに追記します
    # {'head': '●', 'body': '-'},
]

# 繰り返し構造でスライムのインスタンスを生成
slimes = [Slime(head=look['head'], body=look['body']) for look in slime_looks]

# 全てのスライムがゴールに達していない間、ループを続ける
while all(s.position <= 10 for s in slimes):
    for slime in slimes:
        slime.run()
    print('----5----0')
    time.sleep(0.5)