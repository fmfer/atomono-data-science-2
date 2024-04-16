# mecab -d /usr/local/lib/mecab/dic/ipadic -Owakati <input.txt> output.txt
# 上記のコマンドを実行してから、スクリプトを実行する
with open('output.txt', 'r') as file:
    text = file.read()

character_count = len(text)
print("文字数:", character_count)
