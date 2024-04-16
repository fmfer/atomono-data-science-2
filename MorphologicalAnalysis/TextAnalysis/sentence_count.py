# 以下の内容をしてから、
# mecab -d /usr/local/lib/mecab/dic/ipadic -Owakati hoge.txt >  output.txt
# 次にこれを実行
# ex) python sentence_count.py
with open('output.txt', 'r') as file:
    text = file.read()

sentence_count = text.count('。') + text.count('！') + text.count('？')
print("文の数:", sentence_count)
