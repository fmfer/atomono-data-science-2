import MeCab
# 分書きが出力される
m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic')
print(m.parse("1歳9ヶ月の娘がめかぶ大好きなのでMacにMecabを入れて遊んでみます。"))
