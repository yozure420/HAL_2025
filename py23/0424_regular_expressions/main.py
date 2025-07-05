# 正規表現
# 文字列をパターンにて表現するもの
# そのパターンにマッチしているか判定ができる

import re

# パターンの記述には、raw string を使う
# 正規表現にて[\]が特殊文字のため
# pythonとケンカしないように

pattern = "これは\nraw string"
print(pattern)

pattern = r"これは\nraw string"
print(pattern)

pattern = r"a"
str = "a"

# マッチ時は、match objectを返す
print(re.match(pattern, str))
# ミスマッチ時には、noneオブジェクトが返却される
str = "b"
print(re.match(pattern, str))

# パターンのマッチするかしないかは、ifで判定
# matchオブジェクト→true
# noneオブジェクト→false
if re.match(r"a","a"):
    print("match")
else:
    print("miss match")

if re.match(r"a","b"):
    print("match")
else:
    print("miss match")

# matchは先頭がマッチするか判定する
print(re.match(r"a", "abc"))
print(re.match(r"b", "abc")) #none
print(re.match(r"c", "abc")) #none

# searchはマッチする部分を探す
print(re.search(r"a", "abc"))
print(re.search(r"b", "abc"))
print(re.search(r"c", "abc"))

# 大文字小文字は規定では区別される
print(re.search(r"abc", "ABC"))
print(re.search(r"abc", "ABC",re.IGNORECASE)) #これで大文字小文字が区別されなくなる

# メタ文字
# 正規表現で特殊な意味を持つ文字
# ^...先頭・$...末尾・.,,,任意の一字
print ("^$.")
print(re.search(r"^abc", "abc"))
print(re.search(r"^abc", "aabc")) #none
print(re.search(r"^.abc", "abc")) #none
print(re.search(r"^.abc", "aabc"))
print(re.search(r".abc", "babc"))
print(re.search(r".abc", "babcd")) #後ろの文字は考慮されていない
print(re.search(r".abc", "abcd")) #none
print(re.search(r"abc$", "abc"))
print(re.search(r"abc$", "xxxabc"))
print(re.search(r"...abc$", "xxxabc"))
print(re.search(r"...abc$", "xxxxabc"))
print(re.search(r"...abc$", "xxabc")) #none
print(re.search(r"^...abc$", "xxxxabc")) #none

#繰り返し指定のメタ文字
# 「直前の文字」が何回繰り返すか指定することができる
# + ... 直前の文字が1回以上繰り返す
# * ... 直前の文字が0回以上繰り返す
# ? ... 直前の文字が0回か1回出現
# {m} ... 直前の文字がちょうどm回繰り返す
# {m,n} ... 直前の文字がm回以上n回以下繰り返す
# {m,} ... 直前の文字がm回以上繰り返す
# {,n} ... 直前の文字がn回以下繰り返す
print("+*?とか")
print(re.search(r"a+bc", "abc"))
print(re.search(r"a+bc", "aabc"))
print(re.search(r"a+bc", "aaabc"))
print(re.search(r"a+bc", "bc")) #none

print(re.search(r"a*bc", "abc"))
print(re.search(r"a*bc", "aaabc"))
print(re.search(r"a*bc", "bc"))
print(re.search(r"a*bc", "xbc"))

print(re.search(r"a?bc", "abc"))
print(re.search(r"a?bc", "bc"))
print(re.search(r"a?bc", "aabc"))
print(re.search(r"^a?bc", "aabc")) #none

print(re.search(r"a{3}bc", "aaabc"))
print(re.search(r"a{3}bc", "aabc")) #none
print(re.search(r"a{3}bc", "aaaabc"))
print(re.search(r"^a{3}bc", "aaaabc"))

print(re.search(r"a{2,3}bc", "aabc"))
print(re.search(r"a{2,3}bc", "aaabc"))
print(re.search(r"a{2,3}bc", "abc")) #none
print(re.search(r"a{2,3}bc", "aaaaabc"))
print(re.search(r"^a{2,3}bc", "aaaabc")) #none


print(re.search(r"a{2,}bc", "aabc"))
print(re.search(r"a{2,}bc", "aaabc"))
print(re.search(r"a{2,}bc", "abc")) #none
print(re.search(r"^a{2,}bc", "aaabc"))

print(re.search(r"a{,2}bc", "bc"))
print(re.search(r"a{,2}bc", "abc"))
print(re.search(r"a{,2}bc", "aabc"))
print(re.search(r"a{,2}bc", "aaabc"))
print(re.search(r"^a{,2}bc", "aaabc"))#none

# 文字集合
# [] ... いずれか
print("[]")
print(re.search(r'^[abc]bc','abc'))#aかbかcがでたあとに、bc
print(re.search(r'^[abc]bc','bbc'))#aかbかcがでたあとに、bc
print(re.search(r'^[abc]bc','cbc'))#aかbかcがでたあとに、bc
print(re.search(r'^[dbc]bc','abc'))#miss
print(re.search(r'[0123456789]','5'))
print(re.search(r'[0123456789]','b'))
print(re.search(r'[0-9]','5'))#[]内の
print(re.search(r'[a-z]','x'))
print(re.search(r'[a-z]','5'))#miss
print(re.search(r'[a-z]','X'))#大文字なのでmiss
print(re.search(r'[a-zA-Z]','x'))
print(re.search(r'[a-zA-Z]','X'))

print(re.search(r"\d","5")) #数値([0-9０-９])と一緒
print(re.search(r"\d","5"))
print(re.search(r"\d", "a")) #none

print(re.search(r'\D','5'))
print(re.search(r'\D','a'))
print(re.search(r'\d','@'))

print(re.search(r'\s',' '))#空白文字
print(re.search(r'\S','a'))#空白文字以外
print(re.search(r'\S','5'))
print(re.search(r'\S','　'))#miss

print(re.search(r'\bis\b','this is'))
# \bで単語の区切り
print(re.search(r'\bis\b','this'))#miss
#単語選択
#(abc|def) ... abcか、def
print("(abc|def)")
print(re.search(r'(color|colour)','color'))
print(re.search(r'(color|colour)','colour'))

# グループ
# （）で括ってグループ化することにより、
# .groupや、.groupsで取得可能
print('group/groups')
match = re.search(r'(\d{4})/(\d{1,2})/(\d{1,2})','2025/5/8')
print(match)
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))
print(match.groups())

#打消しは[\]
print('打消し')
print(re.search(r'\^','^'))
print(re.search(r'\$','$'))
print(re.search(r'\.','.'))
print(re.search(r'\+','+'))
print(re.search(r'\*','*'))
print(re.search(r'\?','?'))
print(re.search(r'\{','{'))
print(re.search(r'\(','('))
print(re.search(r'[0\-9]','-'))
print(re.search(r'[0\-9]','5'))
print('\\')
print(re.search(r'\\','\\'))

#最短一致
#+? ... 手前の文字が1回以上(最短)
#*? ... 手前の文字が0回以上(最短)
print('+?*?')
print(re.search(r'.+','abc'))#0~3で最短
print(re.search(r'.+?','abc'))#0~1で最短
print(re.search(r'.*','abc'))#0~3で最長
print(re.search(r'.*?','abc'))#0~0で最短

print(re.search(r'aaa.*ccc','aaabbbcccdddccc'))#0~3で最長

#マッチオブジェクトについて
print('Match Object')
match = re.search(r'ccc','abccc')
print(match.span())

# searchは複数マッチしない。
match = re.search(r'ccc','abcccabccc')
print(match.span())
#→最初に見つかった場所だけ。（複数マッチせず。）

#複数マッチ（文字列リスト取得）はfindall
print('findall')
match_str_list = re.findall(r'ccc','abcccabccc')
print(match_str_list)

#複数マッチ（文字列リスト取得）はfindall
print('findall')
match_str_list = re.findall(r'ccc','abcccabccc')
print(match_str_list)

#複数マッチ
#(Matchオブジェクト
# イテレーター取得)hafinditer
#＊イテレーター...forで回せる。
print('findall')
match_iter = re.finditer(r'ccc','abccabccc')

for match in match_iter:
    print(match.span())

#かぶりはなし
match_iter = re.finditer(r'ccc','abccccc')
for match in match_iter:
    print(match.span())

#マッチした箇所で区切ってリスト化
print('split')
print(re.split(r',','aaa,bbb,ccc'))

#マッチした箇所を置換
print('sub')
print(re.sub(r',','|','aaa,bbb,ccc'))
print(re.sub(r',',':','aaa,bbb,ccc'))

#先読み/後読み
# (?= )...先読み
# (?! )...否定先読み
#(?<= )...後読み
#(?<!)...否定後読み
#先頭を表す^や、末尾を表す$と同じ扱い。
# パターンマッチング(検査)はするが、
#検査のマッチオブジェクトには含まれない。

#先読み（右側をチェック）
print(re.search(r'python(?=flask)','pythonflask'))
print(re.search(r'python(?=flask)','python'))#miss
# →右側にflaskがあるpythonだけマッチ

#否定先読み（右側をチェック）
print(re.search(r'python(?!flask)','pythonflask'))
print(re.search(r'python(?!flask)','python'))#miss
# →右側にflaskがないpythonだけマッチ

#後読み（左側をチェック）
print(re.search(r'(?<=python)flask','pythonflask'))
print(re.search(r'(?<=python)flask','flask'))#miss
# →左側にpythonがあるflaskだけマッチ

#否定後読み（左側をチェック）
print(re.search(r'(?<!python)flask','pythonflask'))#miss
print(re.search(r'(?<!python)flask','flask'))
# →左側にpythonがないflaskだけマッチ

#先読み/後読み＋グループ
print(re.search(r'新宿(?=(駅|区))','新宿区'))
print(re.search(r'新宿(?=(駅|区))','新宿駅'))
print(re.search(r'新宿(?=(駅|区))','新宿店'))#miss
print(re.search(r'新宿(?=(駅|区))','新宿'))#miss
print(re.search(r'新宿(?=(駅|御苑))','新宿駅'))#先読みの可変長はOK
print(re.search(r'(?<=(西｜東)新宿)','西新宿'))
print(re.search(r'(?<=(西｜東)新宿)','東新宿'))
#print(re.search(r'(?<=(西｜東)新宿)','東新宿'))　後読みの可変長はNG

#先読み/後読みの活用例　その1
print(re.sub(r'日本(?=語)','国','日本では日本語と英語を勉強する。'))

#先読み/後読みの活用例　その2（タグ取得）
print(re.findall(r'(?<=#)\S+','#aaa #bbb #ccc'))

#先読みの手前(左)記載
print(re.search(r'(?=pythonflask)python','pythonflask'))
print(re.search(r'(?=pythonflask)python','flask'))#miss

print(re.search(r'(?=pythonflask)a','pythonflaska')) # miss
# →あらかじめ、先読み指定パターンが存在することをチェックし、
#  存在した場合、右側のパターンを、存在した場所の先頭からチェックする。
# 後読みの場合、存在した場所の"先頭から"、にならない。
# 存在した場所より"右側から"、となる。
print(re.search(r'(?<=pythonflask)a', 'pythonflaska'))

#先読み/後読みの活用例　その3
#任意条件(今回は3文字)に加え、
#英大文字が含まれないこと
print(re.search(r'(?=.*[A-Z]).{3}','Abc'))
print(re.search(r'(?=.*[A-Z]).{3}','aBc'))
print(re.search(r'(?=.*[A-Z]).{3}','abC'))
print(re.search(r'(?=.*[A-Z]).{3}','abc'))
print(re.search(r'(?=.*[A-Z]).{3}','aB'))

#先読み/後読みの活用例　その4
# 任意条件(今回は3文字)に加え、英大文字及び、小文字が含まれていること
pattern = r'(?=.*?[a-z])(?=.*?[A-Z]).{3}'
print(re.search(pattern,'Abc'))
print(re.search(pattern,'Abc'))
print(re.search(pattern,'AAA'))
print(re.search(pattern,'aaa'))
print(re.search(pattern,'000'))

#Point!
#先読みが連続した場合、AND条件になる。
#先読み/後読みの活用例　その5
#パスワードは、半角英字及び記号(_または.)にて
#構成され、少なくとも5桁必要。
#また、大文字、小文字、数字、記号(_.)の
#全てを含むこと。
pattern = r'(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[_.])[0-9a-zA-Z_.]{5,}$'
print(re.search(pattern,'aA0_a'))
print(re.search(pattern,'aA0.a'))
print(re.search(pattern,'aA0.aa'))
print(re.search(pattern,'aA0.'))#miss
print(re.search(pattern,'aa0.a'))
print(re.search(pattern,'AA0.A'))
print(re.search(pattern,'aA0aa'))
print(re.search(pattern,'aA0.a@'))