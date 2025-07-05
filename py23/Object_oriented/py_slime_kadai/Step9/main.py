from slime import Slime
import time
# スライムの見た目をリストで定義(後から追加するときはここでappend)
slime_looks = [
    {'head': '○', 'body': '='},
    {'head': '★', 'body': '~'},
]
##########################################################################################
slime_looks.append({'head': '●', 'body': '-'})  #修正箇所はこれ
########################################################################################
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


for i in range(3,0,-1):
    print(i,end=' ',flush=True)
    time.sleep(0.1)
print('Go!!')

# レース中の表示
while all(s.position < GOAL for s in slimes):
    for slime in slimes:
        slime.run()
    print('----5----0',flush=True)
    time.sleep(0.1)

# slimes[0].position = 11
# slimes[1].position = 12
#とすると、54のmax関数で、同着なのに、slimes[1]が優勝となってしまう

# レース終了後、勝者判定とwinner!表示
# max_position = max(s.position for s in slimes)　使わない
winners = [s for s in slimes if s.position >= GOAL]  # GOAL以上に達したスライムを勝者とする
# winners = [s for s in slimes if s.position == max_position]とするとpositionが11,12で同着の場合12のほうがwinnerになってしまう(max関数のため)

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