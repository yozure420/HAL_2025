import random,time,sys
i = 0
#sysはpythonのインタプリタや実行環境に関する情報を扱うための標準ライブラリ
num = random.randint(0,10)
while i <= num:
    print('=',end='')
    sys.stdout.flush()#手動フラッシュ
    i += 1
    time.sleep(1)


#バッファリングの無効化は環境変数の制御でもできる
# バッファリングを無効化
#以下で実行↓
# export PYTHONUNBUFFERED=1
# python script.py

#または実行時に指定
#python -u script.py
