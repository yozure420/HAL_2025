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

GOAL = 10

# レース中の表示
while all(s.position < GOAL for s in slimes):
    for slime in slimes:
        slime.run()
    print('----5----10')
    time.sleep(0.5)

# レース終了後、勝者判定とwinner!表示
max_position = max(s.position for s in slimes)
winners = [s for s in slimes if s.position == max_position]

print("\n---結果発表---")
for s in slimes:
    result = s.head
    if s in winners:
        result += " winner!"
    print(result)