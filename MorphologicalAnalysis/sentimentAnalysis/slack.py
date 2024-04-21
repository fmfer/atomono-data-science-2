import os
import json
from functools import reduce
import pprint

# 中鉢PT.* というでディレクトリの名前を取る。その中の各チャンネル名のディレクトリ内のjsonファイルを取得する。
def slack(dir_name):
    res = read_json_files(dir_name)
    all_text_dic = {} # ユーザー別にtextを配列に格納
    for json_data in res:
        dic = extract_text_from_slack(json_data)
        if len(dic) == 0: continue
        for key, value in dic.items():
            if all_text_dic.get(key) is None:
                all_text_dic[key] = []
            if len(value):
                all_text_dic[key].append(reduce(lambda a, b: a + b, value))
    # flatMap
    for key, value in all_text_dic.items():
        if len(value):
            all_text_dic[key] = reduce(lambda a, b: a + b, value)
    return all_text_dic


def read_json_files(directory):
    """
    Find all JSON files in the specified directory and its subdirectories.

    Parameters:
    directory (str): The path to the directory.

    Returns:
    list: A list of relative paths to the JSON files.
    """
    json_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                json_files.append(directory+os.path.relpath(file_path, start=directory))
    json_files_raw_data = []
    for item in json_files:
        file_path = item
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data: list = json.load(json_file)
                json_files_raw_data.append(data)
        except Exception as e:
            print(f"Failed to read {file_path}: {e}")
    return json_files_raw_data

def extract_text_from_slack(data: list):
    """
    Extract text from a Slack JSON file.

    Parameters:
    data (dict): The JSON data loaded from the Slack JSON file.

    Returns:
    str: The extracted text.
    """
    results = []
    dic = {}
    username = ''
    for datum in data:
        if 'user_profile' in datum:
            username = datum['user_profile']['first_name']
            dic[username] = []
        if len(username) == 0: return dic
        if 'blocks' in datum:
            for block in datum['blocks']:
                if 'elements' in block:
                    for element in block['elements']:
                        if 'elements' in element:
                            for item in element['elements']:
                                if 'text' in item:
                                    txt = item['text']
                                    if txt:
                                        results.append(txt)
                                        dic[username].append([txt])
    return dic
