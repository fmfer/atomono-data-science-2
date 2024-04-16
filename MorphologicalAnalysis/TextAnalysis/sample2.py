import MeCab
import collections

# 品詞で分ける
m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic')

text = ("2018年のJaSST東京で柴田さんの講演にこの本が出てきた記憶があり、柴田さんのいちファンとして購入。"
        "日本で言うところのソニックガーデンさん的位置づけの会社の話かなと思って読みました。実際にはそうだったり、違ったり。"
        # 中略 https://yoshikiito.net/blog/archives/2335/ の本文全部をtextという変数に入れてます。
        "ソフトウェア業界で自分の身の回りのチームや組織に対してなにか変えていこう、新しいことをやっていこう、という人に読んでほしい本でした。")

node = m.parseToNode(text)

words = []

while node:
    hinshi = node.feature.split(",")[0]
    if hinshi in ["名詞", "動詞", "形容詞"]:
        origin = node.feature.split(",")[6]
        words.append(origin)
    node = node.next

c = collections.Counter(words)
print(c.most_common(20))
