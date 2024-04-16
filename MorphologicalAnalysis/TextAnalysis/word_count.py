import MeCab

# 単語カウント
# ex) python word_count.py hoge.tx


def find(lists, item):
    for word in lists:
        if isMatch(word, item):
            return word
    return None


def getCounts(a):
    return a["counts"]


def isMatch(a, b):
    if (a["word"] == b["word"]):
        matched = True
        for i in range(len(a["info"])):
            if a["info"][i] != b["info"][i]:
                matched = False
                break
        if matched:
            return True
        else:
            return False
    else:
        return False


def mecab(contents, option):
    results = []
    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic')
    parsed = tagger.parse(contents)
    words = parsed.split('\n')
    for word in words:
        temp = word.split('\t')
        if len(temp) == 2:
            item = {"word": temp[0], "info": temp[1].split(','), "counts": 1}
            results.append(item)
    return results


def readFile(file):
    f = open(file, "r")
    contents = f.read()
    return contents


source = readFile("hoge.txt")
option = '-d  /usr/local/lib/mecab/dic/ipadic'
words = []
print("入力した文章：", source)
results = mecab(source, option)
print("===== 結果 =====")
for result in results:
    found = find(words, result)
    if found == None:
        words.append(result)
    else:
        found["counts"] = found["counts"] + 1
words.sort(reverse=True, key=getCounts)
for word in words:
    if word["info"][0] == "名詞":
        print(word["word"], word["counts"])
