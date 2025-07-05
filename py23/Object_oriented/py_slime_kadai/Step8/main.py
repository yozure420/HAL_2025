from slime import Slime
import time
# スライムの見た目をリストで定義(後から追加するときはここでappend)
slime_looks = [
    {'head': '○', 'body': '='},
    {'head': '★', 'body': '~'},
    # スライムを追加したい場合は、ここに追記します
    # {'head': '●', 'body': '-'},
]

# 新しいスライムを追加
slime_looks.append({'head': '●', 'body': '-'})

# 繰り返し構造でスライムのインスタンスを生成
slimes = [Slime(head=look['head'], body=look['body']) for look in slime_looks]

print('[List of runners]')

for s in slimes:
    num = slimes.index(s) + 1
    print('No.'+f'{num}'+' '+f'{s.head}')

print('[Bet]')

while True:
    try:
        bet_num = int(input('No:'))
        if 1 <= bet_num <= len(slimes):
            bet_slime = slimes[bet_num - 1]
            break
        else:
            print('存在する選手番号の値を入力してください')
    except ValueError:
        print('有効な数字を入力してください')


GOAL = 10

# レース中の表示
while all(s.position < GOAL for s in slimes):
    for slime in slimes:
        slime.run()
    print('----5----0')
    time.sleep(0.1)

# レース終了後、勝者判定とwinner!表示
max_position = max(s.position for s in slimes)
winners = [s for s in slimes if s.position == max_position]#勝ったやつは誰か判定

print("\n---結果発表---")
for s in slimes:
    result = s.head
    if s in winners:
        result += " winner!"
    print(result)
#if result == bet_slime.head:とすると、一個上で、resultがかきかえられているため一致しないので絶対loseなる
if bet_slime in winners:
    print('You win!')
else:
    print('You lose!')

