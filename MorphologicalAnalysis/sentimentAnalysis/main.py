import csv
import pprint
from util import group_values_by_key
from kpt import kpt
from star_fish import star_fish
from speed_car import speed_car
from fun_done_learn import fun_done_learn
from analysis import sentiment_analyse
from elephant_fish import elephant_fish
from files import get_csv_files_by_dir,generate_path,read_markdown_file

def elephant_fish_res():
    # === 象、死んだ魚、嘔吐 ===
    _elephant_fish = elephant_fish()

    # Jira
    _elephant_fish_jira_1_result = []
    for item in _elephant_fish['Jira (1)']:
        _elephant_fish_jira_1_result.append(
            {
                'summary': sentiment_analyse(item['summary']),
                'comment': sentiment_analyse(item['comment']),
                'description': sentiment_analyse(item['description']),
            }
        )
    print("Jira (1)")
    data_len = len(_elephant_fish_jira_1_result)
    summary_scores=sum([item['summary'] for item in _elephant_fish_jira_1_result])
    comment_scores=sum([item['comment'] for item in _elephant_fish_jira_1_result])
    description_scores=sum([item['description'] for item in _elephant_fish_jira_1_result])
    print(' summary: ',summary_scores/data_len )
    print(' comment: ',comment_scores/data_len )
    print(' description: ',description_scores/data_len )
    print(' トータル: ',(summary_scores+comment_scores+description_scores)/(data_len*3) )

    # Jira
    _elephant_fish_jira_result = []
    for item in _elephant_fish['Jira']:
        _elephant_fish_jira_result.append(
            {
                'summary': sentiment_analyse(item['summary']),
                'comment': sentiment_analyse(item['comment']),
                'description': sentiment_analyse(item['description']),
            }
        )
    data_len = len(_elephant_fish_jira_result)
    summary_scores=sum([item['summary'] for item in _elephant_fish_jira_result])
    comment_scores=sum([item['comment'] for item in _elephant_fish_jira_result])
    description_scores=sum([item['description'] for item in _elephant_fish_jira_result])
    print("Jira")
    print(' summary: ', summary_scores/data_len )
    print(' comment: ',  comment_scores/data_len )
    print(' description: ',  description_scores/data_len )
    print(' トータル: ',(summary_scores+comment_scores+description_scores)/(data_len*3) )

    # FigJam
    _elephant_fish_retro_result = []
    for item in _elephant_fish['retro']:
        _elephant_fish_retro_result.append(
            {
                item['Created by']: sentiment_analyse(item['Content']),
            }
        )
    _elephant_fish_retro_by_user = {}
    for name, val in group_values_by_key(_elephant_fish_retro_result).items():
        _elephant_fish_retro_by_user[name] = sum(val)/len(val)
    print("振り返り　象、死んだ魚、嘔吐 (11月分)")
    for key, value in _elephant_fish_retro_by_user.items():
        print(" {}: {}".format(key, value))
    print("FigJam avg: ", sum([value for key, value in _elephant_fish_retro_by_user.items()])/len(_elephant_fish_retro_by_user.items()))

    # Notion
    print("Notion: \n Content: ", sentiment_analyse(_elephant_fish['notion']))

    # Slack
    print("Slack: ")
    _slack:dict = _elephant_fish['slack']
    for key, value in _slack.items():
        if len(value) > 0:
            res = sentiment_analyse("".join(value))
            print(" {}: {}".format(key, res))
    print("Slack avg: ", sum([sentiment_analyse("".join(value)) for key, value in _slack.items()])/len(_slack.items()))


def fun_done_learn_res():
    # === fun done learn ===
    _fun_done_learn = fun_done_learn()

    # Jira
    fun_done_learn_jira_1_result = []
    for item in _fun_done_learn['Jira (1)']:
        fun_done_learn_jira_1_result.append(
            {
                'summary': sentiment_analyse(item['summary']),
                'comment': sentiment_analyse(item['comment']),
                'description': sentiment_analyse(item['description']),
            }
        )
    data_len = len(fun_done_learn_jira_1_result)
    summary_scores=sum([item['summary'] for item in fun_done_learn_jira_1_result])
    comment_scores=sum([item['comment'] for item in fun_done_learn_jira_1_result])
    description_scores=sum([item['description'] for item in fun_done_learn_jira_1_result])
    print("Jira (1)")
    print(' summary: ',summary_scores/data_len )
    print(' comment: ',comment_scores/data_len )
    print(' description: ',description_scores/data_len )
    print(' トータル: ',(summary_scores+comment_scores+description_scores)/(data_len*3) )

    # Jira
    fun_done_learn_jira_result = []
    for item in _fun_done_learn['Jira']:
        fun_done_learn_jira_result.append(
            {
                'summary': sentiment_analyse(item['summary']),
                'comment': sentiment_analyse(item['comment']),
                'description': sentiment_analyse(item['description']),
            }
        )
    data_len = len(fun_done_learn_jira_result)
    summary_scores=sum([item['summary'] for item in fun_done_learn_jira_result])
    comment_scores=sum([item['comment'] for item in fun_done_learn_jira_result])
    description_scores=sum([item['description'] for item in fun_done_learn_jira_result])
    print("Jira")
    print(' summary: ', summary_scores/data_len )
    print(' comment: ',  comment_scores/data_len )
    print(' description: ',  description_scores/data_len )
    print(' トータル: ',(summary_scores+comment_scores)/(data_len*2) )

    # FigJam
    fun_done_learn_retro_result = []
    for item in _fun_done_learn['retro']:
        fun_done_learn_retro_result.append(
            {
                item['Created by']: sentiment_analyse(item['Content']),
            }
        )
    # print("fun,done,learn")
    # print(' Content: ', sum([item['Content'] for item in fun_done_learn_retro_result])/len(fun_done_learn_retro_result) )
    fun_done_learn_retro_by_user = {}
    for name, val in group_values_by_key(fun_done_learn_retro_result).items():
        fun_done_learn_retro_by_user[name] = sum(val)/len(val)
    print("振り返り　fun,done,learn")
    for key, value in fun_done_learn_retro_by_user.items():
        print(" {}: {}".format(key, value))
    print("FigJam avg: ", sum([value for key, value in fun_done_learn_retro_by_user.items()])/len(fun_done_learn_retro_by_user.items()))

    # Notion
    print("Notion: \n Content: ", sentiment_analyse(_fun_done_learn['notion']))

    # Slack
    print("Slack: ")
    _slack:dict = _fun_done_learn['slack']
    for key, value in _slack.items():
        if len(value) > 0:
            res = sentiment_analyse("".join(value))
            print(" {}: {}".format(key, res))
    print("Slack avg: ", sum([sentiment_analyse("".join(value)) for key, value in _slack.items()])/len(_slack.items()))


def speed_car_res():
    ## === speed car ===
    _speed_car = speed_car()

    # Jira
    _speed_car_jira_1_result = []
    for item in _speed_car['Jira2']:
        _speed_car_jira_1_result.append(
            {
                'summary': sentiment_analyse(item['summary']),
                'comment': sentiment_analyse(item['comment']),
                'description': sentiment_analyse(item['description']),
            }
        )

    data_len = len(_speed_car_jira_1_result)
    summary_scores=sum([item['summary'] for item in _speed_car_jira_1_result])
    comment_scores=sum([item['comment'] for item in _speed_car_jira_1_result])
    description_scores=sum([item['description'] for item in _speed_car_jira_1_result])
    print("Jira2")
    print(' summary: ',summary_scores/data_len )
    print(' comment: ',comment_scores/data_len )
    print(' description: ',description_scores/data_len )
    print(' トータル: ',(summary_scores+comment_scores+description_scores)/(data_len*3) )

    # Jira
    _speed_car_jira_result = []
    for item in _speed_car['Jira']:
        _speed_car_jira_result.append(
            {
                'summary': sentiment_analyse(item['summary']),
                'comment': sentiment_analyse(item['comment']),
                'description': sentiment_analyse(item['description']),
            }
        )
    data_len = len(_speed_car_jira_result)
    summary_scores=sum([item['summary'] for item in _speed_car_jira_result])
    comment_scores=sum([item['comment'] for item in _speed_car_jira_result])
    description_scores=sum([item['description'] for item in _speed_car_jira_result])
    print("Jira")
    print(' summary: ', summary_scores/data_len )
    print(' comment: ',  comment_scores/data_len )
    print(' description: ',  description_scores/data_len )
    print(' トータル: ',(summary_scores+comment_scores+description_scores)/(data_len*3) )

    # FigJam
    _speed_car_retro_result = []
    for item in _speed_car['retro']:
        _speed_car_retro_result.append(
            {
                item['Created by']: sentiment_analyse(item['Content']),
            }
        )
    # print("speed car: \n Content: ", sum([item['Content'] for item in _speed_car_retro_result])/len(_speed_car_retro_result) )
    _speed_car_retro_by_user = {}
    for name, val in group_values_by_key(_speed_car_retro_result).items():
        _speed_car_retro_by_user[name] = sum(val)/len(val)
    print("振り返り　speed car")
    for key, value in _speed_car_retro_by_user.items():
        print(" {}: {}".format(key, value))
    print("FigJam avg: ", sum([value for key, value in _speed_car_retro_by_user.items()])/len(_speed_car_retro_by_user.items()))

    # Notion
    print("Notion: \n Content: ", sentiment_analyse(_speed_car['notion']))

    # Slack
    print("Slack: ")
    _slack:dict = _speed_car['slack']
    for key, value in _slack.items():
        if len(value) > 0:
            res = sentiment_analyse("".join(value))
            print(" {}: {}".format(key, res))
    print("Slack avg: ", sum([sentiment_analyse("".join(value)) for key, value in _slack.items()])/len(_slack.items()))


def star_fish_res():
    # === star fish ===
    _star_fish = star_fish()

    # Jira
    _star_fish_jira_1_result = []
    for item in _star_fish['Jira (1)']:
        _star_fish_jira_1_result.append(
            {
                'summary': sentiment_analyse(item['summary']),
                'comment': sentiment_analyse(item['comment']),
                'description': sentiment_analyse(item['description']),
            }
        )
    data_len = len(_star_fish_jira_1_result)
    summary_scores=sum([item['summary'] for item in _star_fish_jira_1_result])
    comment_scores=sum([item['comment'] for item in _star_fish_jira_1_result])
    description_scores=sum([item['description'] for item in _star_fish_jira_1_result])
    print("Jira (1)")
    print(' summary: ',summary_scores/data_len )
    print(' comment: ',comment_scores/data_len )
    print(' description: ',description_scores/data_len )
    print(' トータル: ',(summary_scores+comment_scores+description_scores)/(data_len*3) )

    # Jira
    _star_fish_jira_result = []
    for item in _star_fish['Jira']:
        _star_fish_jira_result.append(
            {
                'summary': sentiment_analyse(item['summary']),
                'comment': sentiment_analyse(item['comment']),
                'description': sentiment_analyse(item['description']),
            }
        )
    data_len = len(_star_fish_jira_result)
    summary_scores=sum([item['summary'] for item in _star_fish_jira_result])
    comment_scores=sum([item['comment'] for item in _star_fish_jira_result])
    description_scores=sum([item['description'] for item in _star_fish_jira_result])
    print("Jira")
    print(' summary: ', summary_scores/data_len )
    print(' comment: ',  comment_scores/data_len )
    print(' description: ',  description_scores/data_len )
    print(' トータル: ',(summary_scores+comment_scores+description_scores)/(data_len*3) )

    # FigJam
    _star_fish_retro_result = []
    for item in _star_fish['retro']:
        _star_fish_retro_result.append(
            {
                item['Created by']: sentiment_analyse(item['Content']),
            }
        )
    # print(' Content: ', sum([item['Content'] for item in _star_fish_retro_result])/len(_star_fish_retro_result) )
    _star_fish_retro_by_user = {}
    for name, val in group_values_by_key(_star_fish_retro_result).items():
        _star_fish_retro_by_user[name] = sum(val)/len(val)
    print("振り返り　star fish")
    for key, value in _star_fish_retro_by_user.items():
        print(" {}: {}".format(key, value))
    print("FigJam avg: ", sum([value for key, value in _star_fish_retro_by_user.items()])/len(_star_fish_retro_by_user.items()))


    # Notion
    print("Notion: \n Content: ", sentiment_analyse(_star_fish['notion']))

    # Slack
    print("Slack: ")
    _slack:dict = _star_fish['slack']
    for key, value in _slack.items():
        if len(value) > 0:
            res = sentiment_analyse("".join(value))
            print(" {}: {}".format(key, res))
    print("Slack avg: ", sum([sentiment_analyse("".join(value)) for key, value in _slack.items()])/len(_slack.items()))


def kpt_res():
    # === KPT ===
    _kpt = kpt()

    # Jira
    _kpt_jira_1_result = []
    for item in _kpt['Jira (1)']:
        _kpt_jira_1_result.append(
            {
                'summary': sentiment_analyse(item['summary']),
                'comment': sentiment_analyse(item['comment']),
                'description': sentiment_analyse(item['description']),
            }
        )
    data_len = len(_kpt_jira_1_result)
    summary_scores=sum([item['summary'] for item in _kpt_jira_1_result])
    comment_scores=sum([item['comment'] for item in _kpt_jira_1_result])
    description_scores=sum([item['description'] for item in _kpt_jira_1_result])
    print("Jira (1)")
    print(' summary: ',summary_scores/data_len )
    print(' comment: ',comment_scores/data_len )
    print(' description: ',description_scores/data_len )
    print(' トータル: ',(summary_scores+comment_scores+description_scores)/(data_len*3) )

    # Jira
    _kpt_jira_result = []
    for item in _kpt['Jira']:
        _kpt_jira_result.append(
            {
                'summary': sentiment_analyse(item['summary']),
                'comment': sentiment_analyse(item['comment']),
                'description': sentiment_analyse(item['description']),
            }
        )
    data_len = len(_kpt_jira_result)
    summary_scores=sum([item['summary'] for item in _kpt_jira_result])
    comment_scores=sum([item['comment'] for item in _kpt_jira_result])
    description_scores=sum([item['description'] for item in _kpt_jira_result])
    print("Jira")
    print(' summary: ', summary_scores/data_len )
    print(' comment: ',  comment_scores/data_len )
    print(' description: ',  description_scores/data_len )
    print(' トータル: ',(summary_scores+comment_scores+description_scores)/(data_len*3) )

    # Notion
    print("Notion: \n Content: ", sentiment_analyse(_kpt['notion']))

    # Slack
    print("Slack: ")
    _slack:dict = _kpt['slack']
    for key, value in _slack.items():
        if len(value) > 0:
            res = sentiment_analyse("".join(value))
            print(" {}: {}".format(key, res))
    print("Slack avg: ", sum([sentiment_analyse("".join(value)) for key, value in _slack.items()])/len(_slack.items()))

if __name__ == '__main__':
    # 参考: 
    # 褒める:  0.99998
    # 今日はいい天気ですね:  0.20651
    # あーあ、残念。うなぎを食べそこねた。:  -0.99596
    # db/seeds.rb#L28 で強制的にアップデートをかけている部分の削除もお願いします:  -0.51265
    # プロダクトいいとこまで行けると良いな:  0.3921
    # print("褒める: ",sentiment_analyse('褒める'))

    # 分析結果

    print("象、死んだ魚、嘔吐 (11月)\n")
    elephant_fish_res()
    print("\n\n")

    print("fun,done,learn\n")
    fun_done_learn_res()
    print("\n\n")

    print("speed car\n")
    speed_car_res()
    print("\n\n")

    print("star fish\n")
    star_fish_res()
    print("\n\n")

    print("KPT\n")
    kpt_res()
    print("\n\n")
