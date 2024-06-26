# ネガポジ分析

## 実行方法

`$ cd MorphologicalAnalysis/sentimentAnalysis`
`$ python main.py`

## 分析対象

`MorphologicalAnalysis/material`配下の csv データ. JIRA, Figjam(「振り返り　象、死んだ魚、嘔吐 (11 月分)」など).

## 各ファイルについて

```
sentimentAnalysis/
├── Pipfile
├── Pipfile.lock
├── README.md
├── analysis.py // 感情分析に関するscriptです
├── elephant_fish.py // 象、死んだ魚、嘔吐をを行った週の分析
├── files.py // path取得のutilです
├── fun_done_learn.py // fun done learnを行った週の分析
├── kpt.py // KPTを行った週の分析
├── main.py // このファイルを実行してください
├── pn_ja.dic // 感情分析に使用する辞書です
├── speed_car.py // スピードカを行った週の分析
└── star_fish.py // star fishを行った週の分析
```

## 分析方法

### JIRA の場合

### ふりかえりデータ(FigJam)の場合

入力されている各文(Content)について、形態素解析を行い、各 token の感情 score の平均値を算出しています。
それらの平均値をさらに算出し、出力しています。

<!-- ## 辞書について

東工大教授高村氏による辞書を使用しています。

リンク: http://www.lr.pi.titech.ac.jp/%7Etakamura/pndic_ja.html -->

## 参考文献

[感情分析でニュース記事のネガポジ度合いをスコア化する](https://qiita.com/g-k/items/e49f68d7e2fed6e300ea)

---

分析内容：

```
python3 main.py
象、死んだ魚、嘔吐 (11月)

Jira (1)
 summary:  0.31956759999999995
 comment:  0.022625199999999998
 description:  0.2671676
 トータル:  0.20312013333333334
Jira
 summary:  0.3829896666666668
 comment:  0.01885433333333333
 description:  0.19412666666666664
 トータル:  0.19865688888888894
振り返り　象、死んだ魚、嘔吐 (11月分)
 中山建太: 0.5281966666666666
 平田聖: 0.49728
 水野響: 0.44598444444444446
 鈴木真希: 0.38452
 Dai Miyahara: 0.41870500000000005
 大野寛人: 0.404905
 FABIAN M. FERNANDEZ: 0.20968
FigJam avg:  0.4127530158730158
Notion: 
 Content:  0.5173
Slack: 
 satoshi.hirata: 0.48091
 Hibiki: 0.51682
 Nakayama: 0.49089
 Dai: 0.51706
 FABIAN: 0.49275
 鈴木真希: 0.49057
 slackbot: 0.57489
 Ohno: 0.45871
Slack avg:  0.502825



fun,done,learn

Jira (1)
 summary:  0.45317375
 comment:  0.069134375
 description:  0.164838125
 トータル:  0.22904875000000002
Jira
 summary:  0.42961045454545455
 comment:  0.025714090909090912
 description:  0.20634681818181821
 トータル:  0.2276622727272727
振り返り　fun,done,learn
 Dai Miyahara: 0.39294
 大野寛人: 0.44095
 中山建太: 0.41590812499999996
 平田聖: 0.46683333333333327
 鈴木真希: 0.4967966666666667
 水野響: 0.4395716666666667
 FABIAN M. FERNANDEZ: 0.4372275
FigJam avg:  0.4414610416666666
Notion: 
 Content:  0.49459
Slack: 
 satoshi.hirata: 0.42283
 Hibiki: 0.46276
 Dai: 0.48348
 FABIAN: 0.44623
 Nakayama: 0.43466
 Ohno: 0.47745
 鈴木真希: 0.49272
 slackbot: 0.57489
Slack avg:  0.4743775



speed car

['ふりかえり：speed car.csv', '中鉢PT2023 Member Analytics Oct 10, 2023 - Oct 16, 2023.csv', 'Jira2.csv', 'Jira.csv', '中鉢PT2023 Channel Analytics Oct 10, 2023 - Oct 16, 2023.csv']
Jira2
 summary:  0.379226
 comment:  0.1037252
 description:  0.2020992
 トータル:  0.22835013333333337
Jira
 summary:  0.37378999999999996
 comment:  0.24836
 description:  0.2761877272727273
 トータル:  0.29944590909090907
振り返り　speed car
 水野響: 0.3797561538461539
 平田聖: 0.5011140000000001
 大野寛人: 0.4821066666666667
 FABIAN M. FERNANDEZ: 0.227235
 Dai Miyahara: 0.40676125
 鈴木真希: 0.43363999999999997
 中山建太: 0.4579915384615385
FigJam avg:  0.41265780128205126
Notion: 
 Content:  0.50054
Slack: 
 satoshi.hirata: 0.46931
 Hibiki: 0.52144
 Dai: 0.47949
 Nakayama: 0.44894
 Ohno: 0.44281
 鈴木真希: 0.50608
 FABIAN: 0.53205
Slack avg:  0.48573142857142854



star fish

Jira (1)
 summary:  0.37239
 comment:  0.06309583333333334
 description:  0.24915416666666668
 トータル:  0.22821333333333335
Jira
 summary:  0.3878445
 comment:  0.02525
 description:  0.30347350000000006
 トータル:  0.238856
振り返り　start fish
 中山建太: 0.41246
 Dai Miyahara: 0.5410283333333333
 鈴木真希: 0.46039666666666673
 大野寛人: 0.3441083333333334
 水野響: 0.45076714285714287
 平田聖: 0.513345
 FABIAN M. FERNANDEZ: 0.41741
FigJam avg:  0.44850221088435377
Notion: 
 Content:  0.51854
Slack: 
 satoshi.hirata: 0.43245
 Nakayama: 0.47048
 Hibiki: 0.4953
 Dai: 0.4798
 FABIAN: 0.4877
 Ohno: 0.47565
 鈴木真希: 0.50792
 slackbot: 0.57489
Slack avg:  0.49052375



KPT

Jira (1)
 summary:  0.31889
 comment:  0.54209
 description:  0.5118
 トータル:  0.45759333333333335
Jira
 summary:  0.371588
 comment:  0.282762
 description:  0.256562
 トータル:  0.30363733333333337
Notion: 
 Content:  0.50962
Slack: 
 satoshi.hirata: 0.47021
 Dai: 0.47733
 FABIAN: 0.49935
 Nakayama: 0.51475
 鈴木真希: 0.56867
 Ohno: 0.49829
 Hibiki: 0.51886
 slackbot: 0.57489
Slack avg:  0.51529375


(base) 
```
