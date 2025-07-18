import random,time
i = 0
# while i <= random.randint(0,10):
#     print('=',end='')
#     i += 1
#     time.sleep(1)
#これだと、毎回違う乱数が生成される
num = random.randint(0,10)
while i <= num:
    print('=',end='',flush=True) #flush=Trueを入れないと1秒ごとにちゃんと出してくれない
    i += 1
    time.sleep(1)

# flush=Trueはバッファ(メモリにためておいたデータ)をフラッシュ(空に)するオプション

# 効率が悪い例（バッファリングなし）
#print("あ")  # 1文字だけ画面に出力
#print("い")  # 1文字だけ画面に出力
#print("う")  # 1文字だけ画面に出力

# 効率が良い例（バッファリングあり）
# 内部では：
# バッファ: "あいう" ← 3文字溜める
# 一気に画面に出力: "あいう"

# 実際の表示タイミング（バッファリングあり）
# 0秒: （何も表示されない）
# 1秒: （何も表示されない）
# 2秒: （何も表示されない）
# 3秒: 1秒目2秒目3秒目完了  ← 一気に表示