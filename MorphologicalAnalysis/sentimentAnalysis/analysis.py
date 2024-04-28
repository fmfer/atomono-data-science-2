from janome.tokenizer import Tokenizer
from asari.api import Sonar
import re
sonar = Sonar()

# sentiment_dic = {}

# with open('pn_ja.dic', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         line_components = line.split(':')
#         sentiment_dic[line_components[0]] = line_components[3]

data = sonar.ping(text="広告多すぎる♡")
def gen_aggregate_score(data):
    # ポジティブとネガティブのconfidence値を抽出
    #negative_confidence = next(item for item in data["classes"] if item["class_name"] == "negative")["confidence"]
    positive_confidence = next(item for item in data["classes"] if item["class_name"] == "positive")["confidence"]
    # 総合スコアを計算 (-1 から 1 の範囲)
    # ネガティブconfidenceからポジティブconfidenceを引いて、結果に2を掛けて範囲を調整します。
    # aggregate_score = (negative_confidence - positive_confidence)*0.5 - 1
    return positive_confidence*2-1
    #return positive_confidence-negative_confidence


def sentiment_analyse(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    sentiment_val = 0
    word_cnt = 0
    p = re.compile('^([あ-ん]|[A-Za-z0-9_!-]+)$')
    for token in tokens:
        #単語の基本形を取り出し
        word = token.surface

        if p.match(word):
            continue

        score = gen_aggregate_score(sonar.ping(text=word))
        sentiment_val = sentiment_val + score
        word_cnt += 1

        # sentiment_val = sentiment_val + float(analyzer.analyze(word))
        # word_cnt += 1
        # if word in sentiment_dic:
        #     # sentiment_val = sentiment_val + float(sentiment_dic[word])
        #     sentiment_val = sentiment_val + float(analyzer.analyze(word))
        #     word_cnt += 1
    if word_cnt == 0:
        return 0
    else:
        return round(sentiment_val/word_cnt, 5)
