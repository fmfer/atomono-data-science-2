# 11/7

作成日時: October 19, 2023 2:09 AM

### プロダクトビジョン

**ユーザーの後継品・代替品検索コストの削減**

### プロダクトゴール

**ユーザーのお気に入り商品の後継品・代替品を見つけやすくする**

### 今月の目標

- https://chubachi-pt-2023.atlassian.net/browse/AT-268
- https://chubachi-pt-2023.atlassian.net/browse/AT-267
- https://chubachi-pt-2023.atlassian.net/browse/AT-460
- https://chubachi-pt-2023.atlassian.net/browse/AT-573
- https://chubachi-pt-2023.atlassian.net/browse/AT-599
- https://chubachi-pt-2023.atlassian.net/browse/AT-601
- https://chubachi-pt-2023.atlassian.net/browse/AT-83
- https://chubachi-pt-2023.atlassian.net/browse/AT-577
- 

### アジェンダ

- [今日のメモ担当](https://www.notion.so/Meetings-b96fa7ac63684ce0b8296f4cfa67604a?pvs=21)(1分)　@FERNANDEZ
- 先週行った振り返り(15分)  @Kenta Nakayama
- 今週のスプリントゴール(10分)
- 今週のアウトプット共有(15分) POから
    - ユーザーストーリー&システムデモ
- 質疑応答(10分)

先生からの報告

 —コアミーティング終了—

- 振り返り手法の今後の運用について @Kenta Nakayama
- 振り返り(45分)
- スプリントプランニング(45分)
- 月末 [プロダクトバックログ](https://chubachi-pt-2023.atlassian.net/jira/software/c/projects/AT/boards/3/timeline)のリファイメントを行う

(スクラムマスターフィードバック設定)

### 先週行った振り返り

スプリントゴールどこまで達成できたか

- 今週のスプリントゴール：ユーザーがログインできる
    - 達成できた
        - コードフリーズ後なのでリリースはまだ

****象、死んだ魚、嘔吐****: 

[ふりかえり手法「象、死んだ魚、嘔吐」でチームの闇と向き合おう - Qiita](https://qiita.com/piyonakajima/items/ad3c44d1dc377e41d394)

- 狙い: 課題だけを扱う
- 手順
    
    
    ```
    * KPTのように「象」「死んだ魚」「嘔吐」それぞれについてタイマーを回し、チームメンバーにふせんを書き出してもらいます。
    * 書き出されたふせんを１枚ずつ紹介し、書いた人が発表します。 （発表されるまで他の人のふせんは見ません）
    * その内容についてチームメンバーは質問を行い内容を深掘り共有します。
    ```
    
- https://www.figma.com/file/I5GPj0YSn0qS0rLzjES4UR/%E6%8C%AF%E3%82%8A%E8%BF%94%E3%82%8A%E3%80%80%E8%B1%A1%E3%80%81%E6%AD%BB%E3%82%93%E3%81%A0%E9%AD%9A%E3%80%81%E5%98%94%E5%90%90?type=whiteboard&node-id=0%3A1&t=uDW7PfWPyMcvXRcS-1

- TOPIC
    - 主に課題がいろいろ出ました
        - 開発負荷
            - TLに対する負荷
                - QAは分担することになりました
            - ペアプロ頼みづらい。開発が一人だとつらい。
                - まずは依頼すること
        - POの負荷
            - POは発表のみでスクラムマスターが現在の状況についての資料は作成する
    - etc…..

振り返りの振り返り

- TOPIC
    - 雰囲気は重くなる
    - 課題 → 改善になる
    - 抱えている思いを話す場になる
- 内容
    - 今回の振り返りでいいと思ったこと
        - 課題がわかり改善につながる @Kenta Nakayama
        - 実は抱えているけど言えなかったことを言う機会があるのは助かる @Dai Miyahara
        - 向き合うべき課題に向き合う機会になる  @Dai Miyahara
        - 課題が丸裸になる感じで、いい(改善活動がススム)
        - 
        - 忖度なく課題を伝えられていた @大野寛人
        - 重要な課題の意識合わせに役立ちます @FERNANDEZ
        - 胸の中にある課題→この項目があると自分の悩みが言いやすくなってよい　@鈴木真希
    - 今回の振り返りでよくないと思ったこと
        - 時間が結構かかってしまっていた @大野寛人
        - テーマが多くて時間が足りなくなりました。 @FERNANDEZ
        - ずっとつらみに向き合って空気が重い @satoshi.hirata
        - テーマが課題のみなので雰囲気が重くなるのと時間が長くなる @Kenta Nakayama
        - 褒める喜ぶセッションがない
            - 別で用意してもいいね
        - 向き合うことができない人にとっては辛い時間なのでは @Dai Miyahara
        - 課題にフォーカスすると時間がかかる。仕方がないが… @Dai Miyahara
        - 空気が重い @鈴木真希
    - KPTと比較してどうか
        - 毎週は必要ないかもしれないが、課題を吐き出す会として月一くらいでやるのは良いかもしれない @大野寛人 @Dai Miyahara
        - KPTより具体的な話に持っていきやすい
        - もっと頻繁にすれば時間がそんなにかからなくなるかもしれません。 @FERNANDEZ
        - スコープが広くなる。スプリント単位ではない。 @Kenta Nakayama
            - KPTより課題が多くなる。着眼点が課題なのでそれはそう。
        - 個人個人が抱える課題についても話せるのがよいと思った @Dai Miyahara
        - 毎週よりかは毎月、クォーターごとにしたほうが、課題の内容もかわると思うので、より効果がでるのでは　@鈴木真希
    - その他
        - 空気感は組織課題であって、振り返り手法の責務範囲ではないと思う
            - [ずっとつらみに向き合って空気が重い @satoshi.hirata ](https://www.notion.so/f5ffd1f9a9ed4c638f3942f66ecf2246?pvs=21)
            - [空気が重い @鈴木真希 ](https://www.notion.so/544fde0a98ff488fbe96bc501b1bc733?pvs=21)
        - ↑たしかに @Dai Miyahara
        - メンバーが課題を溜め込んで雰囲気悪くなるよりは、若干雰囲気重くても課題を共有して改善できた方がチームとしてプラスなような気がしました。 @大野寛人
        - ↑同意 @Dai Miyahara

### 今週のスプリントゴール

- https://chubachi-pt-2023.atlassian.net/browse/AT-268
- https://chubachi-pt-2023.atlassian.net/browse/AT-267
- https://chubachi-pt-2023.atlassian.net/browse/AT-573

### 今週のアウトプット

@FERNANDEZ 

https://chubachi-pt-2023.atlassian.net/browse/AT-600　（https://chubachi-pt-2023.atlassian.net/browse/AT-441）

https://chubachi-pt-2023.atlassian.net/browse/AT-598

https://chubachi-pt-2023.atlassian.net/browse/AT-615（ベロシティーのため水野さんに助けてもらいました**🙏**）

- 今週の動作確認：[11/5 @FERNANDEZ ](https://www.notion.so/11-5-3172af84e81f4ae2ae327029b5ea4ab6?pvs=21)

@satoshi.hirata 

主にインフラ関連と商品画像を表示させる為のAPI実装、一部不具合修正

https://chubachi-pt-2023.atlassian.net/browse/AT-608

https://chubachi-pt-2023.atlassian.net/browse/AT-609

https://chubachi-pt-2023.atlassian.net/browse/AT-442

https://chubachi-pt-2023.atlassian.net/browse/AT-610

https://chubachi-pt-2023.atlassian.net/browse/AT-627

https://chubachi-pt-2023.atlassian.net/browse/AT-629

@鈴木真希 
https://chubachi-pt-2023.atlassian.net/browse/AT-565

@大野寛人

https://chubachi-pt-2023.atlassian.net/browse/AT-611

@Dai Miyahara 

[着手中]

- https://chubachi-pt-2023.atlassian.net/browse/AT-90
- https://chubachi-pt-2023.atlassian.net/browse/AT-434

→　バックエンドコンテナの起動に手こずっている。今週も同タスクに着手予定。

@Kenta Nakayama 

[着手中]

https://chubachi-pt-2023.atlassian.net/browse/AT-621?atlOrigin=eyJpIjoiMDYzOGVmYjZjYjYzNGQ2ZDgzZGMyMjc1ZGIwMTU1MTAiLCJwIjoiaiJ9

[DONE]

https://chubachi-pt-2023.atlassian.net/browse/AT-572?atlOrigin=eyJpIjoiYTZiYThhMjA2MGJkNGM2MmExZmUwMjMxYzcwYWI1NzQiLCJwIjoiaiJ9

https://chubachi-pt-2023.atlassian.net/browse/AT-548?atlOrigin=eyJpIjoiYjM3ZWI4M2MwZTVjNDQzYjg2OWExYzgwMGFkN2IxNDAiLCJwIjoiaiJ9

[そのほか]

10月の振り返りの内容まとめた

@Hibiki Mizuno 

落ち穂拾い：

https://chubachi-pt-2023.atlassian.net/browse/AT-590

イネーブラー(技術的な課題)：

https://chubachi-pt-2023.atlassian.net/browse/AT-479

https://chubachi-pt-2023.atlassian.net/browse/AT-596

https://chubachi-pt-2023.atlassian.net/browse/AT-602

次回スプリントのための作業：

https://chubachi-pt-2023.atlassian.net/browse/AT-603

今スプリントのゴールのための作業：

https://chubachi-pt-2023.atlassian.net/browse/AT-614

https://chubachi-pt-2023.atlassian.net/browse/AT-625

https://chubachi-pt-2023.atlassian.net/browse/AT-619

https://chubachi-pt-2023.atlassian.net/browse/AT-618

その他：

https://chubachi-pt-2023.atlassian.net/browse/AT-628

- **メモ**
    - 「象、死んだ魚、嘔吐」振り返り手法で雰囲気が変わる
    しかしポジティブな振り返り手法だと改善しにくい、バランスが必要
    - 認証の実装の難点、今後SSRを使いたい。NextJSのバージョンが問題になっている
    - ユーザーストーリの分かるデモがあると良い。プロダクトの価値を表現できるデモ
    - マンスリレビュー：全体を紹介する方法で進めた方が良い