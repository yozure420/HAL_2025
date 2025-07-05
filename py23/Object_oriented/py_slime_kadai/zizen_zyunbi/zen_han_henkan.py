print(int(input('数字')))#全角半角の区別なくできる
# これはpythonの内部的には、int()は、
# PyLong_FromUnicodeObject()を通してUnicodeの数値(isdigit()に相当)を許容してるため#これはCPythonというC言語的なpythonの関数の実装
import unicodedata
print(unicodedata.name('１'))
# → FULL WIDTH DIGIT ONE
# のように全角の「１」もdigit(数値)として認識される
#Unicode: 「1」→「U+0031」:: 「１」→「U+FF11」
######################################################################################################
# 全角数字を半角に変換するテーブルを作成
zen_to_han = str.maketrans('０１２３４５６７８９', '0123456789')
num = input("数字を入力してください: ").translate(zen_to_han)
num = int(num)
print(num)
#translateで変換、maketransで変換する内容
################################################################################################################
import unicodedata
num = input("数字を入力してください: ")
num = unicodedata.normalize('NFKC', num)
num = int(num)
print(num)
#NFKCという正規化は、数字だけでなく、記号やアルファベットも全角から半角にしてくれる
#############################################################################################################
bet_num = input('No:')
# 全角数字を半角に変換
z2h = {'０':'0','１':'1','２':'2','３':'3','４':'4','５':'5','６':'6','７':'7','８':'8','９':'9'}
for zenkaku, hankaku in z2h.items(): #z2h.items()で例えば、'０':'0'のペアを取り出す
    bet_num = bet_num.replace(zenkaku, hankaku) #replaceで例えば、'０'を'0'にする
bet_num = int(bet_num)  # 半角も全角も整数に変換
##############################################################################################################
def zenkaku_to_hankaku(num_str):
    # 全角数字を半角数字に変換
    result = ""
    for c in num_str:
        code = ord(c) #Unicodeのコードポイントを取得。半角1なら0x31。全角１なら0xFF11。
        if 0xFF10 <= code <= 0xFF19:  # 全角数字の範囲
            c = chr(code - 0xFF10 + ord('0'))
        result += c
    return result

bet_num = input('No:')
bet_num = zenkaku_to_hankaku(bet_num)
bet_num = int(bet_num)
###########################################################################################################################