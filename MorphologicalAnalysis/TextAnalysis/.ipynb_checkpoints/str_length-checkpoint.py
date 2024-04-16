with open('output.txt', 'r') as file:
    text = file.read()

sentences = text.split('。')  # 文を「。」で分割

sentence_lengths = [len(sentence.split())
                    for sentence in sentences]  # 各文の単語数を計算

# 文の長さの分布を表示
length_count = {}
for length in sentence_lengths:
    length_count[length] = length_count.get(length, 0) + 1

for length, count in sorted(length_count.items()):
    print(f"単語数{length}の文の数: {count}")
