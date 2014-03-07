# -*- coding: utf-8
"""
mecabのユーザ辞書を作る
"""
output = 'words.csv'
data = """
自然数, 標準偏差, テイラー展開, インターフェイス,
X11, P2P, 7zip, SHA1, C#, C++, Tcl/Tk, Objective C,
.NET, 条件分岐, インターフェイス, 派生型, 抽象型,
切り捨て, 無名関数, 関数呼出し, スコープチェーン
"""

fo = file(output, 'w')
words = [x.strip() for x in data.split(',')]

for w in words:
    if not w: continue
    fo.write('%s,,,500,名詞,一般,*,*,*,*,*\n' % w)

fo.close()
